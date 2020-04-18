import csv
from enum import Enum

class Estados(Enum):
 VALIDO = 1
 NOVALIDO = 0

def validar(email):

 dividirString=[]
 vectorLetras=[]
 vectorNumeros=[]
 vectorEspeciales=[]
 validaciontotal=0
 estado=""
 estadofinaldominio=""
 estadofinalusername=""

 print("a validar: "+email)
 if(email.count("@") > 0):
   print("primer validacion: "+str(email.count("@")))
   dividirString = email.split("@")

   print(len(dividirString))
   if(len(dividirString) > 1):
     print(len(dividirString[0]))
     if(len(dividirString[0]) > 0):
       print("TIENE USER NAME VALIDO")

       username=dividirString[0]
    
       vectorLetras=["a","b","c","d","e","f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
       vectorEspeciales=["-","_","."]
       vectorNumeros=[0,1,2,3,4,5,6,7,8,9]

       #recorrer primer sub string(username[0])
       for x in username:
         validaciontotal=0
         #validar caracter con letras
         for y in vectorLetras:
           if(x==y):
             print(x+" esta dentro de los parametros admitidos!y"+y)
             validaciontotal = validaciontotal + 1
         #validar caracter con especiales
         for z in vectorEspeciales:
           print(str(x)+"-"+str(z))
           if(x==z):
             print(x+" esta dentro de los parametros admitidos!z"+z)
             validaciontotal = validaciontotal + 1
         #validar con numeros
         for w in vectorNumeros:
           #print(str(x)+":"+str(w))
           if(str(x)==str(w)):
             print(str(x)+" esta dentro de los parametros admitidos!w"+str(w))
             validaciontotal = validaciontotal + 1

         print("PUNTAJE:"+str(validaciontotal))
         if(validaciontotal == 0):
           print("CARACTE NO ADMITEDDD!")
           estado=Estados.NOVALIDO

       if(estado==Estados.NOVALIDO):
         print("USERNAME NO VALIDO")
         estadofinalusername=Estados.NOVALIDO
       else:
         print("USERNAME VALIDO !!!!!!!!!!!!!!!!")
         estadofinalusername=Estados.VALIDO

       print("----------------------------------------")
       print("------VALIDAR DOMINIO y ENDING----------")
       print("----------------------------------------")

       domain=dividirString[1].split(".") #separa el dominio en sub dominios
      
       print(dividirString)

       validaciontotal=0
       estado=""
       print(domain)
       lendomain=len(domain)
       print(lendomain)
      
       if(lendomain > 1):
         domainname= domain[0]
         ending = domain[1]
         print(domainname+"/"+ending)
         print(str(lendomain-1)+" ENDING,CONTINUAR!")
         contadordominios=0
         print(contadordominios)
         for x in domain:
           #
           print("COMPARAR CARACTERES DE :"+x)
           for y in domain[contadordominios]:
             validaciontotal=0        
             print("-COMPARAR CON NUMEROS")
             #
             if(contadordominios == 0):
               print("solo al dominio compararle numeros!")
               for w in vectorNumeros:
                 #print(str(y)+":"+str(w))
                 if(str(y)==str(w)):
                   print(str(y)+" esta dentro de los parametros admitidos!w"+str(w))
                   validaciontotal = validaciontotal + 1
             #
             print("-COMPARAR CON LETRAS")
             for w in vectorLetras:
               #print(str(y)+":"+str(w))
               if(str(y)==str(w)):
                 print(str(y)+" esta dentro de los parametros admitidos!w"+str(w))
                 validaciontotal = validaciontotal + 1
                  
             print("PUNTAJE:"+str(validaciontotal))
             if(validaciontotal == 0):
               print("CARACTE NO ADMITEDDD!")
               estado=Estados.NOVALIDO

           if(estado==Estados.NOVALIDO):
             if(contadordominios==0):
               print("Dominio:"+str(x)+" NO VALIDO!")
               estadofinaldominio=Estados.NOVALIDO
             else:
               print("Ending:"+str(x)+" NO VALIDO!")
               estado=Estados.NOVALIDO
           else:
             if(contadordominios==0):
               print("Dominio:"+str(x)+" VALIDO!")
               estadofinaldominio=Estados.VALIDO
             else:
               print("Ending:"+str(x)+" VALIDO!")
               estado=Estados.VALIDO
           contadordominios=contadordominios + 1
           print(str(contadordominios))

           if(estadofinaldominio==Estados.NOVALIDO):
             print("EMAIL INVALIDO")
             archivo2 = open("validaciones.txt","a")
             archivo2.write(str(mail['mail'])+" INVALIDO!"+"\n")
             archivo2.close()
           elif(estado==Estados.NOVALIDO):
             print("EMAIL INVALIDO")
             archivo2 = open("validaciones.txt","a")
             archivo2.write(str(mail['mail'])+" INVALIDO!"+"\n")
             archivo2.close()
           elif(estadofinalusername==Estados.NOVALIDO):
             print("EMAIL INVALIDO")
             archivo2 = open("validaciones.txt","a")
             archivo2.write(str(mail['mail'])+" INVALIDO!"+"\n")
             archivo2.close()
           else:
             print("EMAIL VALIDO")
             archivo2 = open("validaciones.txt","a")
             archivo2.write(str(mail['mail'])+" VALIDO!"+"\n")
             archivo2.close()

       else:
         print("no tiene ending,MAIL INVALIDO!")

     else:
       print("user name invalido, caracteres:"+str(len(dividirString[0])))

 else:
   print("no tiene @ !")


lista=['a@a.com', 'b.com', 'c@.com', 'ddcom', 'e@e.com.ar', '´ç@.com.ar', 'asd@123.123.', 'qwe@ca.123']

archivo1=""
archivo1 = open("mails.csv","w")
archivo1.write("mail"+"\n")
archivo1.close()

archivo1 = open("mails.csv","a")
for x in lista:
 archivo1.write(x+"\n")
archivo1.close()

print("--------------------------------")
archivo2=""
archivo2 = open("validaciones.txt","w")
archivo2.write("MAILS VALIDADOS"+"\n")
archivo2.close()

archivo=""
archivo = open("mails.csv","r")
leer = csv.DictReader(archivo)
for mail in leer:
  print("\n")
  print(mail['mail'])
    #meter todo el codigo aca adentro para recorrer todos los mails del archivo
  inpute = input()
  email=mail['mail']
  validar(email)