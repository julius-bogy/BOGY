import time, random

# SCHEDULER

def Scheduler():

    global timeInterval
    global minFillValue
    global maxFillValue
    
    timeInterval = 5 # time in secs between each call
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

    if maxFillValue - minFillValue < 10:
        print('Fehler: Zwischen "minFillValue" & "maxFillValue" muss ein Abstand von mind. 10 liegen.')
        exit()

    # check if timeInterval is less or more than defined region

    if timeInterval < 0:
        print('Fehler: "timeInterval" darf den Wert 0 (0s) nicht unterschreiten.')
        exit()

    if timeInterval > 900:
        print('Fehler: "timeInterval" darf den Wert 900 (900s) nicht überschreiten.')
        exit()

    #print('Scheduler wurde aufgerufen')

# SIMULATOR

# setting start-vars

firstCall = True # stating if first call or not
tendency = random.randint(0, 1) # generating randomly if increasing or decreasing tendency
tendencyRange = random.randint(3, 7) # generating random tendency range
tendencyRangeCounter = 0 # counting current tendencyRange status

def Simulator():
    global firstCall
    global fillValue
    global tendency
    global tendencyRange
    global tendencyRangeCounter

    # SIMULATOR: FILL-VALUE

    # firstCall: check if first call or not

    if firstCall == True: # "True": is first call
        fillValue = random.randint(minFillValue, maxFillValue)
        firstCall = False
        print(f"Wasserspeicher-Füllstand beträgt: {fillValue}")
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
            Simulator() # not in region: re-call function
        else:
            print(f"Wasserspeicher-Füllstand beträgt: {fillValue}") # in region: go on

    # SIMULATOR: HUMIDITY-VALUE

    humidityValue = random.randint(0, 1)

    if humidityValue == 0:
        print('Feuchtigkeit ist: OK')
    else:
        print('Feuchtigkeit ist: NOK')


# SYSTEM: PROCESS-LOOP

while True:
    Scheduler()
    Simulator()
    for x in range(timeInterval):
        time.sleep(1)
        #print(f'{timeInterval - x - 1} Sekunde(n) bis zum Aufruf.')