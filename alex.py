from pawn import *

x = Pawn('white',1,3)
print (x)
x.setcolor('black')
print(x)
#x.setcol('blue')

l = "A B c D e f g h 54534fsdf"
liste_lettre_plateau=['a','b','c','d','e','f','g','h','A','B','C','D','E','F','G','H']
n = []
for x in l:
    if x in liste_lettre_plateau:
        n.append(ord(x) - 96)
print(n)