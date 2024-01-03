# test comment
print("Halo nama saya askar")

print("saya tinggal di jawa barat")

print("umur saya 23 tahun")

# test comment
print("Hello world")

def convert_temperature(degrees, from_unit, to_unit):
    # def celsius_to_fahrenheit(celsius_degrees):
    #     celsius_to_fahrenheit = (celsius_degrees * 9/5) + 32
        
    #     return celsius_to_fahrenheit
    
    def fahrenheit_to_celsius(fahrenheit_degrees):
        fahrenheit_to_celsius = (fahrenheit_degrees - 32) * 5/9

        return fahrenheit_to_celsius
    
    if from_unit == "C" and to_unit == "F":
        return "bbbbb"
    elif from_unit == "F" and to_unit == "C":
        return fahrenheit_to_celsius(degrees)
    else:
        return degrees
    
celsius = 30
fahrenheit = 75

convert_temperature_1 = convert_temperature(celsius,'C','F')
convert_temperature_2 = convert_temperature(fahrenheit,'F','C')

print(f"{celsius} derajat celsius adalah {convert_temperature_1:.2f} derajat fahrenheit")
print(f"{fahrenheit} derajat fahrenheit adalah {convert_temperature_2:.2f} derajat celsius")
