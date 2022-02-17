import random

nombres = ['Juan', 'Pedro', 'Jhon', 'Steven', 'Jackson', 'Jesus', 'Justin', 'Arturo', 'Claudia', 'Eddie', 'Eduardo', 'Luis', 'Gustavo', 'Joel', 'Alejandro', 'Jairo']
apellidos = ['Gonzalez', 'Rodriguez', 'Suarez', 'Salazar', 'Salgado', 'Miller', 'Villa']
correos = ['gmail.com', 'hotmail.com', 'outlook.com', 'live.com']


nombre = random.choice(nombres)
apellido = random.choice(apellidos)
email = str.lower(nombre) + str.lower(apellido) + str(random.randint(1, 100))
dominio = random.choice(correos)
telefono = str(950) + str(random.randint(0000000,9999999))

print(nombre + ' ' + apellido)
print(email)
print(telefono)
