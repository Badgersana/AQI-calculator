import math

def printSummary(average, locationHigh, aqiHigh):
    print(f'Summary:\n   Location with highest AQI is {locationHigh} ({aqiHigh})\n   Average PM-2.5 concentration: {average}')

#removes decimal places from a float
def truncate(no, dp):
    step = 10.0 ** dp
    
    return math.trunc(step * no) / step

#does the calculation to find the index value of a pollutant
def findIP(cp, ih, il, ch, cl):
    ip = (((ih - il) / (ch - cl)) * (cp - cl)) + il
    ip = round(ip)  

    return ip

def checkPM2(cp):
    if cp <= 12:
        ih, il, ch, cl = 50, 0, 12.0, 0
        
    elif cp >= 12.1 and cp <= 35.4:
        ih, il, ch, cl = 100, 51, 35.4, 12.1
        
    elif cp >= 35.5 and cp <= 55.4:
        ih, il, ch, cl = 150, 101, 55.4, 35.5
        
    elif cp >= 55.5 and cp <= 150.4:
        ih, il, ch, cl = 200, 151, 150.4, 55.5
        
    elif cp >= 150.5 and cp <= 250.4:
        ih, il, ch, cl = 300, 201, 250.4, 150.5
        
    elif cp >= 250.5 and cp <= 500.4:
        ih, il, ch, cl = 500, 301, 500.4, 250.5

    x = findIP(cp, ih, il, ch, cl)
    print(f'   PM-2.5 concentration of {cp} is index level', x)

    return x

def checkPM10(cp):
    if cp <= 54:
        ih, il, ch, cl = 50, 0, 54, 0
        
    elif cp >= 55 and cp <= 154:
        ih, il, ch, cl = 100, 51, 154, 55
        
    elif cp >= 155 and cp <= 254:
        ih, il, ch, cl = 150, 101, 254, 155
        
    elif cp >= 255 and cp <= 354:
        ih, il, ch, cl = 200, 151, 354, 255
        
    elif cp >= 355 and cp <= 424:
        ih, il, ch, cl = 300, 201, 424, 355
        
    elif cp >= 425 and cp <= 604:
        ih, il, ch, cl = 500, 301, 604, 425

    x = findIP(cp, ih, il, ch, cl)
    print(f'   PM-10 concentration of {cp} is index level', x)

    return x

def checkNO2(cp):
    if cp <= 53:
        ih, il, ch, cl = 50, 0, 53, 0
        
    elif cp >= 54 and cp <= 100:
        ih, il, ch, cl = 100, 51, 100, 54
        
    elif cp >= 101 and cp <= 360:
        ih, il, ch, cl = 150, 101, 360, 101
        
    elif cp >= 361 and cp <= 649:
        ih, il, ch, cl = 200, 151, 649, 361
        
    elif cp >= 650 and cp <= 1249:
        ih, il, ch, cl = 300, 201, 1249, 650
        
    elif cp >= 1250 and cp <= 2049:
        ih, il, ch, cl = 500, 301, 2049, 1250
        
    x = findIP(cp, ih, il, ch, cl)
    print(f'   NO-2 concentration of {cp} is index level', x)

    return x

def checkSO2(cp):
    if cp <= 35:
        ih, il, ch, cl = 50, 0, 35, 0
        
    elif cp >= 36 and cp <= 75:
        ih, il, ch, cl = 100, 51, 75, 36
        
    elif cp >= 76 and cp <= 185:
        ih, il, ch, cl = 150, 101, 185, 76
        
    elif cp >= 186 and cp <= 304:
        ih, il, ch, cl = 200, 151, 304, 186
        
    elif cp >= 305 and cp <= 604:
        ih, il, ch, cl = 300, 201, 604, 305
        
    elif cp >= 605 and cp <= 1004:
        ih, il, ch, cl = 500, 301, 1004, 605
        
    x = findIP(cp, ih, il, ch, cl)
    print(f'   SO-2 concentration of {cp} is index level', x)

    return x

