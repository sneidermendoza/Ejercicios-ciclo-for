# Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
# siguiente tabla:
# Valor vendido              Comisión
# Menor o igual que 20
# Millones
#                               10%
# Mayor de 20 Millones y
# menor de 40 Millones
#                               15%
# Mayor o igual de 40          
# Millones y menor de 80
# Millones
#                               20%
# Mayor o igual de 80
# millones y menor de
# 160 Millones
# 25%
# De 160 Millones en
# adelante
#                                30%
# Realice un método que diga cuanto vendió y la comisión de los 100
# vendedores que tiene la empresa.


print("              !!!Programa de comisiones!!!!")
for i in range(5):
    sales = float(input(f"Por favor, ingrese las ventas del vendedor #{i + 1}: $"))
    if sales <= 20000000:
        commission = sales * 10 / 100
        print(f"Por su ezfuerso de vender ${sales}, su comision es de: ${commission}")
    elif sales > 20000000 and sales < 40000000:
        commission = sales * 15 / 100
        print(f"Por su ezfuerso de vender ${sales}, su comision es de: ${commission}")
    elif sales >= 40000000 and sales < 80000000:
        commission = sales * 20 / 100
        print(f"Por su ezfuerso de vender ${sales}, su comision es de: ${commission}")
    elif sales >= 80000000 and sales < 160000000:
        commission = sales * 25 / 100
        print(f"Por su ezfuerso de vender ${sales}, su comision es de: ${commission}")
    else:
        commission = sales * 30 / 100
        print(f"Por su ezfuerso de vender ${sales}, su comision es de: ${commission}")
