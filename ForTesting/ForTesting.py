#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, math



def run(context):
    ui = None
    try:
        params = {"d":300, "D":620, "B":185, "r":10,"r1":7.5}
        d = params["d"]
        D = params["D"]
        B = params["B"]
        r = params["r"]
        r1 = params["r1"]

        ADA = B*0.25
        BID1 = d + (D-d)/3.33333333
        KAD1 = BID1 + 1.33333 * (D-d)/3.33333333
        KID1 = BID1 / 1.11111111111

        CylCount = round(math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        components = design.allComponents
        rootComp = design.rootComponent
        occurence = rootComp.occurrences.item(rootComp.occurrences.count-1)
        sketches = occurence.component.sketches[0]
        sketchDimensions = sketches.sketchDimensions
        _dim = sketchDimensions[0].expression = str(B) + " mm"
        dim = sketchDimensions[2].parameters.expression
        # sketchDimensions[1].expression = str(d) + " mm"
        # sketchDimensions[2].expression = str(B) + " mm"
        # sketchDimensions[3].expression = str(B) + " mm"
        # sketchDimensions[4].expression = str(B) + " mm"
        # sketchDimensions[5].expression = str(B) + " mm"
        # sketchDimensions[6].expression = str(B) + " mm"
        # sketchDimensions[0].expression = str(B) + " mm"

        # parametres = occurence.component.parentDesign.allParameters
        # parametres.itemByName('d').expression = "50 mm"
        # parametres.itemByName('D').expression = "80 mm"
        # parametres.itemByName('B').expression = "16 mm"
        # parametres.itemByName('_r').expression = "1.5 mm"
        # parametres.itemByName('_r1').expression = "1 mm"

        u = 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
