def burbuja(lista):

    bandera=False

    while bandera==False:
        bandera=True
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                valor = lista[i]
                lista[i] = lista[i+1]
                lista[i+1]=valor
                bandera = False
    print(lista)


burbuja([10,9,8,7,6,5,4,3,2,1])