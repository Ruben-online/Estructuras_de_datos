# Devolver los índices o posiciones de la lista que sumados den como resultado el valor fuera
# de la lista

class Resultado:
    def sumar_elementos(self,numeros,suma):
        diccionario={}

        for indice, numero in enumerate(numeros):
            diferencia=suma-numero

            if diferencia in diccionario:
                print([diccionario[diferencia],indice])

            diccionario[numero]=indice
        return

s=Resultado()
s.sumar_elementos([1,2,3,2,5,7,2],3)