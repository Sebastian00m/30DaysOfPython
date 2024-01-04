#Exercises: Level 1
#1_Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#2_Write a python comment saying 'Day 2: 30 Days of python programming'
#3_Declare a first name variable and assign a value to it
first_name='Mauro'
#4_Declare a last name variable and assign a value to it
last_name='Montaño'
#5_Declare a full name variable and assign a value to it
full_name=first_name + last_name
#6_Declare a country variable and assign a value to it
country='Argentina'
#7_Declare a city variable and assign a value to it
city='Buenos Aires'
#8_Declare an age variable and assign a value to it
age=23
#9_Declare a year variable and assign a value to it
year=2024
#10_Declare a variable is_married and assign a value to it
is_married=False
#11_Declare a variable is_true and assign a value to it
is_true=True
#12_Declare a variable is_light_on and assign a value to it
is_light_on=True
#13_Declare multiple variable on one line
University,carrer,aproved_subjects='UNLaM','Ing.Informatica',17

#Ejercicios: Nivel 2
#1)_Verifique el tipo de datos de todas sus variables usando la función incorporada type()
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2)_Usando la función incorporada len() , encuentre la longitud de su nombre
print(len(full_name))
#3)_Compara la longitud de tu nombre y tu apellido
print((len(first_name))==(len(last_name)))
#4)_Declare 5 como num_one y 4 como num_two
num_one = 5
num_two = 4
    #a_Suma num_one y num_two y asigna el valor a una variable total
suma = num_one + num_two
print(suma)
    #b_Reste num_two de num_one y asigne el valor a una variable diff
diff =num_one - num_two
print(diff)
    #c_Multiplica num_two y num_one y asigna el valor a un producto variable
producto = num_one * num_two
print(producto)
    #d_Divide num_one por num_two y asigna el valor a una división variable
division = num_one / num_two
print(division)
    #e_Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
resto = num_two % num_one
print(resto)
    #f_Calcula num_one elevado a num_two y asigna el valor a una variable exp
expo = num_one**num_two
print(expo)
    #g_Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
floor_division = num_one // num_two
print(floor_division)

#5)_El radio de un círculo es de 30 metros.
rad = 30
#Calcula el área de un círculo y asigna el valor a un nombre de variable de area_of_circle
area_of_circle = 3.14*(rad**2)
print(area_of_circle)
#Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle
circum_of_circle = 2*3.14*rad
print(circum_of_circle)
#Tome el radio como entrada del usuario y calcule el área.
rad_in = input('Ingrese el radio deseado ')
area_of_circle_in = 3.14*(rad_in**2)
print(area_of_circle_in)
#6)_Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variables correspondientes.
#nombre_in, apellido_in =input('Ingrese el nombre :', 'Ingrese el apellido:')