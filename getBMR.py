def getBMR(weightLBS, heightINCHES, age):   
    weightKG = weightLBS*.453592
    heightCM = heightINCHES*2.54
    BMR = 10*weightKG+.25*heightCM-5*age+5
    return BMR
