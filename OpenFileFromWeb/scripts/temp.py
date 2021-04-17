import adsk.core, adsk.fusion, adsk.cam, traceback, math

def bearing20001(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component

    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)


    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-1, 4 + dlina, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 4 + dlina, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 3, 0), adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.endSketchPoint, adsk.core.Point3D.create(-0.5, 2.5, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(0.5, 3, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 3, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.startSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

        
    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(7).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 2000"