# Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará 40

animals_number = 0
category_one_count = 0
category_two_count = 0
category_three_count = 0

animal = input("Por favor ingrese que animal quiere estudiar, (elefantes, jirafas, chimpances): ")

if animal == "elefantes":
    animals_number = 20
elif animal == "jirafas":
    animals_number = 15
elif animal == "chimpances":
    animals_number = 40 
else:
    print("!!Solo puedes elegir entre elefantes, jirafas o chimpaces!!")

for i in range(animals_number):
    edad = float(input(f"Ingrese la edad del animal {i + 1}:  "))
    if edad > 0 and edad <= 1:
        category_one_count += 1
    elif edad > 1 and edad < 3:
        category_two_count += 1
    elif edad >= 3:
        category_three_count += 1
    else:
        print("Ingrese un numero positivo")  

category_one_percentage = (category_one_count / animals_number) * 100
category_two_percentage = (category_two_count / animals_number) * 100
category_three_percentage = (category_three_count / animals_number) * 100

print(f"porcentaje de {animal} en la categoria 1 es: {category_one_percentage}% ")
print(f"porcentaje de {animal} en la categoria 2 es: {category_two_percentage}% ")
print(f"porcentaje de {animal} en la categoria 3 es: {category_three_percentage}% ")
