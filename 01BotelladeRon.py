#Se genera una lista de 100 elementos, se invierte el orden con reverse y se elimina el 0, 
# con el objetivo de recorrer la lista y llegar "0 bottles of beer on the wall.
lista = range(100)
lista.reverse()
lista.pop()
#print lista

print "                              Song Bottle of Beer.\n"
for Elemento in lista :
    print "          ", Elemento, "bottles of beer on the wall,", Elemento, "bottles of beer."
    print "          ", "Take one down, pass it around,", Elemento-1, "bottles of beer on the wall."
print "\n                              End of song" 
