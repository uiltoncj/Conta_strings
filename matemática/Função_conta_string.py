def contar_caracteres(s):
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem+= 1
        else:
            print('{}: {}'.format(caracter_anterior,contagem))
            caracter_anterior = caracter
            contagem = 1
    print('{}: {}'.format(caracter_anterior, caracter))

if __name__=='__main__':
    contar_caracteres('uilton')

