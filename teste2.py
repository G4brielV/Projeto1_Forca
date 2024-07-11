a = "agua"
lista = [l for l in a]
remover = "g"
if remover in lista:
    n = lista.count(remover)
    for _ in range(0,n):
        lista.remove(remover)
print(lista)