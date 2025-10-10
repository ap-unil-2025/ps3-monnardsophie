def celsius_to_fahrenheit(celsius):
    fahrenheit = (float(celsius)*9/5)+32

    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (float(fahrenheit)-32)*5/9
    return celsius

def temperature_converter():
    temperature = float(input("Temperature"))
    unit = input("unit (C or F)")
    if unit == "C":
        print(celsius_to_fahrenheit(temperature))
    else :
        print(fahrenheit_to_celsius(temperature))

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()