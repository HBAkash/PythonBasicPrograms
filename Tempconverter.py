#. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
# Take the Celsius temperature as input from the user.

def CeltoFar(celcius):
    farenheit = (celcius * (9/5)) + 32
    print(f"The {celcius} degree celcius is {farenheit:.2f} degree farenheit")
CeltoFar(36)
CeltoFar(-41.8)
