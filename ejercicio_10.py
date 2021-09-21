# La empresa Encuestas S.A desea crear una función que les permita
# conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
# el ganador o indicar si hubo empate y la cantidad de votos obtenidos.
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

candidate =("""    ¡¡¡Encuenta!!! 
Elija el candidato de su preferencia

1 - Candidato #1 
2 - Candidato #2
3 - Candidato #3

Elija una de las tres opciones """)
for i in range(50000):
    votes = int(input(candidate))
    if votes == 1:
        candidato_1 += 1
    elif votes == 2:
        candidato_2 += 1
    elif votes == 3:
        candidato_3 += 1
    else:
        print("elija una opcion correcta") 

print(f"El candidato #1 obtuvo {candidato_1} votos") 
print(f"El candidato #2 obtuvo {candidato_2} votos") 
print(f"El candidato #3 obtuvo {candidato_3} votos") 

if candidato_1 > candidato_2 and candidato_1 > candidato_3:
    print(f"El ganador es el: candidato #1 ")
elif candidato_2 > candidato_1 and candidato_2 > candidato_3:
    print(f"El ganador es el: candidato #2 ")
elif candidato_3 > candidato_2 and candidato_3 > candidato_1:
    print(f"El ganador es el: candidato #3 ")
elif candidato_1 == candidato_2 and candidato_1 > candidato_3:
    print(f"Hay un empate entre el candidato #1 y #2 ")
elif candidato_1 == candidato_3 and candidato_1 > candidato_2:
    print(f"Hay un empate entre el candidato #1 y #3 ")
elif candidato_2 == candidato_3 and candidato_2 > candidato_1:
    print(f"Hay un empate entre el candidato #2 y #3 ")

