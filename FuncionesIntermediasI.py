x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Funcion para cambiar el valor de 10 a 15

x[1][0] = 15
print(x)

# Funcion para cambiar el Jordan a Bryant en el diccionario

estudiantes[0]['last_name'] = "Bryant"
print(estudiantes)

# Funcion para cambiar el nombre de Messi a Andres

directorio_deportes['fútbol'][0] = 'Andres'
print( directorio_deportes['fútbol'])

# Funcion para cambiar 20 a 30

z[0]['y'] = 30
print(z)