from src.bingo import carton


#comentario auxiliar 2 para probar el merge


#Ejercicio 1 y 2 de la tarea 1
def test_prac1_eje1y2():
    mi_carton = carton()
    contador = 27
    for fila in mi_carton:
        for celda in fila:
            if celda==0:
                contador=contador-1

    assert contador == 15

#Ejercicio 3 de la tarea 1
def test_prac1_eje3():
    mi_carton = carton()
    contador = 0
    for contador in range(9):
        assert (mi_carton[0][contador] + mi_carton[1][contador] + mi_carton[2][contador]) >= 1