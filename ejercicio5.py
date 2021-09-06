# Encontrar el menor valor de un conjunto de n números dados

set_number = int(input("Por favor ingrese cuantos numeros hay en su conjunto  de numeros: "))
minor_number = int(input("ingrese el primer # 1:  "))

for i in range(set_number -1):
    number = int(input(f"ingrese el # {i + 2}: "))
    if number < minor_number:
        minor_number = number  


print(f"Dentro del conjunto de numeros, el menor # es :{minor_number}") 

# set_number = int(input("Por favor ingrese cuantos numeros hay en su conjunto  de numeros: "))
# minor_number = 100000000000

# for i in range(set_number):
#     number = float(input(f"ingrese el # {i + 1}: "))
#     if number < minor_number:
#         minor_number = number
      
# print(f"Dentro del conjunto de numeros, el menor # es :{minor_number}")