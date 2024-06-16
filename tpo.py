import random

# Definición de los precios y costos por tipo de evento
casamiento=0
casamiento_fijo = 750000
casamiento_ad_50 = 6500
casamiento_ad_100 = 6000
casamiento_costo = 160000

quince=0
quince_fijo = 850000
quince_ad_50 = 7500
quince_ad_100 = 8000
quince_costo = 180000

cumpleaños=0
cumpleaños_fijo = 650000
cumpleaños_ad_50 = 5500
cumpleaños_ad_100 = 6000
cumpleaños_costo = 160000

bautismo=0
bautismo_fijo = 750000
bautismo_ad_50 = 6500
bautismo_ad_100 = 7000
bautismo_costo = 170000

otros=0
otros_fijo = 800000
otros_ad_50 = 7000
otros_ad_100 = 8000
otros_costo = 180000

# Inicialización de contadores y acumuladores
total_fac_casamiento = 0
total_fac_quince = 0
total_fac_bautismo = 0
total_fac_cumpleaños = 0
total_fac_otros = 0

total_costo_casamiento = 0
total_costo_quince = 0
total_costo_bautismo = 0
total_costo_cumpleaños = 0
total_costo_otros = 0

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n---- MENÚ ----")
    print("1. Total de facturación del mes")
    print("2. Total de facturación por tipo de evento")
    print("3. Listado completo detallado del total facturado de cada evento")
    print("4. Detalles de facturación por tipo de evento")
    print("5. Salir")

# Función para generar eventos aleatorios
def generar_eventos():
    eventos = ["casamiento", "quince", "cumpleaños", "bautismo", "otros"]
    cantidad_eventos = random.randint(10, 30)
    datos_generados = []

    for _ in range(cantidad_eventos):
        evento = random.choice(eventos)
        cant_invitados = random.randint(50, 200)
        datos_generados.append((evento, cant_invitados))

    return datos_generados

# Calcular la facturación y costos de los eventos generados
def calcular_facturacion(eventos):
    global total_fac_casamiento, total_fac_quince, total_fac_bautismo, total_fac_cumpleaños, total_fac_otros
    global total_costo_casamiento, total_costo_quince, total_costo_bautismo, total_costo_cumpleaños, total_costo_otros

    for evento, cant_invitados in eventos:
        if evento == "casamiento":

            total_costo_casamiento += casamiento_costo
            if cant_invitados <= 50:
                total_fac_casamiento += casamiento_fijo
            elif cant_invitados <= 100:
                total_fac_casamiento += casamiento_fijo + (cant_invitados - 50) * casamiento_ad_50
            else:
                total_fac_casamiento += casamiento_fijo + (cant_invitados - 100) * casamiento_ad_100

        elif evento == "quince":

            total_costo_quince += quince_costo
            if cant_invitados <= 50:
                total_fac_quince += quince_fijo
            elif cant_invitados <= 100:
                total_fac_quince += quince_fijo + (cant_invitados - 50) * quince_ad_50
            else:
                total_fac_quince += quince_fijo + (cant_invitados - 100) * quince_ad_100

        elif evento == "cumpleaños":

            total_costo_cumpleaños += cumpleaños_costo

            if cant_invitados <= 50:
                total_fac_cumpleaños += cumpleaños_fijo
            elif cant_invitados <= 100:
                total_fac_cumpleaños += cumpleaños_fijo + (cant_invitados - 50) * cumpleaños_ad_50
            else:
                total_fac_cumpleaños += cumpleaños_fijo + (cant_invitados - 100) * cumpleaños_ad_100

        elif evento == "bautismo":

            total_costo_bautismo += bautismo_costo
            if cant_invitados <= 50:
                total_fac_bautismo += bautismo_fijo
            elif cant_invitados <= 100:
                total_fac_bautismo += bautismo_fijo + (cant_invitados - 50) * bautismo_ad_50
            else:
                total_fac_bautismo += bautismo_fijo + (cant_invitados - 100) * bautismo_ad_100

        elif evento == "otros":

            total_costo_otros += otros_costo
            if cant_invitados <= 50:
                total_fac_otros += otros_fijo
            elif cant_invitados <= 100:
                total_fac_otros += otros_fijo + (cant_invitados - 50) * otros_ad_50
            else:
                total_fac_otros += otros_fijo + (cant_invitados - 100) * otros_ad_100

# Programa principal
eventos_mes = generar_eventos()
calcular_facturacion(eventos_mes)

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        total_facturacion = total_fac_casamiento + total_fac_quince + total_fac_bautismo + total_fac_cumpleaños + total_fac_otros
        print("Total de la facturación del mes:", total_facturacion)
        total_costo=total_costo_casamiento + total_costo_quince + total_costo_bautismo + total_costo_cumpleaños + total_costo_otros
        print("Total del costo del mes:", total_costo)
        cant_eventos=casamiento+bautismo+quince+cumpleaños+otros
        print("Cantidad de eventos:", cant_eventos)
        
    elif opcion == "2":
        print("Facturación por tipo de evento:")
        print("Casamientos:", total_fac_casamiento)
        print("Quinceañeras:", total_fac_quince)
        print("Cumpleaños:", total_fac_cumpleaños)
        print("Bautismos:", total_fac_bautismo)
        print("Otros eventos:", total_fac_otros)

    elif opcion == "3":
        print("Listado completo detallado del total facturado de cada evento:")
        for evento, cant_invitados in eventos_mes:
            print(f"Evento: {evento}, Cantidad de invitados: {cant_invitados}")

    elif opcion == "4":
        print("Detalles de facturación por tipo de evento:")
        print("Casamientos: Facturación =", total_fac_casamiento, ", Costo =", total_costo_casamiento)
        print("Quinceañeras: Facturación =", total_fac_quince, ", Costo =", total_costo_quince)
        print("Cumpleaños: Facturación =", total_fac_cumpleaños, ", Costo =", total_costo_cumpleaños)
        print("Bautismos: Facturación =", total_fac_bautismo, ", Costo =", total_costo_bautismo)
        print("Otros eventos: Facturación =", total_fac_otros, ", Costo =", total_costo_otros)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, intente nuevamente.")
