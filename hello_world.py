var = 'mundo'
num = 1234
num2 = 5678

flotante = 123.4
flotante2 = 456.3
carac = 'c'
carac2 ='d'

bol = True
bol2 = False
bol3 = None

print (var)
print (num + num2)
print (var + carac)

print (num + num2)
print (flotante + flotante2)

print(not bol)
print (not bol2)
print (bol or bol2)
print (bol and bol2)


if 10 > 5:
    print ('10 es mayor que 5')
elif 10 < 5:
    print ('Eso es imposible viejo')

if bol:
    print ('Usamos la variable bol')

# Forma mala de programar (siempre va a ser verdadero)
if True:
    print ('Es verdadero')

if not False:
    print ('La negacion de falso')

var_rapida = 0

while bol != bol2:
    if var_rapida > 10:
        bol = False
    print(var_rapida)
    var_rapida += 2

var_par = 0

for i in range(2,101): 
    if i%2==0: 
       print(i)

if type(var_rapida) is int:
    print ('Es un entero')

if type(flotante) is str:
    print ('Es una cadena')

if type(flotante) is float:
    print ('Es una flotante')

if type(var_rapida) is int:
    print ('Es un entero')

arreglo_num = [0, 1, 2, 3]
arreglo_car = ['c', 'h', 'a', 'r']

print(arreglo_car[0])
print(arreglo_car[1])
print(arreglo_car[3])
print(len(arreglo_car))
print(arreglo_car[len(arreglo_car)-1])

for cualquiernombredevariable in arreglo_num:
    print(cualquiernombredevariable)

for x in range(5):
    print(var[x])

for x in var:
    print(x)

print(10%3)

for k in range (1, 100, 2):
    print (k)