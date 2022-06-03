import random, time

timeInterval = 10 # time in secs between each call
minFillValue = 0 # minimal Fill Value for water tank
maxFillValue = 100 # maximal Fill Value for water tan

firstCall = True # stating whether first call or not
tendency = random.randint(0, 1) # generating randomly whether increasing or decreasing tendency
tendencyRange = random.randint(3, 7) # generating random tendency range
tendencyRangeCounter = 0 # counting current tendencyRange status
isLimit = False # stating whether value reachs limit or not

def Simulator():
    global firstCall
    global fillValue
    global tendency
    global tendencyRange
    global tendencyRangeCounter
    global fillValue
    global humidityValue
    global isLimit

    # SIMULATOR: FILL-VALUE

    # firstCall: check if first call or not

    if firstCall == True: # "True": is first call
        fillValue = random.randint(minFillValue, maxFillValue)
        firstCall = False
        if fillValue > maxFillValue:
            fillValueState = "Zu Hoch"
        elif fillValue < minFillValue:
            fillValueState = "Zu Klein"
        else:
            fillValueState = "Okay"
        print(f'Wasserspeicher-Füllstand beträgt: {fillValue} ({fillValueState})')
    else: # "False": is not first call

        # when addition-tendency
        
        if tendency == 0:
            if tendencyRange != tendencyRangeCounter:
                fillValueTimeFactor = tendencyRange / timeInterval
                currentTendencyRange = tendencyRange - tendencyRangeCounter
                factor = int(round((fillValueTimeFactor / currentTendencyRange) + currentTendencyRange, 0))
                print(factor)
                fillValue = fillValue + factor
                tendencyRangeCounter = tendencyRangeCounter + 1
            else:
                tendency = random.randint(0, 1)
                tendencyRange = random.randint(3, 7)
                tendencyRangeCounter = 0
        
        # when subtraction-tendency

        else:
            if tendencyRange != tendencyRangeCounter:
                fillValueTimeFactor = tendencyRange / timeInterval
                currentTendencyRange = tendencyRangeCounter + 1
                factor = int(round((fillValueTimeFactor / currentTendencyRange) + currentTendencyRange, 0))
                print(factor)
                fillValue = fillValue - factor
                tendencyRangeCounter = tendencyRangeCounter + 1
            else:
                tendency = random.randint(0, 1)
                tendencyRange = random.randint(3, 7)
                tendencyRangeCounter = 0

        # check if vars are in defined region

        if fillValue < minFillValue or fillValue > maxFillValue:
            try:
                Simulator() # not in region: re-call function
                isLimit = True
            except:
                #print('Fehler: "Maximum recursion depth exceeded in comparison"')
                Simulator()
                isLimit = True
            
        else:
            isLimit = False
            if type(fillValue) == int:
                if fillValue > maxFillValue:
                    fillValueState = "Zu Hoch"
                elif fillValue < minFillValue:
                    fillValueState = "Zu Klein"
                else:
                    fillValueState = "Okay"
                print(f'Wasserspeicher-Füllstand beträgt: {fillValue} ({fillValueState})') # in region: go on
            else:
                print('Fehler: "fillValue" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')
                exit()

    # SIMULATOR: HUMIDITY-VALUE

    if isLimit == False:
        humidityValue = random.randint(0, 1)

        if humidityValue == 0:
            print('Feuchtigkeit ist: OK')
        else:
            print('Feuchtigkeit ist: NOK')

while True:
    Simulator()
    for secs in range(timeInterval):
        time.sleep(1)