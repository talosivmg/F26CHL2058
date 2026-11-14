import sys

def convertTemperature(mode, value):  #function
    if mode == "FtoC":
        return (value - 32) * 5 / 9
    elif mode == "CtoF":
        return (value * 9 / 5) + 32
    else:
        return None

if len(sys.argv) < 2:  #this is the check
    sys.exit(1)

temperatureMode = sys.argv[1]  # get argument

with open("challenge.data", "r") as rawFile:
    contents = rawFile.read().strip()
    contentsValue = float(contents)

result = convertTemperature(temperatureMode, contentsValue) #this is the call

with open("challenge.out", "w") as outputFile:
    outputFile.write(str(result))



"""
import sys
temperatureMode = sys.argv [1]

with open ("challenge.data", "r") as rawFile:
    contents = rawFile.read().strip()
    contentsValue = float(contents)

def convert(inputMode, value):
    if inputMode == "FtoC":
        tempCalculation = ( value -32 ) * 5 / 9
    elif inputMode == "CtoF":
        tempCalculation = ( value * 9 / 5 ) + 32
    return tempCalculation

result = convert(temperatureMode, contentsValue)

with open ( "challenge.out", "w") as outputFile:
    outputFile.write(str(result))
"""