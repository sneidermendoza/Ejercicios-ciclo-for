# Una empresa se requiere calcular el salario semanal de cada uno de los n
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de
# lasprimeras 40 horas y $25 por cada hora extra



number_employee = int(input("Enter number of employees: "))


for i in range(number_employee):
    hours_worked = int(input(f"Please, enter the hours worked of the employee #{i + 1}: ")) 
    if hours_worked <= 40:
        total = hours_worked * 20
    else:
        extra_hours = hours_worked - 40
        total = (40 * 20) + (extra_hours * 25) 
    
    print(f"The weekly salary of the employee {i + 1} is :  {total}")