def checkCO(cp):
    if cp <= 4.4:
        ih, il, ch, cl = 50, 0, 4.4, 0
        
    elif cp >= 4.5 and cp <= 9.4:
        ih, il, ch, cl = 100, 51, 9.4, 4.5
        
    elif cp >= 9.5 and cp <= 12.4:
        ih, il, ch, cl = 150, 101, 12.4, 9.5
        
    elif cp >= 12.5 and cp <= 15.4:
        ih, il, ch, cl = 200, 151, 15.4, 12.5
        
    elif cp >= 15.5 and cp <= 30.4:
        ih, il, ch, cl = 300, 201, 30.4, 15.5
        
    elif cp >= 30.5 and cp <= 50.4:
        ih, il, ch, cl = 500, 301, 50.4, 30.5
        
    x = findIP(cp, ih, il, ch, cl)
    print(f'   CO concentration of {cp} is index level', x)

    return x

def checkO3(cp):
    x = 0
    if cp >= 125 and cp <= 164:
        ih, il, ch, cl = 150, 101, 164, 125
        x = findIP(cp, ih, il, ch, cl)
        
    elif cp >= 165 and cp <= 204:
        ih, il, ch, cl = 200, 151, 204, 165
        x = findIP(cp, ih, il, ch, cl)
        
    elif cp >= 205 and cp <= 404:
        ih, il, ch, cl = 300, 201, 404, 205
        x = findIP(cp, ih, il, ch, cl)
        
    elif cp >= 405 and cp <= 604:
        ih, il, ch, cl = 500, 301, 604, 405
        x = findIP(cp, ih, il, ch, cl)

    if x >= 125:
        print(f'   O3 concentration of {cp} is index level', x)
        
        return x
    else:
        
        return 0


def main(locationNo):
    average = 0
    locationHigh = ''
    aqiHigh = 0
    counter = 0
    
    
    for i in range(locationNo):
        locationName = input(f'What is the name of location {i + 1}? ')

        cPM2 = float(input('-> Enter PM-2.5 concentration: '))
        if cPM2 >= 0:
            cPM2 = truncate(cPM2, 1)
            x = checkPM2(cPM2)
            average += cPM2
            counter += 1
        else:
            x = 0
        
        cPM10 = float(input('-> Enter PM-10 concentration: '))
        if cPM10 >= 0:
            cPM10 = int(cPM10)
            y = checkPM10(cPM10)
        else:
            y = 0
        
        cNO2 = float(input('-> Enter NO-2 concentration: '))
        if cNO2 >= 0:
            cNO2 = int(cNO2)
            z = checkNO2(cNO2)
        else:
            z = 0

        cSO2 = float(input('-> Enter SO-2 concentration: '))
        if cSO2 >= 0:
            cSO2 = int(cSO2)
            a = checkSO2(cSO2)
        else:
            a = 0

        cCO = float(input('-> Enter CO concentration: '))
        if cCO >= 0:
            cCO = truncate(cCO, 1)
            b = checkCO(cCO)
        else:
            b = 0

        cO3 = float(input('-> Enter O3 concentration: '))
        if cO3 >= 0:
            cO3 = int(cO3)
            c = checkO3(cO3)
        else:
            c = 0

        largest = max(x, y, z, a, b, c)
        print(f'\nAQI for {locationName} is {largest}')

        #finds largest aqi 
        if largest >= aqiHigh:
            aqiHigh = largest
            locationHigh = locationName

        #determines AQI rating
        list1 = [51, 101, 151, 201, 301, 501]
        count = 0
        for i in range(len(list1)):
            if largest >= list1[i]:
                count += 1

        if count == 0:
            aq = 'Good'
        elif count == 1:
            aq = 'Moderate'
        elif count == 2:
            aq = 'Unhealthy for Sensitive Groups'
        elif count == 3:
            aq = 'Unhealthy'
        elif count == 4:
            aq = 'Very Unhealthy'
        elif count == 5:
            aq = 'Hazardous'

        print(f'Air Quality: {aq}\n')
        
    average = average / counter
    printSummary(average, locationHigh, aqiHigh)
        
print('Air Quality Index Calculator')
running = True
while running == True:
    try:
        locationNo = int(input('How many locations for this report? '))
        if locationNo > 0:
            main(locationNo)
            break
    except TypeError:
        print('')

        
    



