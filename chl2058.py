import sys  # Import the sys module to read command-line arguments

def convert(mode, value):  # Define the conversion function taking the mode string and numeric temperature
    if mode == "FtoC":  # Check if the requested conversion is Fahrenheit to Celsius
        return (value - 32) * 5 / 9  # Calculate and return the Celsius value as a float
    elif mode == "CtoF":  # Check if the requested conversion is Celsius to Fahrenheit
        return (value * 9 / 5) + 32  # Calculate and return the Fahrenheit value as a float
    else:  # Catch any unrecognized, missing, or invalid mode strings
        return None  # Return None to signal an invalid conversion mode

if __name__ == "__main__":  # Run the file I/O logic only when executed directly as a script (not imported)
    if len(sys.argv) > 1:  # Check if a command-line argument was supplied after the script filename
        temperatureMode = sys.argv[1]  # Store the first command-line argument as the conversion mode
    else:  # Handle runs where no command-line argument was provided
        temperatureMode = "None"  # Set a fallback string that will safely fail validation in convert()
            
    with open("challenge.data", "r") as rawFile:  # Open the input data file safely in read mode
        contents = rawFile.read().strip()  # Read the entire file and strip surrounding whitespace/newlines
        contentsValue = float(contents)  # Convert the cleaned text string into a floating-point number

    result = convert(temperatureMode, contentsValue)  # Call convert() with the CLI mode and parsed float value

    if result is not None:  # Only write to disk if convert() returned a valid calculation (protects prior output)
        with open("challenge.out", "w") as outputFile:  # Open the output file in write mode
            outputFile.write(str(result))  # Convert the float result to a string and write it to the output file