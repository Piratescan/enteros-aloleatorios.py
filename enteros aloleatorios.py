
#import random
#print(random.randint(0,10))

print("Juegos de adivinar, tienes 7 intentos ")

import random
m=random.randint(1,10)
print("adivina el numero del 1 al 10")

for i in range(0,7):
    y=int(input("Segun tu el numero es:"))
    if m==y:
        break

if m==y : 
    print("tu numero es correcto")
else :
    print("tu numero es incorrecto")