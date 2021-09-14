# Un teatro otorga descuentos según la edad del cliente, determinar la
# cantidad del dinero que el teatro deja de percibir por cada ua de las
# categorias. Tomar en cuenta que los niños menores de 5 años no pueden
# entrar al teatro y que existe un precio único en los asientos. Los descuentos
# se hacen tomando en cuenta el siguiente cuadro:
# Edad % Descuento
# 5 – 14 35%
# 15-19 25%
# 20 – 45 10%
# 46 – 65 25%
# 66 en Adelante 35%

age_5_14 = 0
age_15_19 = 0
age_20_45 = 0
age_46_65 = 0
age_66 = 0
people = 0
# discount = 0
persons = int(input("Por favor, ingrese cuantas personas entraron al teatro: "))
price_chair = float(input("Por favor, ingrese el preio por asientos: $ "))

for i in range(persons):
   
    people += 1
    age = int(input(f"Por favor, ingrese la edad de la persona #{people}:  "))

    if age < 5:
        print("Menor de 5 años, no puede ingresar")
    if age >= 5 and age <= 14:
        age_5_14 = age_5_14 + 1
        count_chair = price_chair * age_5_14 
        discount_a = count_chair * 35 / 100
    elif age >= 15 and age <= 19:
        age_15_19 = age_15_19 + 1
        count_chair = price_chair * age_15_19 
        discount_b = count_chair * 25 / 100
    elif age >= 20 and age <= 45: 
        age_20_45 = age_20_45 + 1
        count_chair = price_chair * age_20_45
        discount_c = count_chair * 10 / 100
    elif age >= 46 and age <= 65: 
        age_46_65 = age_46_65 + 1
        count_chair = price_chair * age_46_65
        discount_d = count_chair * 25 / 100 
    elif age >= 66: 
        age_66 = age_66 + 1
        count_chair = price_chair * age_66
        discount_e = count_chair * 35 / 100
print("/////////////////////////////////////////////////////////////////////")
print(f"El teatro dejo de persibir en la categoria de 5 - 14: ${discount_a} ")
print(f"El teatro dejo de persibir en la categoria de 15 - 19: ${discount_b} ")
print(f"El teatro dejo de persibir en la categoria de 20 - 45: ${discount_c} ")
print(f"El teatro dejo de persibir en la categoria de 46 - 65: ${discount_d} ")
print(f"El teatro dejo de persibir en la categoria de mayor de 66: ${discount_e} ")