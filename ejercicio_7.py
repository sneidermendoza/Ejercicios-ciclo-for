# En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artóculo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.

articles = int(input("Por favor, ingrese cuantos articulos compro:  "))
number_articles = 0
total = 0
items = 0

for i in range(articles):
    number_articles += 1
    value_artile = float(input(f"valor del articulo # {number_articles}: $"))
    number_items = int(input("numero de articulos: "))
    items += number_items
    value_x_items = value_artile * number_items
    total += value_x_items

print(f"El total de articulos es: {items} unidades, y el toal de la compra es: ${total} ")    


    