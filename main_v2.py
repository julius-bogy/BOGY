import time, random
global humidityValue
global fillValue

print('Mit welchen Werten möchten sie fortfahren? \n[1] Automatische\n[2] Benutzerdefinierte')
askAction = input('Eingabe (1/2): ')

# SCHEDULER

def Scheduler():

    global timeInterval
    global minFillValue
    global maxFillValue
    
    timeInterval = 10 # time in secs between each call
    minFillValue = 0 # minimal Fill Value for water tank
    maxFillValue = 100 # maximal Fill Value for water tank

    # timeInteval: check if var is set & check if int

    try:
        timeInterval
        if type(timeInterval) != int:
            print('Fehler: "timeInteval" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')
            exit()
    except Exception:
        print('Fehler: "timeInterval" hat keinen gültigen Wert.')
        exit()

    # minFillValue: check if var is set & check if int

    try:
        minFillValue
        if type(minFillValue) != int:
            print('Fehler: "minFillValue" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')
            exit()
    except Exception:
        print('Fehler: "minFillValue" hat keinen gültigen Wert.')
        exit()

    # maxFillValue: check if var is set & check if int

    try:
        maxFillValue
        if type(maxFillValue) != int:
            print('Fehler: "maxFillValue" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')
            exit()
    except Exception:
        print('Fehler: "maxFillValue" hat keinen gültigen Wert.')
        exit()

    # check if minFillValue is less than maxFillValue

    if minFillValue >= maxFillValue:
        print('Fehler: "minFillValue" darf nicht größer oder gleich "maxFillValue" sein.')
        exit()

    # check if there's an min difference of 10

    if maxFillValue - minFillValue < 10:
        print('Fehler: Zwischen "minFillValue" & "maxFillValue" muss ein Abstand von mind. 10 liegen.')
        exit()

    # check if timeInterval is less or more than defined region

    if timeInterval < 1:
        print('Fehler: "timeInterval" darf den Wert 1 (1s) nicht unterschreiten.')
        exit()

    if timeInterval > 900:
        print('Fehler: "timeInterval" darf den Wert 900 (900s) nicht überschreiten.')
        exit()

    #print('Scheduler wurde aufgerufen')






# SIMULATOR

# setting start-vars

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
    global humidityValue
    global isLimit

    # SIMULATOR: FILL-VALUE

    # firstCall: check if first call or not

    if firstCall == True: # "True": is first call
        fillValue = random.randint(minFillValue, maxFillValue)
        firstCall = False
        print(f'Wasserspeicher-Füllstand beträgt: {fillValue}')
    else: # "False": is not first call

        # when addition-tendency

        if tendency == 0:
            if tendencyRange != tendencyRangeCounter:
                fillValue = fillValue + random.randint(0, 10)
                tendencyRangeCounter = tendencyRangeCounter + 1
            else:
                tendency = random.randint(0, 1)
                tendencyRange = random.randint(3, 7)
                tendencyRangeCounter = 0
        
        # when subtraction-tendency

        else:
            if tendencyRange != tendencyRangeCounter:
                fillValue = fillValue - random.randint(0, 10)
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
                print(f'Wasserspeicher-Füllstand beträgt: {fillValue}') # in region: go on
            else:
                print('Fehler: "fillValue" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')

    # SIMULATOR: HUMIDITY-VALUE
    if isLimit == False:
        humidityValue = random.randint(0, 1)

        if humidityValue == 0:
            print('Feuchtigkeit ist: OK')
        else:
            print('Feuchtigkeit ist: NOK')

# CONTROL

def Control():
    
    # fillValue (>max) & humidityValue (OK/NOK)

    if fillValue > maxFillValue and humidityValue == 0:
        print('Ventil: OUT\nPumpe: Entwässern')
    elif fillValue > maxFillValue and humidityValue == 1:
        print('Ventil: IN\nPumpe: Gießen')
    
    # fillValue (okay) & humidityValue (OK/NOK)

    elif fillValue < maxFillValue and fillValue > minFillValue and humidityValue == 0:
        print('Ventil: IN\nPumpe: Aus')
    elif fillValue < maxFillValue and fillValue > minFillValue and humidityValue == 1:
        print('Ventil: IN\nPumpe: Gießen')

    # fillValue (<min) & humidityValue (OK/NOK)

    elif fillValue < minFillValue and humidityValue == 0:
        print('Ventil: OUT\nPumpe: Aus')
    elif fillValue < minFillValue and humidityValue == 1:
        print('Ventil: OUT\nPumpe: Gießen')
    

# SYSTEM: PROCESS-LOOP

if askAction == "1":
    while True:
        Scheduler()
        Simulator()
        Control()
        for x in range(timeInterval):
            time.sleep(1)

elif askAction == "2":
    fillValue = int(input('Eingabe (Füllwert - Int): '))
    humidityValue = int(input('Eingabe (Feuchtigkeit - "OK"/"NOK"): '))
    
    if humidityValue < 0 or humidityValue > 1:
        print(f'Fehler: "{humidityValue}" ist kein Wert für die Feuchtigkeit.')
        exit()
    
    while True:
        Scheduler()
        Control()
        for x in range(timeInterval):
            time.sleep(1)