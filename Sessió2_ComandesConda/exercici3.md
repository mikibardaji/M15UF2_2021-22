***Exercici 3*** Construir la llista de tuples amb un bucle while

i = [0,1,2,3,4,5,6,7]
l = ["a","b","c","d","e","f","g","h"]

#Construir la llista de tuples amb un bucle while
count=0
length = len(l)
array_out = []

while (count < length):
    index = i[count]
    elem = l[count]
    t = (index,elem)
    array_out.append(t)
    count += 1
    
array_out
