import random

# Definición de los precios y costos por tipo de evento

casamiento=0
casamiento_fijo=750000
casamineto_ad_50=6500
casamineto_ad_100=6000
casamiento_costo=160000

quince=0
quince_fijo=850000
quince_ad_50=7500
quince_ad_100=8000
quince_costo=180000

cumpleaños=0
cumpleaños_fijo=650000
cumpleaños_ad_50=5500
cumpleaños_ad_100=6000
cumpleaños_costo=160000

bautismo=0
bautismo_fijo=750000
bautismo_ad_50=6500
bautismo_ad_100=7000
bautismo_costo=170000

otros=0
otros_fijo=800000
otros_ad_50=7000
otros_ad_100=8000
otros_costo=180000







evento=[ casamiento, quince, cumpleaños, bautismo, otros  ]

cant_invitados=0


# Función para mostrar el menú principal
def mostrar_menu():
    print("\n---- MENÚ ----")
    print("1. Total de facturación del mes")
    print("2. Total de facturación por tipo de evento")
    print("3. Listado completo detallado del total facturado de cada evento")
    print("4. Detalles de facturación por tipo de evento")
    print("5. Salir")





total_facturacion = 0
total_costo= 0
total_fac_casamiento=0
total_fac_quince=0
total_fac_bautismo=0
total_fac_cumpleaños=0
total_fac_otros=0



def generar_eventos():
    eventos = ["casamiento", "quince", "cumpleaños", "bautismo", "otros"]
    cantidad_eventos = random.randint(10, 30)
    datos_generados = []

    for _ in range(cantidad_eventos):
        evento = random.choice(eventos)
        cant_invitados = random.randint(50, 200)
        datos_generados.append((evento, cant_invitados))


    return datos_generados
#Calcular la facturacion:

cant_invitados_casamiento=0
if evento == casamiento:
    cant_invitados_casamiento+= cant_invitados
    quince +=1

    if cant_invitados > 50 :
        total_fac_casamiento+=casamiento_fijo

    elif cant_invitados < 50 and cant_invitados < 100:
        invitados_extras= cant_invitados - 50
        total_fac_casamiento= casamiento_fijo + (invitados_extras * casamineto_ad_50)

    elif cant_invitados < 100 :
        invitados_extras= cant_invitados - 50
        total_fac_casamiento= casamiento_fijo + (invitados_extras * casamineto_ad_100)


cant_invitados_quince=0
if evento == quince:
    cant_invitados_quince+= cant_invitados
    quince +=1

    if cant_invitados > 50 :
        total_fac_quince+=quince_fijo

    elif cant_invitados < 50 and cant_invitados < 100:
        invitados_extras= cant_invitados - 50
        total_fac_quince= quince_fijo+ (invitados_extras * quince_ad_50)

    elif cant_invitados < 100 :
        invitados_extras= cant_invitados - 50
        total_fac_quince= quince_fijo + (invitados_extras * quince_ad_100)


cant_invitados_bautismo=0
if evento == bautismo:
    cant_invitados_bautismo+= cant_invitados
    bautismo +=1

    if cant_invitados > 50 :
        total_fac_bautismo +=bautismo_fijo

    elif cant_invitados < 50 and cant_invitados < 100:
        invitados_extras= cant_invitados - 50
        total_fac_bautismo= bautismo_fijo+ (invitados_extras * bautismo_ad_50)

    elif cant_invitados < 100 :
        invitados_extras= cant_invitados - 50
        total_fac_bautismo= bautismo_fijo + (invitados_extras * bautismo_ad_100)


cant_invitados_cumpleaños=0
if evento == cumpleaños:
    cant_invitados_cumpleaños+= cant_invitados
    cumpleaños +=1

    if cant_invitados > 50 :
        total_fac_cumpleaños += cumpleaños_fijo

    elif cant_invitados < 50 and cant_invitados < 100:
        invitados_extras= cant_invitados - 50
        total_fac_cumpleaños= cumpleaños_fijo + (invitados_extras * cumpleaños_ad_50)

    elif cant_invitados < 100 :
        invitados_extras= cant_invitados - 50
        total_fac_cumpleaños= cumpleaños_fijo + (invitados_extras * cumpleaños_ad_100)


cant_invitados_otros=0
if evento == otros:
    cant_invitados_otros+= cant_invitados
    otros +=1

    if cant_invitados > 50 :
        total_fac_otros += cumpleaños_fijo

    elif cant_invitados < 50 and cant_invitados < 100:
        invitados_extras= cant_invitados - 50
        total_fac_otros= otros_fijo + (invitados_extras * otros_ad_50)

    elif cant_invitados < 100 :
        invitados_extras= cant_invitados - 50
        total_fac_otros= otros_fijo + (invitados_extras * otros_ad_100)



#Programa principal:
evento_mes = generar_eventos

mostrar_menu()
opcion = int(input("Ingrese una opcion ): "))





