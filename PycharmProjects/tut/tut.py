# Einfuehrung in Python

# Operatoren: +, -, *, /, %, // (floor division), ** (Exponent)
# Datenstrukturen: List, Set, Dictionary(wie HashMap), immutable List(Type)
# List
liste = []
# gemischte Typen moeglich
# Laenge
print(len(liste))


# Set (Menge)
menge = {1, 3, 'a', "abc"}
# ist Element in Menge?
1 in menge

# immutable List (Tuple) (unveraenderlich)
xyz = (1, 4, 5, 6)

# dictionary: key-value-paare
dictio = {1: 'a', 2: 4, 3: "abc"}
# x in dictionary laesst nur nach keys suchen
# Eintraege hinzufuegen:
dictio[4] = 3.5

#FOR-Schleife
for x in liste:
    print(x)

# range(start, stop, step(optional), praktisch auch fuer for
for x in range(0, 20, 3):
    print(x)

#WHILE-Schleife
x = 0
while x < 10:
    print(x)
    x += 1
# kein ++ oder -- in Python!!!!

# Verzweigungen
if x is 10:
    print("yeah")
# if x == 10: geht auch
else:
    print("not yeah")

# elseif heisst elif

# ich bin ein Kommentar
def fak(n):
    if n == 1:
        return 1
    else:
        return n*fak(n-1)


print(fak(5))


def fun(i):
    return "Hello" if i > 10 else "Goodbye"


def fak2(m):
    return 1 if m == 1 else m*fak2(m-1)


print(fak2(1), fak2(5))


print("fak(5): {0} \nfak(10): {1}".format(fak(5), fak(10)))


# and or not sind die logischen Operatoren
#  die Comprehensions sind das geilste ever

squares = [x**x for x in range(0, 11)]

print(squares)


facool = [fak(y) for y in range(1, 20, 4)]

print(facool)


test = [x**2 for x in range(1, 11) if x % 2 == 0]

print(test)

# slicing (erzeugt Unterlisten z.B.)
# Notation start:stop:step(optional)

subway = [1, 5, 7, 78, "Immanuel", "Chicken Teriyaki"]

print(subway[::2])
print(subway[::-1])
# reversdte liste




