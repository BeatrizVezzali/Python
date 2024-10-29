Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
marcas =  ["Asus", "Dell", "Mac", "HP"]
print(marcas)
['Asus', 'Dell', 'Mac', 'HP']
paises = ["Brasil", "Alemanha", "USA", "Canadá"]
cliente = ["Fulano de tal", "2222-3222", 43]
print(cliente)
['Fulano de tal', '2222-3222', 43]
marcas[0]
'Asus'
marcas[1]
'Dell'
marcas[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    marcas[4]
IndexError: list index out of range
marcas[3]
'HP'
listaNomes = ["João", "Paulo", "Débora"]
print(listaNomes[1])
Paulo
listaNomes.append("Mariana")
print(listaNomes)
['João', 'Paulo', 'Débora', 'Mariana']
print(listaNomes[3])
Mariana
listaNomes.insert(1, "Jacksoprodenílson")
print(listaNomes)
['João', 'Jacksoprodenílson', 'Paulo', 'Débora', 'Mariana']
listaNomes.remove("Jacksoprodenílson")
print(listaNomes)
['João', 'Paulo', 'Débora', 'Mariana']
listaNomes.remove("Débora")
print(listaNomes)
['João', 'Paulo', 'Mariana']
listaNomes.append(none)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    listaNomes.append(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
listaNomes.append('  ')
print(listaNomes)
['João', 'Paulo', 'Mariana', '  ']
len(marcas)
4
print(marcas)
['Asus', 'Dell', 'Mac', 'HP']
print(cliente)
['Fulano de tal', '2222-3222', 43]
type(cliente[0])
<class 'str'>
type(cliente[2])
<class 'int'>
listanomes = ["Jonas", "Cibele", "Marcia"]
print(listanomes)
['Jonas', 'Cibele', 'Marcia']
print(listanomes[0])
Jonas
listanomes.append("William")
print(listanomes)
['Jonas', 'Cibele', 'Marcia', 'William']
listanomes.remove("Cibele")
print(listanomes)
['Jonas', 'Marcia', 'William']
listanomes.insert(1, "Adriana")
print(listanomes)
['Jonas', 'Adriana', 'Marcia', 'William']
listanomes.clear()
print(listanomes)
[]
listanomes.count("Marcia")
0
listanomes = ["Huguinho", "Zezinho", "Luizinho", "Patinhas"]
listanomes.count("Zezinho")
1
numeros = [5, 7, 4, 6, 8, 9, 15, 10]
print(numeros)
[5, 7, 4, 6, 8, 9, 15, 10]
numeros.sort()
print(numeros)
[4, 5, 6, 7, 8, 9, 10, 15]
numeros.reverse()
print(numeros)
[15, 10, 9, 8, 7, 6, 5, 4]
numeros.pop(2)
9
print(numeros)
[15, 10, 8, 7, 6, 5, 4]
listanomes = ["Jonas", "Cibele", "Márcia"]
print(listanomes)
['Jonas', 'Cibele', 'Márcia']
print(listanomes[-1])
Márcia
print(listanomes)
['Jonas', 'Cibele', 'Márcia']
listanomes[1] = "Roberta"
print(listanomes)
['Jonas', 'Roberta', 'Márcia']
listanomes.insert(1, "Adriana")
print(listanomes)
['Jonas', 'Adriana', 'Roberta', 'Márcia']
print(len(listanomes))
4
listanomes.clear()
numerosPares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
numerosPares[4:8]
[10, 12, 14, 16]
numerosPares[:5]
[2, 4, 6, 8, 10]
numerosPares[:10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numerosPares[10:]
[22, 24, 26, 28, 30]
marcas1 = ["Asus", "Dell", "Mac", "HP"]
marcas2 = marcas1
print(marcas2)
['Asus', 'Dell', 'Mac', 'HP']
marcas2[2] = "Positivo"
print(marcas2)
['Asus', 'Dell', 'Positivo', 'HP']
print(marcas1)
['Asus', 'Dell', 'Positivo', 'HP']
marcas1.append("Mac")
print(marcas1)
['Asus', 'Dell', 'Positivo', 'HP', 'Mac']
print(marcas2)
['Asus', 'Dell', 'Positivo', 'HP', 'Mac']
marcas3 = marcas1[:]
prints(marcas3)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    prints(marcas3)
NameError: name 'prints' is not defined. Did you mean: 'print'?
print(marcas3)
['Asus', 'Dell', 'Positivo', 'HP', 'Mac']
marcas1.pop(4)
'Mac'
marcas3.remove("Mac")
print(marcas3)
['Asus', 'Dell', 'Positivo', 'HP']
print(marcas2)
['Asus', 'Dell', 'Positivo', 'HP']
marcas3.pop(1)
'Dell'
print(marcas3)
['Asus', 'Positivo', 'HP']
print(marcas1)
['Asus', 'Dell', 'Positivo', 'HP']
"Mac" in marcas3
False
"Asus" in marcas3
True
nome = ["Saturnino", "Segurola"]
end = ["Parque Chacabuco", 13, "CABA"]
dados = nome + end
print(dados)
['Saturnino', 'Segurola', 'Parque Chacabuco', 13, 'CABA']
comidas = ["Pataniscas", "Bifana", "Rojões", "Prego"]
del comidas[1]
print(comidas)
['Pataniscas', 'Rojões', 'Prego']
del comidas[1:]
print(comidas)
['Pataniscas']
