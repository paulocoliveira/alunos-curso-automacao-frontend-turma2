# criar lista
lista = [1, 2, 3, 4]
print(lista)

# adicionar elemento na lista
lista.append(5)
print(lista)

# remover o último elemento da lista
lista.pop()
print(lista)

# remover item da lista
lista.remove(2)
print(lista)

# reverter a ordem dos itens da lista
lista.reverse()
print(lista)

# adicionar mais itens na lista
lista.extend([2, 5, 0, 3])
print(lista)

# ordenar os itens na lista
lista.sort()
print(lista)

# acessar item
print(lista[2])
print(lista[5])

# contar itens
quantidade = lista.count(3)
print(quantidade)

# pegar o tamanho da lista
tamanho = len(lista)
print(tamanho)

# pesquisar na lista
if 8 in lista:
    print("número está na lista")
else:
    print("número não está na lista")


# remover item da lista por índice
lista.remove(lista[2])
print(lista)