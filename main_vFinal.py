import time, random

# USER INPUT

set_mode = 1 # (1 = Automatic, 2 = Userdefined Values)
userDefined_fillValue = 26 # (Integer from <minFillValue> to <maxFillValue>)
userDefined_humidityValue = 0 # (Integer of "0" = "OK" or "1" = "NOK")


# ----------------------------------------------------------------------------------------------------


# Function: SCHEDULER

def Scheduler():

    global timeInterval
    global minFillValue
    global maxFillValue
    
    timeInterval = 3 # time in secs between each call
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

    print('\n--- SCHEDULER WURDE AUFGERUFEN ---\n')


# ----------------------------------------------------------------------------------------------------


# Function: SIMULATOR

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
                fillValueTimeFactor = tendencyRange / timeInterval # get factor of fillValue and tendencyRange
                #print(f'Faktor (gerunded) aus Tendenzlänge & Zeitintervall: {round(fillValueTimeFactor, 1)}')
                currentTendencyRange = tendencyRange - tendencyRangeCounter
                followingValue = int(round((fillValueTimeFactor / currentTendencyRange) + currentTendencyRange, 0)) # get rounded addition value
                #print(followingValue)
                fillValue = fillValue + followingValue # add to fillValue
                tendencyRangeCounter = tendencyRangeCounter + 1
            else:
                tendency = 1
                tendencyRange = random.randint(3, 7)
                tendencyRangeCounter = 0
        
        # when subtraction-tendency

        else:
            if tendencyRange != tendencyRangeCounter:
                fillValueTimeFactor = tendencyRange / timeInterval # get factor of fillValue and tendencyRange
                #print(f'Faktor aus Tendenzlänge & Zeitintervall: {round(fillValueTimeFactor, 1)}')
                currentTendencyRange = tendencyRangeCounter + 1
                followingValue = int(round((fillValueTimeFactor / currentTendencyRange) + currentTendencyRange, 0)) # get subtraction addition value
                #print(followingValue)
                fillValue = fillValue - followingValue # subtract from fillValue
                tendencyRangeCounter = tendencyRangeCounter + 1
            else:
                tendency = 0
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


# ----------------------------------------------------------------------------------------------------


# Function: USERDEFINED VALUES

def userdefinedValues(fillValue, humidityValue):
    
    # check if humidityValue is in defined region 

    if humidityValue < 0 or humidityValue > 1:
        print(f'Fehler: "humidityValue" kann nur den Wert "0" (OK) oder "1" (NOK) annehmen.')
        exit()

    # check if vars are in defined region

    if fillValue < minFillValue or fillValue > maxFillValue:
        print(f'Fehler: "fillValue" darf den min. Wert "{minFillValue}" nicht unterschreiten oder den max. Wert "{maxFillValue}" überschreiten.')     
        exit()
    else:
        if type(fillValue) == int:
            print(f'Wasserspeicher-Füllstand beträgt: {fillValue}')
        else:
            print('Fehler: "fillValue" muss ein Wert vom Typ Integer sein/eine ganze Zahl sein.')
            exit()

    if humidityValue == 0:
        print('Feuchtigkeit ist: OK')
    else:
        print('Feuchtigkeit ist: NOK')


# ----------------------------------------------------------------------------------------------------


# CONTROL

# setting start-vars

lastRun = None
currentRun = None

def Control():
    
    global lastRun
    global currentRun

    # fillValue (>max) & humidityValue (OK/NOK)
    
    if fillValue > maxFillValue and humidityValue == 0:
        currentRun = 'Ventil: OUT\nPumpe: Entwässern'
    elif fillValue > maxFillValue and humidityValue == 1:
        currentRun = 'Ventil: IN\nPumpe: Gießen'
        
    # fillValue (okay) & humidityValue (OK/NOK)
    
    elif fillValue < maxFillValue and fillValue > minFillValue and humidityValue == 0:
        currentRun = 'Ventil: IN\nPumpe: Aus'
    elif fillValue < maxFillValue and fillValue > minFillValue and humidityValue == 1:
        currentRun = 'Ventil: IN\nPumpe: Gießen'
    
    # fillValue (<min) & humidityValue (OK/NOK)
    
    elif fillValue < minFillValue and humidityValue == 0:
        currentRun = 'Ventil: OUT\nPumpe: Aus'
    elif fillValue < minFillValue and humidityValue == 1:
        currentRun = 'Ventil: OUT\nPumpe: Gießen'

    if currentRun != lastRun:
        print(currentRun)
    else:
        print('Es müssen keine Änderungen vorgenommen werden.\n')

    lastRun = currentRun
    

# ----------------------------------------------------------------------------------------------------


# PROCESS-LOOP

while True:
    Scheduler()

    if set_mode == 1:
        Simulator() # select mode 1
    elif set_mode == 2:
        fillValue = userDefined_fillValue
        humidityValue = userDefined_humidityValue
        userdefinedValues(fillValue, humidityValue) # select mode 2
    else:
        print(f'Fehler: Es kann nur zwischen Mode "1" und Mode "2" gewählt werden.')
        exit()

    Control()

    for x in range(timeInterval):
        time.sleep(1)
        #print(f'{timeInterval - x - 1} Sekunde(n) bis zum Aufruf.')