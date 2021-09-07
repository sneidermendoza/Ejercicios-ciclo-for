# Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si existe diferencia 
# positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso.
weight_accum_member = 0
actual_weight_1 = float(input("Por favor, miembro #1 ingrese su peso actual: "))
actual_weight_2 = float(input("Por favor, miembro #2 ingrese su peso actual: "))
actual_weight_3 = float(input("Por favor, miembro #3 ingrese su peso actual: "))
actual_weight_4 = float(input("Por favor, miembro #4 ingrese su peso actual: "))
actual_weight_5 = float(input("Por favor, miembro #5 ingrese su peso actual: "))
member = 0

for n in range(5):
    member += 1
    for i in range(10):
        weighing_machine = float(input(f"miembro # {member}, el peso de la bascula # {i + 1} es: "))
        weight_accum_member += weighing_machine


print(weighing_machine)
