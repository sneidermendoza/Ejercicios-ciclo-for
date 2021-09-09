# Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si existe diferencia 
# positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso.


member = 0
number_membes = int(input("Ingrese el numero de miembros a pesar:  "))


for n in range(number_membes):
    weight_accum_member = 0
    member += 1
    actual_weight = float(input(f"Por favor, miembro {member} ingrese su peso actual: "))
    
    for i in range(10):
        weighing_machine = float(input(f"miembro # {member}, el peso de la bascula # {i + 1} es: "))
        weight_accum_member += weighing_machine
    avg = weight_accum_member / 10 

    if avg < actual_weight:
        weight = "BAJO"
    elif avg > actual_weight:
        weight = "SUBIO" 
    else:
        weight = " Su peso es IGUAL"
            
    amount_of_kilos = round(avg - actual_weight , 2) 

    print(f"Miembro # {member}, {weight} {amount_of_kilos} kilos ")