""""
import sys

def convertTemperature(mode, value):  #function
    if mode == "FtoC":
        return (value - 32) * 5 / 9
    elif mode == "CtoF":
        return (value * 9 / 5) + 32
    else:
        return None

if len(sys.argv) > 1:  #this is the check
    temperatureMode = sys.argv[1]  # get argument

with open("challenge.data", "r") as rawFile:
    contents = rawFile.read().strip()
    contentsValue = float(contents)

result = convertTemperature(temperatureMode, contentsValue) #this is the call

with open("challenge.out", "w") as outputFile:
    outputFile.write(str(result))
"""

import sys  # Import sys so the script can read command-line arguments from sys.argv.


def convert(mode, value):  # Define a function that takes a conversion mode and a numeric temperature.
    if mode == "FtoC":  # Check whether the requested conversion is Fahrenheit to Celsius.
        return (value - 32) * 5 / 9  # Subtract 32, multiply by 5/9, and return the Celsius temperature.
    elif mode == "CtoF":  # If the first condition was false, check for Celsius to Fahrenheit.
        return (value * 9 / 5) + 32  # Multiply by 9/5, add 32, and return the Fahrenheit temperature.
    else:  # Run this block when neither conversion mode matches.
        return None  # Return None to indicate that the supplied mode is invalid.


if len(sys.argv) > 1:  # Check whether sys.argv contains the script name and at least one extra argument.
    temperatureMode = sys.argv[1]  # Store the first argument after the script name as the conversion mode.
    print (f"temperatureMode: {temperatureMode}")
else: 
    temperatureMode = "None"
    print (f"temperatureMode: {temperatureMode}")
        
with open("challenge.data", "r") as rawFile:  # Open the input file for reading and close it when this block ends.
    contents = rawFile.read().strip()  # Read the file as text and remove whitespace from both ends.
    contentsValue = float(contents)  # Convert the text to a number that can have a decimal part.
print (f"Chanllenge data: {contentsValue}")
result = convert(temperatureMode, contentsValue)  # Call the function with the mode and temperature, then store its return value.

with open("challenge.out", "w") as outputFile:  # Open the output file for writing, replacing any existing contents.
    outputFile.write(str(result))  # Convert the result to text and write it to the file
    print (f"Challenge out: {result}")


"""
import sys


def convertTemperature(inputMode, value):
    if inputMode == "FtoC":
        return (value - 32) * 5 / 9
    elif inputMode == "CtoF":
        return (value * 9 / 5) + 32
    return None


try:
    temperatureMode = sys.argv[1]
except IndexError:
    pass
else:
    print (f"argument: {sys.argv[1]}")
    with open("challenge.data", "r") as rawFile:
        contentsValue = float(rawFile.read().strip())
    print (f"value: {contentsValue}")
    result = convertTemperature(temperatureMode, contentsValue)
    print (f"result: {result}")
    with open("challenge.out", "w") as outputFile:
        outputFile.write(f"{result}")

"""


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