# El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:


cars_number = int(input("Please, enter the number of cars: "))
yellow_count = 0
pink_count = 0
red_count = 0
green_count = 0
blue_count = 0


for i in range(cars_number):
    plate  = input(f"Please, enter the plate {i + 1}: ")
    plate_last_digit = int(plate[-1])
    if plate_last_digit == 1 or plate_last_digit == 2:
        yellow_count = yellow_count + 1
    elif plate_last_digit == 3 or plate_last_digit == 4:
        pink_count = pink_count + 1
    elif plate_last_digit == 5 or plate_last_digit == 6:
        red_count = red_count + 1
    elif plate_last_digit == 7 or plate_last_digit == 8:
        green_count = green_count + 1
    elif plate_last_digit == 9 or plate_last_digit == 0:
        blue_count = blue_count + 1
    else:
        print("Ingresaste dato incorrecto")

print(f"Con calcomania amarilla hay: {yellow_count}")
print(f"Con calcomania rosada hay: {pink_count}")
print(f"Con calcomania roja hay:  {red_count}")
print(f"Con calcomania verde hay: {green_count}")
print(f"con calcomania azul hay:  {blue_count}")