#Programm zur Berechnung von Primzahlen nach dem Sieb des Eratosthenes

def sieb(n):
    numberlist = []
    for i in range(n-1):
        if i is 1:
            numberlist.append(0)
        else:
            numberlist.append(i)
    primzahlen = []
    for i in numberlist:
        if numberlist[i] is not 0:
            primzahlen.append(i)
            count = 1
            j = count * i
            while j <= len(numberlist)-1:
                numberlist[j] = 0
                count += 1
                j = i * count
    return primzahlen

print (sieb(42))
print (sieb(1864))
print (sieb(1111))
