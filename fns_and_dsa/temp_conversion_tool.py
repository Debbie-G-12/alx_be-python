FACTOR = 9/5
OFFSET = 32

def celsius_to_fahrenheit(celsius):
    return (celsius * FACTOR) + OFFSET

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - OFFSET) / FACTOR
