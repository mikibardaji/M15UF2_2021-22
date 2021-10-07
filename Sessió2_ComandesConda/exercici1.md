*Exercici* Crear un nou diccionari on les claus del primer siguin els valors del segon i els valors, passin a ser les claus.


```python
# Solution "for" 1

dict_reverse = {}

for key, value in d.items():
    name = key
    tel  = value
    dict_reverse[tel] = name
dict_reverse
```

Una segona solució, seria... 

```python
#Solution 2 items() example
d.items()
dict_reverse2 = {}
for key, item in d.items():
    dict_reverse2[item] = key
    print(key, item)
dict_reverse2
```
```python
#Solution 3 with only keys
# keys() example

dict_reverse3 = {}
for key in d.keys():
    tel = d[key]
    dict_reverse2[tel] = key
dict_reverse3
```
