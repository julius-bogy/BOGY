import time, random

# Scheduler

def Scheduler():

    # setting global vars

    global timeInterval
    global minFillValue
    global maxFillValue
    
    timeInterval = 1 # time in secs between each call
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

    #print('Scheduler wurde aufgerufen')

# Simulator

firstCall = True # var which states if first call or not

def Simulator():
    global firstCall
    global fillValue
    tendency = random.randint(0, 1)

    # firstCall: check if first call or not

    if firstCall == True: # "True": is first call
        fillValue = random.randint(minFillValue, maxFillValue)
        firstCall = False
    else: # "False": is not first call
        
        # tendency: decides if addition or subtraction

        if tendency == 0:
            fillValue = fillValue + random.randint(0, 10)
        else:
            fillValue = fillValue - random.randint(0, 10)

        # fillValue: check if var is in the defined region

        if fillValue < minFillValue or fillValue > maxFillValue:
            Simulator() # outside of region: call again
        else:
            print(f"Wasserspeicher-Füllstand beträgt: {fillValue}") # inside of region: print & go on

# calling Scheduler-function each <timeInterval> seconds

while True:
    Scheduler()
    Simulator()
    for x in range(timeInterval):
        time.sleep(1)
        #print(f'{timeInterval - x - 1} Sekunde(n) bis zum Aufruf.')