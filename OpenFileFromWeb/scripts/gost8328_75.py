import adsk.core, adsk.fusion, adsk.cam, traceback, math


def run(parametres, Description):
    # rootComp = design.rootComponent
    # occurence = rootComp.occurrences.item(rootComp.occurrences.count-1)

    # parametres = occurence.component.parentDesign.allParameters
    params = Description.split("/")
    parametres.itemByName('d').expression = params[0]
    parametres.itemByName('D').expression = params[1]
    parametres.itemByName('B').expression = params[2]
    parametres.itemByName('_r').expression = params[3]
    parametres.itemByName('_r1').expression = params[4]
