# Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.

men_ages_accum = 0
women_ages_accum = 0
men_number = int(input("Por favor; ingrese el numero de hombres: "))
women_number = int(input("Por favor; ingrese el numero de mujeres: "))

for i in range(men_number):
    age = int(input(f" ingrese la edad del hombre # {i + 1 }: "))
    men_ages_accum += age

for i in range(women_number):
    age = int(input(f" ingrese la edad de la mujer # {i + 1 }: "))
    women_ages_accum += age

students_age_avg = round((women_ages_accum + men_ages_accum) / (women_number + men_number), 2)

print(f"el promedio de edades de los hombre es: {round(men_ages_accum / men_number, 2)}")
print(f"el promedio de edades de las mujeres es: {round (women_ages_accum / women_number, 2)}")
print(f"el promedio de edades de los alumnos es: {students_age_avg}")