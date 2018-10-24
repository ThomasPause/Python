#Programm zur Berechnung von Quersummen,
#gewichteten und potenzierten Quersummen,
#sowie Armstrongzahlen

def quer(z):
   liste = list(z)   
   sqnbr = 0
   for digit in liste:
      sqnbr += int(digit)
   return sqnbr


def gewichtetQuer(z):
    liste = list(z)
    liste = liste[::-1]
    gewsq = 0
    gewicht = [1,3,2,-1,-3,-2]
    i = 0
    j = 0
    
    while i < len(liste):
        gewsq += int(liste[i]) * int((gewicht[j%6]))
        i+=1
        j+=1
    return str(gewsq)

        
def potenziertQuer(z):
   liste = list(z)   
   sqnbr = 0
   if int(z) > 0:
      for digit in liste:
         sqnbr += pow(int(digit), len(liste))     
   return sqnbr


def alleArmstrongZahlen(n):
   armst = []
   for i in range(n):
      if int(potenziertQuer(str(i))) == i:
         armst.append(i)
   return armst

zahl = input("Bitte eine nat.Zahl eingeben: ")
print("Die Quersumme von ", zahl, " ist ", quer(zahl))
print("Die gewichtete Quersumme von ", zahl, " ist ", gewichtetQuer(zahl))
print("Die potenzierte Quersumme von ", zahl, " ist ", potenziertQuer(zahl))

number = (int(input("Bitte eine nat.Zahl fuer die Armstrongausgabe eingeben: ")))
print("Alle ArmstrongZahlen bis ", number, " sind:\n", (*alleArmstrongZahlen(number+1)))


