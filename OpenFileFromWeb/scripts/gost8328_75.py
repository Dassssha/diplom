import adsk.core, adsk.fusion, adsk.cam, traceback, math


# def run(parametres, Description):
#     # rootComp = design.rootComponent
#     # occurence = rootComp.occurrences.item(rootComp.occurrences.count-1)

#     # parametres = occurence.component.parentDesign.allParameters
#     params = Description.split("/")
#     parametres.itemByName('d').expression = params[0]
#     parametres.itemByName('D').expression = params[1]
#     parametres.itemByName('B').expression = params[2]
#     parametres.itemByName('_r').expression = params[3]
#     parametres.itemByName('_r1').expression = params[4]

def run(occurence, Description):
    # Переменные
    params = Description.split("/")
    d = float(params[0])
    D = float(params[1])
    B = float(params[2])
    r = float(params[3])
    r1 = float(params[4])

    ADA = B*0.25
    BID1 = d + (D-d)/3.33333333
    KAD1 = BID1 + 1.33333 * (D-d)/3.33333333
    KID1 = BID1 / 1.11111111111

    CylCount = round(math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

    # Стандартные получалки
    app = adsk.core.Application.get()
    ui  = app.userInterface
    design = app.activeProduct
    components = design.allComponents
    rootComp = design.rootComponent

    # Получаем массив
    patternFeature = occurence.component.features.circularPatternFeatures[0]
    # Получаем скетч и его размеры
    sketches = occurence.component.sketches[0]
    sketchDimensions = sketches.sketchDimensions
    # Получаем коллекцию скруглений
    filletFeatures = occurence.component.features.filletFeatures
    
    # Вносим новые параметры
    sketchDimensions[0].parameter.expression = str(B) + " mm"
    sketchDimensions[1].parameter.expression = str(d) + " mm"
    sketchDimensions[2].parameter.expression = str(ADA) + " mm"
    sketchDimensions[3].parameter.expression = str(KID1) + " mm"
    sketchDimensions[4].parameter.expression = str(BID1) + " mm"
    sketchDimensions[5].parameter.expression = str(KAD1) + " mm"
    sketchDimensions[8].parameter.expression = str(D) + " mm"
    
    # Изменяем количество цилиндров
    patternFeature.quantity.expression = str(CylCount)

    # Правим скругления
    filletFeatures[0].edgeSets[0].radius.expression = str(r) + " mm"
    filletFeatures[1].edgeSets[0].radius.expression = str(r1) + " mm"