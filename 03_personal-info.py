first_name = input("Nombre: ")
last_name = input("Apellidos: ")
location = input("Ciudad: ")
try:
  age = int(input("Edad: "))
except:
  age = "unknown"
space = " "
print(f"Hi {first_name} {last_name}! Your location is {location} and you are {age} years old")
