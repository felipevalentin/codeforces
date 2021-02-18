for i in range(int(input())):
    n = int(input())
    a = [0]*3
    ans = 0
    for j in input().split():
        a[int(j)%3] += 1
    for j in range(3):
        ans = max(ans, a[j] - a[j-1])
    print(ans)
# Pense na distancia entre 2 numeros com o uso de um auxiliar
# como 77 e 88 pensando na distancia de 77 a 80 e 80 a 88
# o resultado é a soma 80 - 77 + 88 - 80 = 88 - 77 = 11
# a ideia aqui é pensar que vc só precisa saber quantos tirar da posição atual
# e quantos colocar na posição anteiror ou seja a final teoricamente
# entao se calcularmos da seguinte forma pos[atual] - ponto fixo + ponto fixo - pos[anterior]
# temos que a resposta é pos[atual] - pos[anterior] podemos apenas cortar o ponto fixo
