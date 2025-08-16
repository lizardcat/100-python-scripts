temp = float(input("Please enter your celsius temperature: "))

def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

result = celsius_to_fahrenheit(temp)
print(f"Your temperature in Fahrenheit is: {result}°F")