

#  -----------------------------------
def verify(magic_square) -> bool:
    #  verify lines -------------------
    for i in range(4):
        cont = 0
        for j in range(4):
            cont += magic_square[i][j]
            j += 1
        if cont != 34:
            return False
        i += 1
    #  --------------------------------

    # verify columns ------------------
    for i in range(4):
        cont = 0
        for j in range(4):
            cont += magic_square[j][i]
            j += 1
        if cont != 34:
            return False
        i += 1
    #  --------------------------------
    #  verify primary diagonal --------
    cont = 0
    for i in range(4):
        cont += magic_square[i][i]
    if cont != 34:
        return False
    #  --------------------------------
    #  verify secundary diagonal ------
    cont = 0
    for i in range(4):
        j = 3-i
        cont = magic_square[i][j]
    if cont != 34:
        return False
    #  --------------------------------
    return True


# -----------------------------------------------------------------------------
magic_square = []
for i in range(4):
    magic_square.append([0]*4)

#  initial square --------------------
cont = 0
for i in range(4):
    for j in range(4):
        cont += 1
        magic_square[i][j] = cont
        j += 1
    i += 1
#  -----------------------------------
"""Após o preenchimento inicial teremos uma matriz ordenada de 1 a 16 é necessário então testar cada combinação possivel
 com a função verify para que seja garantido que todos os possiveis quadrados magicos serão gerados. Basicamente iriamos
 gerar todas as possiveis matrizes e verificar uma por uma se são um quadrado magico. Por limitação de tempo tal 
 programa provavelmente nunca seria executado, porém é uma forma de obter todos os possiveis resultados. Além disso por
 uma questão de incompetencia técnica aliada a falta de tempo o codigo para a criação de todas as combinações possiveis 
 nao foi concluido, no entanto, caso fosse, seria necessário a chamada da função verify após a geração de cada resultado
 """
