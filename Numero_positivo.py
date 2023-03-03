#NUMERO_POSITIVO
#Verificar si un numero es positivo y de 4 digitos
print("----------------------------")
print("---NUMERO POSITIVO Y DE 4 CIFRAS---")
print("----------------------------------")

#inpput
n=int(input("Digite el numero: "))

#procesing
if(n>1000 and n<10000)or( n<-1000 and n>-10000):
   Sol="Es de 4 Digitos"
else:
   Sol="No es de 4 digitos" 

if(n==0):
   Rta="Nulo"
else:
    if(n>0):
        Rta="Positivo"
    else:
     Rta="No es positivo"   
     
#ouput
print("-----------------------------")
print("El numero: " +str(Sol))
print("El numero: " +str(Rta))