# a = "água"
# remover = "g"
# for l in a:
#     if l == remover:
#         a = a.replace(l," ")
# print(a)
#
# # for l in palavra:
# #     if l == letra:
# #         palavra = palavra.replace(l, " ")

palavra = "arabia"
letras_usadas = " a b c r"
nivel_atual = [letra if letra in letras_usadas else '_' for letra in palavra]
str_nivel_atual = " ".join(nivel_atual)

print(str_nivel_atual)


# _ _ _ _
