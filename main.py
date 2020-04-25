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

 print("----------------------")
 print("a validar: "+email)
 if(email.count("@") > 0):
   dividirString = email.split("@")
  
   if(len(dividirString) > 1):
     if(len(dividirString[0]) > 0):
       username=dividirString[0]

       vectorLetras=["a","b","c","d","e","f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
       vectorEspeciales=["-","_","."]
       vectorNumeros=[0,1,2,3,4,5,6,7,8,9]

       for x in username:
         validaciontotal=0
         #validar caracter con letras
         for y in vectorLetras:
           if(x==y):
             validaciontotal = validaciontotal + 1
         #validar caracter con especiales
         for z in vectorEspeciales:
           if(x==z):
             validaciontotal = validaciontotal + 1
         #validar con numeros
         for w in vectorNumeros:
           if(str(x)==str(w)):
             validaciontotal = validaciontotal + 1

         if(validaciontotal == 0):
           estado=Estados.NOVALIDO

       if(estado==Estados.NOVALIDO):
         estadofinalusername=Estados.NOVALIDO
       else:
         estadofinalusername=Estados.VALIDO

       domain=dividirString[1].split(".") #separa el dominio en sub dominios
    
       validaciontotal=0
       estado=""
       #print(domain)
       lendomain=len(domain)
       lendomain1=len(domain[0])
       lendomain2=len(domain[1])
       #print(lendomain)
      
       if(lendomain > 1 and lendomain1 >0 and lendomain2 >0):
         domainname= domain[0]
         ending = domain[lendomain-1]#esto toque
        
         contadordominios=0
        
         for x in domain:
            lendomi=len(x)
              
            for y in domain[contadordominios]:
                 
              #print("-COMPARAR CON NUMEROS")
              #
              validaciontotal=0
              if(contadordominios == 0):
                
                for w in vectorNumeros:
                  #print(str(y)+":"+str(w))
                  if(str(y)==str(w)):
                    #print(str(y)+" esta dentro de los parametros admitidos!w"+str(w))
                    validaciontotal = validaciontotal + 1
              #
              #print("-COMPARAR CON LETRAS")
              for w in vectorLetras:
                #print(str(y)+":"+str(w))
                if(str(y)==str(w)):
                  #print(str(y)+" esta dentro de los parametros admitidos!w"+str(w))
                  validaciontotal = validaciontotal + 1

            contadordominios=contadordominios + 1  
            
            if(contadordominios < len(domain)):
              validaciontotal = validaciontotal - 1 
            else:

              if(validaciontotal <= 0):
                  #print("CARACTE NO ADMITEDDD!")
                estado=Estados.NOVALIDO
              if(estado==Estados.NOVALIDO):
                if(contadordominios==0):
                    #print("Dominio:"+str(x)+" NO VALIDO!")
                  estadofinaldominio=Estados.NOVALIDO
                else:
                    #print("Ending:"+str(x)+" NO VALIDO!")
                  estado=Estados.NOVALIDO
              else:
                if(contadordominios==0):  
                  estadofinaldominio=Estados.VALIDO
                else:
                  estado=Estados.VALIDO

              if(estadofinaldominio==Estados.NOVALIDO):
                print("EMAIL INVALIDO")
                print("----------------------")
                return Estados.NOVALIDO
              elif(estado==Estados.NOVALIDO):
                print("EMAIL INVALIDO")
                print("----------------------")
                return Estados.NOVALIDO
              elif(estadofinalusername==Estados.NOVALIDO):
                print("EMAIL INVALIDO")
                print("----------------------")
                return Estados.NOVALIDO
              else:
                print("EMAIL VALIDO")
                print("----------------------")
                return Estados.VALIDO

       else:
         print("EMAIL INVALIDO")
         print("----------------------")
         return Estados.NOVALIDO
         

     else:
       print("EMAIL INVALIDO")
       print("----------------------")
       return Estados.NOVALIDO
 else:
   print("EMAIL INVALIDO")
   print("----------------------")
   return Estados.NOVALIDO
   

#########################################################################
lista=['a@a.com', 'b.com', 'c@.com', 'ddcom', 'e@e.com.ar', '´ç@.com.ar', 'asd@123.123', 'qwe@ca.123.']

archivo1=""
archivo1 = open("mails.csv","w")
archivo1.write("mail"+"\n")
archivo1.close()

archivo1 = open("mails.csv","a")
for x in lista:
 archivo1.write(x+"\n")
archivo1.close()
#########################################################################

retorno=""
contadoremails=0

archivo2=""
archivo2 = open("validaciones.txt","w")
archivo2.write("MAILS VALIDADOS"+"\n")
archivo2.close()

archivo=""
archivo = open("mails.csv","r")
leer = csv.DictReader(archivo)
for mail in leer:
  print("\n")
  email=mail['mail']
  retorno=validar(email)
  #print("%%%%%%%%%%%"+str(retorno)+"%%%%%%")
  if(retorno==Estados.VALIDO):
    archivo2 = open("validaciones.txt","a")
    archivo2.write(str(mail['mail'])+" VALIDO!"+"\n")
    archivo2.close()
  else:
    archivo2 = open("validaciones.txt","a")
    archivo2.write(str(mail['mail'])+" (NO) VALIDO!"+"\n")
    archivo2.close()
  contadoremails=contadoremails+1
  #print("contador emails:"+str(contadoremails))