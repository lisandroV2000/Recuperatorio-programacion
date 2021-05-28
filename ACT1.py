#1. Cargue desde la consola los datos de dos personajes de Star Wars (nombre , altura,
#peso, planeta de origen, cantidad de peliculas), y luego resuelva lo siguiente:
#a. cual es el personaje más bajo (indicar el nombre)
#b. cual es el personaje más pesado (indicar el nombre)
#c. cual personaje participó en más películas (si los dos participaron en la misma
#cantidad indicarlo) (indicar el nombre)
#d. determinar si alguno de los personajes aleatorios se llama Yoda o
#Chewbacca





Personaje1 = (input('ingrese el nombre del personaje'))
Altura1 = int(input('ingrese altura del personaje')) 
Pesopers1 = int(input('ingrese el peso del personaje')) 
Planeta1 = (input('ingrese el planeta del personaje')) 
Films1 = int(input('ingrese la peliicula del personaje')) 
 

Personaje2 = (input('ingrese el nombre del personaje'))
Altura2 = int(input('ingrese altura del personaje')) 
Pesopers2 = int(input('ingrese el peso del personaje')) 
Planeta2 = (input('ingrese el planeta del personaje')) 
Films2 = int(input('ingrese la peliicula del personaje'))  


Pj1 = [Personaje1, Altura1, Pesopers1, Planeta1, Films1]
Pj2 = [Personaje2, Altura2, Pesopers2, Planeta2, Films2]

print("Resp 1b") 

if (Pj1[2] > Pj2[2]):
    print(Pj1[0], 'es mas pesado')
elif (Pj1[2]) == Pj2[2]:
    print('pesan lo mismo')
else:
     (Pj2[2], 'es mas pesado')

print("Resp 1c")

if (Pj1[4] > Pj2[4]):
    print(Pj1[0], 'participo en mas pelis')
elif (Pj1[4]) == Pj2[4]:
    print('participaron en las mismas pelis')
else:
    (Pj2[4], 'participo en mas pelis') 

print("Resp 1a")

if (Pj2[1] < Pj1[1]):
    print(Pj2[0], 'es mas bajo')
else:
    (Pj1[1], 'es mas bajo')

print("Resp 1d")

if (Personaje1.lower == 'Chewbacca' or Personaje1.lower == 'Yoda' and Personaje2.lower == 'Yoda' or Personaje2.lower == 'Chewbacca'):
    print(Personaje1 and Personaje2, 'no coiciden los nombres')  
else:
    print(Personaje1 and Personaje2, 'se llaman asi los 2')