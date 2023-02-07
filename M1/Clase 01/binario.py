def binario(num: int) -> int:
    lista_restos = []
    while (num // 2):
        lista_restos.append(str(num % 2))
        num //= 2
    if num == 1:
        lista_restos.append(str(num))
    lista_restos.reverse()
    res = int("".join(lista_restos))
    return res


num = 153
num_bin = binario(num)
print(num_bin)
