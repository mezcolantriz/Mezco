from datetime import datetime, timedelta


def seleccionar_lugar(lugares):
    while True:
        for idx, lugar in enumerate(lugares):
            print(f"{idx + 1}. {lugar}")
        seleccion = input("Seleccione un lugar por número o escriba 'back' para regresar: ")

        if seleccion.lower() == "back":
            return "back"
        try:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(lugares):
                return lugares[seleccion - 1]
        except ValueError:
            pass
        print("Selección no válida. Intente de nuevo.")


def calcular_tiempo_espera(numero_pax):
    base_espera = timedelta(hours=5, minutes=15)
    bloques_adicionales = (numero_pax - 1) // 4
    tiempo_adicional = timedelta(minutes=10 * bloques_adicionales)
    return base_espera + tiempo_adicional


def obtener_tiempo_transporte(lugar_salida, lugar_destino, tiempos_transporte):
    try:
        return tiempos_transporte[(lugar_salida, lugar_destino)]
    except KeyError:
        return "Tiempo de transporte no disponible"


def calcular_hora_salida_no_aeropuerto(tee_time, tiempo_transporte):
    hora_tee_time = datetime.strptime(tee_time, "%H:%M")
    tiempo_transporte_total = tiempo_transporte + 60  # Sumar una hora de buffer adicional al tiempo de transporte
    hora_salida = hora_tee_time - timedelta(minutes=tiempo_transporte_total)
    return redondear_minutos(hora_salida)


def redondear_minutos(hora):
    minutos = hora.minute
    minutos_redondeados = round((minutos / 5)) * 5
    if minutos_redondeados == 60:
        hora = hora.replace(hour=(hora.hour + 1) % 24)
        minutos_redondeados = 0
    return hora.replace(minute=minutos_redondeados, second=0, microsecond=0)


def respuesta_positiva(respuesta):
    return respuesta.lower() in ['s', 'si', 'sí', 'ok', 'vale']


def respuesta_negativa(respuesta):
    return respuesta.lower() in ['n', 'no', 'noo']


def obtener_input_valido(prompt, formato):
    while True:
        entrada = input(prompt).strip()
        if entrada.lower() == "back":
            return "back"
        try:
            if formato == "fecha":
                try:
                    datetime.strptime(entrada, "%d/%m/%Y")
                except ValueError:
                    datetime.strptime(entrada, "%d/%m/%y")
            elif formato == "hora":
                datetime.strptime(entrada, "%H:%M")
            elif formato == "numerico":
                int(entrada)
            return entrada
        except ValueError:
            print("Formato no válido. Intente de nuevo.")


def main():
    lugares = sorted([
        "La Finca Golf Hotel", "La Zenia Servigroup", "Villamartin Golf", "Cabo Roig", "Campoamor Hotel",
        "Las Colinas Golf", "La Torre Golf Resort", "Mar Menor Golf Resort", "La Manga Golf Resort", "Roda Golf Resort",
        "Los Alcazáres", "Hotel Lodomar", "Alicante Airport", "Murcia Airport", "Alicante Golf",
        "El Plantio Golf", "Alenda Golf", "Font Del Llop Golf", "La Marquesa Golf", "La Finca Golf",
        "Las Ramblas Golf", "Lo Romero Golf", "La Serena Golf", "Saurines Golf", "El Valle Golf",
        "Hacienda Riquelme Golf", "Condado Alhama Golf", "Hacienda Del Alamo Golf",
        "Vistabella Golf", "Altorreal Golf", "Altaona Golf", "La Finca Golf Hotel", "HOTEL 525", "HOTEL COSTA NAREJOS"
    ])

    tiempos_transporte = {
        ("La Finca Golf Hotel", "La Zenia Servigroup"): 25,
        ("La Finca Golf Hotel", "Villamartin Golf"): 25,
        ("La Finca Golf Hotel", "Cabo Roig"): 30,
        ("La Finca Golf Hotel", "Campoamor Hotel"): 30,
        ("La Finca Golf Hotel", "Las Colinas Golf"): 25,
        ("La Finca Golf Hotel", "La Torre Golf Resort"): 45,
        ("La Finca Golf Hotel", "Mar Menor Golf Resort"): 45,
        ("La Finca Golf Hotel", "La Manga Golf Resort"): 55,
        ("La Finca Golf Hotel", "Roda Golf Resort"): 35,
        ("La Finca Golf Hotel", "Los Alcazáres"): 40,
        ("La Finca Golf Hotel", "Hotel Lodomar"): 35,
        ("La Finca Golf Hotel", "Alicante Airport"): 40,
        ("La Finca Golf Hotel", "Murcia Airport"): 55,
        ("La Finca Golf Hotel", "Alicante Golf"): 50,
        ("La Finca Golf Hotel", "El Plantio Golf"): 40,
        ("La Finca Golf Hotel", "Alenda Golf"): 40,
        ("La Finca Golf Hotel", "Font Del Llop Golf"): 40,
        ("La Finca Golf Hotel", "La Marquesa Golf"): 20,
        ("La Finca Golf Hotel", "Las Ramblas Golf"): 30,
        ("La Finca Golf Hotel", "Campoamor Golf"): 35,
        ("La Finca Golf Hotel", "Lo Romero Golf"): 35,
        ("La Finca Golf Hotel", "La Serena Golf"): 40,
        ("La Finca Golf Hotel", "Saurines Golf"): 45,
        ("La Finca Golf Hotel", "El Valle Golf"): 55,
        ("La Finca Golf Hotel", "Hacienda Riquelme Golf"): 45,
        ("La Finca Golf Hotel", "Condado Alhama Golf"): 75,
        ("La Finca Golf Hotel", "Hacienda Del Alamo Golf"): 70,
        ("La Finca Golf Hotel", "Vistabella Golf"): 20,
        ("La Finca Golf Hotel", "Altorreal Golf"): 50,
        ("La Finca Golf Hotel", "Altaona Golf"): 50,

        # Desde Hotel Costa Narejos

        ("HOTEL COSTA NAREJOS", "La Finca Golf Hotel"): 35,
        ("HOTEL COSTA NAREJOS", "La Zenia Servigroup"): 25,
        ("HOTEL COSTA NAREJOS", "Villamartin Golf"): 25,
        ("HOTEL COSTA NAREJOS", "Cabo Roig"): 25,
        ("HOTEL COSTA NAREJOS", "Campoamor Hotel"): 30,
        ("HOTEL COSTA NAREJOS", "Las Colinas Golf"): 25,
        ("HOTEL COSTA NAREJOS", "La Torre Golf Resort"): 20,
        ("HOTEL COSTA NAREJOS", "Mar Menor Golf Resort"): 15,
        ("HOTEL COSTA NAREJOS", "La Manga Golf Resort"): 25,
        ("HOTEL COSTA NAREJOS", "Roda Golf Resort"): 5,
        ("HOTEL COSTA NAREJOS", "Los Alcazáres"): 5,
        ("HOTEL COSTA NAREJOS", "Hotel Lodomar"): 15,
        ("HOTEL COSTA NAREJOS", "Alicante Airport"): 60,
        ("HOTEL COSTA NAREJOS", "Murcia Airport"): 35,
        ("HOTEL COSTA NAREJOS", "Alicante Golf"): 70,
        ("HOTEL COSTA NAREJOS", "El Plantio Golf"): 60,
        ("HOTEL COSTA NAREJOS", "Alenda Golf"): 60,
        ("HOTEL COSTA NAREJOS", "Font Del Llop Golf"): 60,
        ("HOTEL COSTA NAREJOS", "La Marquesa Golf"): 40,
        ("HOTEL COSTA NAREJOS", "Las Ramblas Golf"): 30,
        ("HOTEL COSTA NAREJOS", "Campoamor Golf"): 30,
        ("HOTEL COSTA NAREJOS", "Lo Romero Golf"): 25,
        ("HOTEL COSTA NAREJOS", "La Serena Golf"): 10,
        ("HOTEL COSTA NAREJOS", "Saurines Golf"): 20,
        ("HOTEL COSTA NAREJOS", "El Valle Golf"): 30,
        ("HOTEL COSTA NAREJOS", "Hacienda Riquelme Golf"): 25,
        ("HOTEL COSTA NAREJOS", "Condado Alhama Golf"): 50,
        ("HOTEL COSTA NAREJOS", "Hacienda Del Alamo Golf"): 40,
        ("HOTEL COSTA NAREJOS", "Vistabella Golf"): 35,
        ("HOTEL COSTA NAREJOS", "Altorreal Golf"): 45,
        ("HOTEL COSTA NAREJOS", "Altaona Golf"): 25,

        # Desde HOTEL 525
        ("HOTEL 525", "La Finca Golf Hotel"): 35,
        ("HOTEL 525", "La Zenia Servigroup"): 25,
        ("HOTEL 525", "Villamartin Golf"): 25,
        ("HOTEL 525", "Cabo Roig"): 30,
        ("HOTEL 525", "Campoamor Hotel"): 30,
        ("HOTEL 525", "Las Colinas Golf"): 25,
        ("HOTEL 525", "La Torre Golf Resort"): 20,
        ("HOTEL 525", "Mar Menor Golf Resort"): 15,
        ("HOTEL 525", "La Manga Golf Resort"): 25,
        ("HOTEL 525", "Roda Golf Resort"): 5,
        ("HOTEL 525", "Los Alcazáres"): 5,
        ("HOTEL 525", "Hotel Lodomar"): 15,
        ("HOTEL 525", "Alicante Airport"): 60,
        ("HOTEL 525", "Murcia Airport"): 30,
        ("HOTEL 525", "Alicante Golf"): 70,
        ("HOTEL 525", "El Plantio Golf"): 60,
        ("HOTEL 525", "Alenda Golf"): 60,
        ("HOTEL 525", "Font Del Llop Golf"): 60,
        ("HOTEL 525", "La Marquesa Golf"): 40,
        ("HOTEL 525", "Las Ramblas Golf"): 30,
        ("HOTEL 525", "Campoamor Golf"): 30,
        ("HOTEL 525", "Lo Romero Golf"): 20,
        ("HOTEL 525", "La Serena Golf"): 10,
        ("HOTEL 525", "Saurines Golf"): 20,
        ("HOTEL 525", "El Valle Golf"): 30,
        ("HOTEL 525", "Hacienda Riquelme Golf"): 20,
        ("HOTEL 525", "Condado Alhama Golf"): 50,
        ("HOTEL 525", "Hacienda Del Alamo Golf"): 35,
        ("HOTEL 525", "Vistabella Golf"): 35,
        ("HOTEL 525", "Altorreal Golf"): 45,
        ("HOTEL 525", "Altaona Golf"): 25,

        # Desde La Zenia Servigroup
        ("La Zenia Servigroup", "Villamartin Golf"): 10,
        ("La Zenia Servigroup", "Cabo Roig"): 10,
        ("La Zenia Servigroup", "Campoamor Hotel"): 15,
        ("La Zenia Servigroup", "Las Colinas Golf"): 25,
        ("La Zenia Servigroup", "La Torre Golf Resort"): 35,
        ("La Zenia Servigroup", "Mar Menor Golf Resort"): 30,
        ("La Zenia Servigroup", "La Manga Golf Resort"): 45,
        ("La Zenia Servigroup", "Roda Golf Resort"): 25,
        ("La Zenia Servigroup", "Los Alcazáres"): 25,
        ("La Zenia Servigroup", "Hotel Lodomar"): 20,
        ("La Zenia Servigroup", "Alicante Airport"): 50,
        ("La Zenia Servigroup", "Murcia Airport"): 45,
        ("La Zenia Servigroup", "Alicante Golf"): 60,
        ("La Zenia Servigroup", "El Plantio Golf"): 50,
        ("La Zenia Servigroup", "Alenda Golf"): 50,
        ("La Zenia Servigroup", "Font Del Llop Golf"): 45,
        ("La Zenia Servigroup", "La Marquesa Golf"): 30,
        ("La Zenia Servigroup", "Las Ramblas Golf"): 15,
        ("La Zenia Servigroup", "Campoamor Golf"): 15,
        ("La Zenia Servigroup", "Lo Romero Golf"): 25,
        ("La Zenia Servigroup", "La Serena Golf"): 30,
        ("La Zenia Servigroup", "Saurines Golf"): 35,
        ("La Zenia Servigroup", "El Valle Golf"): 40,
        ("La Zenia Servigroup", "Hacienda Riquelme Golf"): 30,
        ("La Zenia Servigroup", "Condado Alhama Golf"): 70,
        ("La Zenia Servigroup", "Hacienda Del Alamo Golf"): 55,
        ("La Zenia Servigroup", "Vistabella Golf"): 25,
        ("La Zenia Servigroup", "Altorreal Golf"): 60,
        ("La Zenia Servigroup", "Altaona Golf"): 35,

        # Desde Villamartin Golf
        ("Villamartin Golf", "Cabo Roig"): 15,
        ("Villamartin Golf", "Campoamor Hotel"): 10,
        ("Villamartin Golf", "Las Colinas Golf"): 15,
        ("Villamartin Golf", "La Torre Golf Resort"): 30,
        ("Villamartin Golf", "Mar Menor Golf Resort"): 35,
        ("Villamartin Golf", "La Manga Golf Resort"): 40,
        ("Villamartin Golf", "Roda Golf Resort"): 25,
        ("Villamartin Golf", "Los Alcazáres"): 30,
        ("Villamartin Golf", "Hotel Lodomar"): 20,
        ("Villamartin Golf", "Alicante Airport"): 45,
        ("Villamartin Golf", "Murcia Airport"): 45,
        ("Villamartin Golf", "Alicante Golf"): 60,
        ("Villamartin Golf", "El Plantio Golf"): 55,
        ("Villamartin Golf", "Alenda Golf"): 45,
        ("Villamartin Golf", "Font Del Llop Golf"): 50,
        ("Villamartin Golf", "La Marquesa Golf"): 30,
        ("Villamartin Golf", "Las Ramblas Golf"): 10,
        ("Villamartin Golf", "Campoamor Golf"): 10,
        ("Villamartin Golf", "Lo Romero Golf"): 25,
        ("Villamartin Golf", "La Serena Golf"): 25,
        ("Villamartin Golf", "Saurines Golf"): 35,
        ("Villamartin Golf", "El Valle Golf"): 40,
        ("Villamartin Golf", "Hacienda Riquelme Golf"): 30,
        ("Villamartin Golf", "Condado Alhama Golf"): 65,
        ("Villamartin Golf", "Hacienda Del Alamo Golf"): 55,
        ("Villamartin Golf", "Vistabella Golf"): 20,
        ("Villamartin Golf", "Altorreal Golf"): 55,
        ("Villamartin Golf", "Altaona Golf"): 30,

        # Desde Cabo Roig
        ("Cabo Roig", "Campoamor Hotel"): 15,
        ("Cabo Roig", "Las Colinas Golf"): 20,
        ("Cabo Roig", "La Torre Golf Resort"): 30,
        ("Cabo Roig", "Mar Menor Golf Resort"): 30,
        ("Cabo Roig", "La Manga Golf Resort"): 40,
        ("Cabo Roig", "Roda Golf Resort"): 25,
        ("Cabo Roig", "Los Alcazáres"): 25,
        ("Cabo Roig", "Hotel Lodomar"): 20,
        ("Cabo Roig", "Alicante Airport"): 45,
        ("Cabo Roig", "Murcia Airport"): 40,
        ("Cabo Roig", "Alicante Golf"): 60,
        ("Cabo Roig", "El Plantio Golf"): 50,
        ("Cabo Roig", "Alenda Golf"): 45,
        ("Cabo Roig", "Font Del Llop Golf"): 45,
        ("Cabo Roig", "La Marquesa Golf"): 30,
        ("Cabo Roig", "Las Ramblas Golf"): 15,
        ("Cabo Roig", "Campoamor Golf"): 15,
        ("Cabo Roig", "Lo Romero Golf"): 20,
        ("Cabo Roig", "La Serena Golf"): 25,
        ("Cabo Roig", "Saurines Golf"): 30,
        ("Cabo Roig", "El Valle Golf"): 35,
        ("Cabo Roig", "Hacienda Riquelme Golf"): 30,
        ("Cabo Roig", "Condado Alhama Golf"): 70,
        ("Cabo Roig", "Hacienda Del Alamo Golf"): 55,
        ("Cabo Roig", "Vistabella Golf"): 25,
        ("Cabo Roig", "Altorreal Golf"): 60,
        ("Cabo Roig", "Altaona Golf"): 35,

        # Desde Campoamor Hotel
        ("Campoamor Hotel", "Las Colinas Golf"): 20,
        ("Campoamor Hotel", "La Torre Golf Resort"): 35,
        ("Campoamor Hotel", "Mar Menor Golf Resort"): 35,
        ("Campoamor Hotel", "La Manga Golf Resort"): 45,
        ("Campoamor Hotel", "Roda Golf Resort"): 30,
        ("Campoamor Hotel", "Los Alcazáres"): 30,
        ("Campoamor Hotel", "Hotel Lodomar"): 25,
        ("Campoamor Hotel", "Alicante Airport"): 50,
        ("Campoamor Hotel", "Murcia Airport"): 45,
        ("Campoamor Hotel", "Alicante Golf"): 60,
        ("Campoamor Hotel", "El Plantio Golf"): 55,
        ("Campoamor Hotel", "Alenda Golf"): 50,
        ("Campoamor Hotel", "Font Del Llop Golf"): 50,
        ("Campoamor Hotel", "La Marquesa Golf"): 30,
        ("Campoamor Hotel", "Las Ramblas Golf"): 10,
        ("Campoamor Hotel", "Campoamor Golf"): 5,
        ("Campoamor Hotel", "Lo Romero Golf"): 25,
        ("Campoamor Hotel", "La Serena Golf"): 30,
        ("Campoamor Hotel", "Saurines Golf"): 35,
        ("Campoamor Hotel", "El Valle Golf"): 40,
        ("Campoamor Hotel", "Hacienda Riquelme Golf"): 35,
        ("Campoamor Hotel", "Condado Alhama Golf"): 70,
        ("Campoamor Hotel", "Hacienda Del Alamo Golf"): 55,
        ("Campoamor Hotel", "Vistabella Golf"): 25,
        ("Campoamor Hotel", "Altorreal Golf"): 60,
        ("Campoamor Hotel", "Altaona Golf"): 35,

        # Desde Las Colinas Golf
        ("Las Colinas Golf", "La Torre Golf Resort"): 20,
        ("Las Colinas Golf", "Mar Menor Golf Resort"): 25,
        ("Las Colinas Golf", "La Manga Golf Resort"): 30,
        ("Las Colinas Golf", "Roda Golf Resort"): 35,
        ("Las Colinas Golf", "Los Alcazáres"): 25,
        ("Las Colinas Golf", "Hotel Lodomar"): 30,
        ("Las Colinas Golf", "Alicante Airport"): 40,
        ("Las Colinas Golf", "Murcia Airport"): 50,
        ("Las Colinas Golf", "Alicante Golf"): 25,
        ("Las Colinas Golf", "El Plantio Golf"): 15,
        ("Las Colinas Golf", "Alenda Golf"): 20,
        ("Las Colinas Golf", "Font Del Llop Golf"): 25,
        ("Las Colinas Golf", "La Marquesa Golf"): 30,
        ("Las Colinas Golf", "Las Ramblas Golf"): 20,
        ("Las Colinas Golf", "Campoamor Golf"): 20,
        ("Las Colinas Golf", "Lo Romero Golf"): 25,
        ("Las Colinas Golf", "La Serena Golf"): 30,
        ("Las Colinas Golf", "Saurines Golf"): 40,
        ("Las Colinas Golf", "El Valle Golf"): 45,
        ("Las Colinas Golf", "Hacienda Riquelme Golf"): 35,
        ("Las Colinas Golf", "Condado Alhama Golf"): 50,
        ("Las Colinas Golf", "Hacienda Del Alamo Golf"): 55,
        ("Las Colinas Golf", "Vistabella Golf"): 50,
        ("Las Colinas Golf", "Altorreal Golf"): 45,
        ("Las Colinas Golf", "Altaona Golf"): 50,

        # Desde La Torre Golf Resort
        ("La Torre Golf Resort", "Mar Menor Golf Resort"): 20,
        ("La Torre Golf Resort", "La Manga Golf Resort"): 35,
        ("La Torre Golf Resort", "Roda Golf Resort"): 20,
        ("La Torre Golf Resort", "Los Alcazáres"): 20,
        ("La Torre Golf Resort", "Hotel Lodomar"): 25,
        ("La Torre Golf Resort", "Alicante Airport"): 65,
        ("La Torre Golf Resort", "Murcia Airport"): 20,
        ("La Torre Golf Resort", "Alicante Golf"): 75,
        ("La Torre Golf Resort", "El Plantio Golf"): 65,
        ("La Torre Golf Resort", "Alenda Golf"): 60,
        ("La Torre Golf Resort", "Font Del Llop Golf"): 65,
        ("La Torre Golf Resort", "La Marquesa Golf"): 45,
        ("La Torre Golf Resort", "Las Ramblas Golf"): 35,
        ("La Torre Golf Resort", "Campoamor Golf"): 35,
        ("La Torre Golf Resort", "Lo Romero Golf"): 30,
        ("La Torre Golf Resort", "La Serena Golf"): 20,
        ("La Torre Golf Resort", "Saurines Golf"): 10,
        ("La Torre Golf Resort", "El Valle Golf"): 15,
        ("La Torre Golf Resort", "Hacienda Riquelme Golf"): 20,
        ("La Torre Golf Resort", "Condado Alhama Golf"): 45,
        ("La Torre Golf Resort", "Hacienda Del Alamo Golf"): 30,
        ("La Torre Golf Resort", "Vistabella Golf"): 40,
        ("La Torre Golf Resort", "Altorreal Golf"): 35,
        ("La Torre Golf Resort", "Altaona Golf"): 10,

        # Desde Mar Menor Golf Resort
        ("Mar Menor Golf Resort", "La Manga Golf Resort"): 25,
        ("Mar Menor Golf Resort", "Roda Golf Resort"): 10,
        ("Mar Menor Golf Resort", "Los Alcazáres"): 15,
        ("Mar Menor Golf Resort", "Hotel Lodomar"): 20,
        ("Mar Menor Golf Resort", "Alicante Airport"): 60,
        ("Mar Menor Golf Resort", "Murcia Airport"): 30,
        ("Mar Menor Golf Resort", "Alicante Golf"): 75,
        ("Mar Menor Golf Resort", "El Plantio Golf"): 65,
        ("Mar Menor Golf Resort", "Alenda Golf"): 60,
        ("Mar Menor Golf Resort", "Font Del Llop Golf"): 60,
        ("Mar Menor Golf Resort", "La Marquesa Golf"): 45,
        ("Mar Menor Golf Resort", "Las Ramblas Golf"): 35,
        ("Mar Menor Golf Resort", "Campoamor Golf"): 35,
        ("Mar Menor Golf Resort", "Lo Romero Golf"): 30,
        ("Mar Menor Golf Resort", "La Serena Golf"): 10,
        ("Mar Menor Golf Resort", "Saurines Golf"): 20,
        ("Mar Menor Golf Resort", "El Valle Golf"): 30,
        ("Mar Menor Golf Resort", "Hacienda Riquelme Golf"): 25,
        ("Mar Menor Golf Resort", "Condado Alhama Golf"): 45,
        ("Mar Menor Golf Resort", "Hacienda Del Alamo Golf"): 30,
        ("Mar Menor Golf Resort", "Vistabella Golf"): 40,
        ("Mar Menor Golf Resort", "Altorreal Golf"): 50,
        ("Mar Menor Golf Resort", "Altaona Golf"): 25,

        # Desde La Manga Golf Resort
        ("La Manga Golf Resort", "Roda Golf Resort"): 25,
        ("La Manga Golf Resort", "Los Alcazáres"): 25,
        ("La Manga Golf Resort", "Hotel Lodomar"): 35,
        ("La Manga Golf Resort", "Alicante Airport"): 65,
        ("La Manga Golf Resort", "Murcia Airport"): 35,
        ("La Manga Golf Resort", "Alicante Golf"): 85,
        ("La Manga Golf Resort", "El Plantio Golf"): 75,
        ("La Manga Golf Resort", "Alenda Golf"): 60,
        ("La Manga Golf Resort", "Font Del Llop Golf"): 75,
        ("La Manga Golf Resort", "La Marquesa Golf"): 55,
        ("La Manga Golf Resort", "Las Ramblas Golf"): 45,
        ("La Manga Golf Resort", "Campoamor Golf"): 45,
        ("La Manga Golf Resort", "Lo Romero Golf"): 40,
        ("La Manga Golf Resort", "La Serena Golf"): 25,
        ("La Manga Golf Resort", "Saurines Golf"): 35,
        ("La Manga Golf Resort", "El Valle Golf"): 45,
        ("La Manga Golf Resort", "Hacienda Riquelme Golf"): 40,
        ("La Manga Golf Resort", "Condado Alhama Golf"): 50,
        ("La Manga Golf Resort", "Hacienda Del Alamo Golf"): 40,
        ("La Manga Golf Resort", "Vistabella Golf"): 50,
        ("La Manga Golf Resort", "Altorreal Golf"): 55,
        ("La Manga Golf Resort", "Altaona Golf"): 35,

        # Desde Roda Golf Resort
        ("Roda Golf Resort", "Los Alcazáres"): 5,
        ("Roda Golf Resort", "Hotel Lodomar"): 15,
        ("Roda Golf Resort", "Alicante Airport"): 60,
        ("Roda Golf Resort", "Murcia Airport"): 35,
        ("Roda Golf Resort", "Alicante Golf"): 65,
        ("Roda Golf Resort", "El Plantio Golf"): 60,
        ("Roda Golf Resort", "Alenda Golf"): 55,
        ("Roda Golf Resort", "Font Del Llop Golf"): 60,
        ("Roda Golf Resort", "La Marquesa Golf"): 40,
        ("Roda Golf Resort", "Las Ramblas Golf"): 30,
        ("Roda Golf Resort", "Campoamor Golf"): 25,
        ("Roda Golf Resort", "Lo Romero Golf"): 20,
        ("Roda Golf Resort", "La Serena Golf"): 10,
        ("Roda Golf Resort", "Saurines Golf"): 20,
        ("Roda Golf Resort", "El Valle Golf"): 30,
        ("Roda Golf Resort", "Hacienda Riquelme Golf"): 20,
        ("Roda Golf Resort", "Condado Alhama Golf"): 50,
        ("Roda Golf Resort", "Hacienda Del Alamo Golf"): 40,
        ("Roda Golf Resort", "Vistabella Golf"): 35,
        ("Roda Golf Resort", "Altorreal Golf"): 45,
        ("Roda Golf Resort", "Altaona Golf"): 25,

        # Desde Los Alcazáres
        ("Los Alcazáres", "Hotel Lodomar"): 15,
        ("Los Alcazáres", "Alicante Airport"): 60,
        ("Los Alcazáres", "Murcia Airport"): 35,
        ("Los Alcazáres", "Alicante Golf"): 65,
        ("Los Alcazáres", "El Plantio Golf"): 60,
        ("Los Alcazáres", "Alenda Golf"): 55,
        ("Los Alcazáres", "Font Del Llop Golf"): 60,
        ("Los Alcazáres", "La Marquesa Golf"): 40,
        ("Los Alcazáres", "Las Ramblas Golf"): 30,
        ("Los Alcazáres", "Campoamor Golf"): 25,
        ("Los Alcazáres", "Lo Romero Golf"): 20,
        ("Los Alcazáres", "La Serena Golf"): 10,
        ("Los Alcazáres", "Saurines Golf"): 20,
        ("Los Alcazáres", "El Valle Golf"): 30,
        ("Los Alcazáres", "Hacienda Riquelme Golf"): 20,
        ("Los Alcazáres", "Condado Alhama Golf"): 50,
        ("Los Alcazáres", "Hacienda Del Alamo Golf"): 45,
        ("Los Alcazáres", "Vistabella Golf"): 35,
        ("Los Alcazáres", "Altorreal Golf"): 45,
        ("Los Alcazáres", "Altaona Golf"): 25,

        # Desde Hotel Lodomar
        ("Hotel Lodomar", "Alicante Airport"): 50,
        ("Hotel Lodomar", "Murcia Airport"): 35,
        ("Hotel Lodomar", "Alicante Golf"): 65,
        ("Hotel Lodomar", "El Plantio Golf"): 55,
        ("Hotel Lodomar", "Alenda Golf"): 50,
        ("Hotel Lodomar", "Font Del Llop Golf"): 55,
        ("Hotel Lodomar", "La Marquesa Golf"): 35,
        ("Hotel Lodomar", "Las Ramblas Golf"): 25,
        ("Hotel Lodomar", "Campoamor Golf"): 25,
        ("Hotel Lodomar", "Lo Romero Golf"): 20,
        ("Hotel Lodomar", "La Serena Golf"): 20,
        ("Hotel Lodomar", "Saurines Golf"): 25,
        ("Hotel Lodomar", "El Valle Golf"): 30,
        ("Hotel Lodomar", "Hacienda Riquelme Golf"): 25,
        ("Hotel Lodomar", "Condado Alhama Golf"): 60,
        ("Hotel Lodomar", "Hacienda Del Alamo Golf"): 45,
        ("Hotel Lodomar", "Vistabella Golf"): 30,
        ("Hotel Lodomar", "Altorreal Golf"): 50,
        ("Hotel Lodomar", "Altaona Golf"): 25,

        # Desde Alicante Airport
        ("Alicante Airport", "Murcia Airport"): 60,
        ("Alicante Airport", "Alicante Golf"): 20,
        ("Alicante Airport", "El Plantio Golf"): 10,
        ("Alicante Airport", "Alenda Golf"): 15,
        ("Alicante Airport", "Font Del Llop Golf"): 20,
        ("Alicante Airport", "La Marquesa Golf"): 35,
        ("Alicante Airport", "Las Ramblas Golf"): 55,
        ("Alicante Airport", "Campoamor Golf"): 50,
        ("Alicante Airport", "Lo Romero Golf"): 55,
        ("Alicante Airport", "La Serena Golf"): 60,
        ("Alicante Airport", "Saurines Golf"): 65,
        ("Alicante Airport", "El Valle Golf"): 65,
        ("Alicante Airport", "Hacienda Riquelme Golf"): 65,
        ("Alicante Airport", "Condado Alhama Golf"): 75,
        ("Alicante Airport", "Hacienda Del Alamo Golf"): 75,
        ("Alicante Airport", "Vistabella Golf"): 40,
        ("Alicante Airport", "Altorreal Golf"): 45,
        ("Alicante Airport", "Altaona Golf"): 55,

        # Desde Murcia Airport
        ("Murcia Airport", "Alicante Golf"): 75,
        ("Murcia Airport", "El Plantio Golf"): 65,
        ("Murcia Airport", "Alenda Golf"): 60,
        ("Murcia Airport", "Font Del Llop Golf"): 60,
        ("Murcia Airport", "La Marquesa Golf"): 55,
        ("Murcia Airport", "Las Ramblas Golf"): 45,
        ("Murcia Airport", "Campoamor Golf"): 45,
        ("Murcia Airport", "Lo Romero Golf"): 40,
        ("Murcia Airport", "La Serena Golf"): 30,
        ("Murcia Airport", "Saurines Golf"): 20,
        ("Murcia Airport", "El Valle Golf"): 20,
        ("Murcia Airport", "Hacienda Riquelme Golf"): 25,
        ("Murcia Airport", "Condado Alhama Golf"): 35,
        ("Murcia Airport", "Hacienda Del Alamo Golf"): 20,
        ("Murcia Airport", "Vistabella Golf"): 55,
        ("Murcia Airport", "Altorreal Golf"): 35,
        ("Murcia Airport", "Altaona Golf"): 15,

        # Desde Alicante Golf
        ("Alicante Golf", "El Plantio Golf"): 20,
        ("Alicante Golf", "Alenda Golf"): 25,
        ("Alicante Golf", "Font Del Llop Golf"): 30,
        ("Alicante Golf", "La Marquesa Golf"): 50,
        ("Alicante Golf", "Las Ramblas Golf"): 65,
        ("Alicante Golf", "Campoamor Golf"): 60,
        ("Alicante Golf", "Lo Romero Golf"): 65,
        ("Alicante Golf", "La Serena Golf"): 70,
        ("Alicante Golf", "Saurines Golf"): 75,
        ("Alicante Golf", "El Valle Golf"): 75,
        ("Alicante Golf", "Hacienda Riquelme Golf"): 70,
        ("Alicante Golf", "Condado Alhama Golf"): 85,
        ("Alicante Golf", "Hacienda Del Alamo Golf"): 85,
        ("Alicante Golf", "Vistabella Golf"): 55,
        ("Alicante Golf", "Altorreal Golf"): 60,
        ("Alicante Golf", "Altaona Golf"): 70,

        # Desde El Plantio Golf
        ("El Plantio Golf", "Alenda Golf"): 20,
        ("El Plantio Golf", "Font Del Llop Golf"): 25,
        ("El Plantio Golf", "La Marquesa Golf"): 45,
        ("El Plantio Golf", "Las Ramblas Golf"): 60,
        ("El Plantio Golf", "Campoamor Golf"): 55,
        ("El Plantio Golf", "Lo Romero Golf"): 60,
        ("El Plantio Golf", "La Serena Golf"): 65,
        ("El Plantio Golf", "Saurines Golf"): 70,
        ("El Plantio Golf", "El Valle Golf"): 70,
        ("El Plantio Golf", "Hacienda Riquelme Golf"): 70,
        ("El Plantio Golf", "Condado Alhama Golf"): 75,
        ("El Plantio Golf", "Hacienda Del Alamo Golf"): 80,
        ("El Plantio Golf", "Vistabella Golf"): 45,
        ("El Plantio Golf", "Altorreal Golf"): 55,
        ("El Plantio Golf", "Altaona Golf"): 60,

        # Desde Alenda Golf
        ("Alenda Golf", "Font Del Llop Golf"): 10,
        ("Alenda Golf", "La Marquesa Golf"): 35,
        ("Alenda Golf", "Las Ramblas Golf"): 50,
        ("Alenda Golf", "Campoamor Golf"): 50,
        ("Alenda Golf", "Lo Romero Golf"): 55,
        ("Alenda Golf", "La Serena Golf"): 60,
        ("Alenda Golf", "Saurines Golf"): 60,
        ("Alenda Golf", "El Valle Golf"): 60,
        ("Alenda Golf", "Hacienda Riquelme Golf"): 60,
        ("Alenda Golf", "Condado Alhama Golf"): 45,
        ("Alenda Golf", "Hacienda Del Alamo Golf"): 70,
        ("Alenda Golf", "Vistabella Golf"): 40,
        ("Alenda Golf", "Altorreal Golf"): 45,
        ("Alenda Golf", "Altaona Golf"): 60,

        # Desde Font Del Llop Golf
        ("Font Del Llop Golf", "La Marquesa Golf"): 35,
        ("Font Del Llop Golf", "Las Ramblas Golf"): 55,
        ("Font Del Llop Golf", "Campoamor Golf"): 50,
        ("Font Del Llop Golf", "Lo Romero Golf"): 55,
        ("Font Del Llop Golf", "La Serena Golf"): 60,
        ("Font Del Llop Golf", "Saurines Golf"): 65,
        ("Font Del Llop Golf", "El Valle Golf"): 65,
        ("Font Del Llop Golf", "Hacienda Riquelme Golf"): 65,
        ("Font Del Llop Golf", "Condado Alhama Golf"): 75,
        ("Font Del Llop Golf", "Hacienda Del Alamo Golf"): 75,
        ("Font Del Llop Golf", "Vistabella Golf"): 40,
        ("Font Del Llop Golf", "Altorreal Golf"): 45,
        ("Font Del Llop Golf", "Altaona Golf"): 60,

        # Desde La Marquesa Golf
        ("La Marquesa Golf", "Las Ramblas Golf"): 30,
        ("La Marquesa Golf", "Campoamor Golf"): 30,
        ("La Marquesa Golf", "Lo Romero Golf"): 35,
        ("La Marquesa Golf", "La Serena Golf"): 40,
        ("La Marquesa Golf", "Saurines Golf"): 45,
        ("La Marquesa Golf", "El Valle Golf"): 50,
        ("La Marquesa Golf", "Hacienda Riquelme Golf"): 45,
        ("La Marquesa Golf", "Condado Alhama Golf"): 80,
        ("La Marquesa Golf", "Hacienda Del Alamo Golf"): 65,
        ("La Marquesa Golf", "Vistabella Golf"): 20,
        ("La Marquesa Golf", "Altorreal Golf"): 45,
        ("La Marquesa Golf", "Altaona Golf"): 50,

        # Desde Las Ramblas Golf
        ("Las Ramblas Golf", "Campoamor Golf"): 10,
        ("Las Ramblas Golf", "Lo Romero Golf"): 25,
        ("Las Ramblas Golf", "La Serena Golf"): 30,
        ("Las Ramblas Golf", "Saurines Golf"): 35,
        ("Las Ramblas Golf", "El Valle Golf"): 40,
        ("Las Ramblas Golf", "Hacienda Riquelme Golf"): 35,
        ("Las Ramblas Golf", "Condado Alhama Golf"): 75,
        ("Las Ramblas Golf", "Hacienda Del Alamo Golf"): 60,
        ("Las Ramblas Golf", "Vistabella Golf"): 25,
        ("Las Ramblas Golf", "Altorreal Golf"): 60,
        ("Las Ramblas Golf", "Altaona Golf"): 40,

        # Desde Campoamor Golf
        ("Campoamor Golf", "Lo Romero Golf"): 25,
        ("Campoamor Golf", "La Serena Golf"): 30,
        ("Campoamor Golf", "Saurines Golf"): 35,
        ("Campoamor Golf", "El Valle Golf"): 40,
        ("Campoamor Golf", "Hacienda Riquelme Golf"): 35,
        ("Campoamor Golf", "Condado Alhama Golf"): 75,
        ("Campoamor Golf", "Hacienda Del Alamo Golf"): 55,
        ("Campoamor Golf", "Vistabella Golf"): 25,
        ("Campoamor Golf", "Altorreal Golf"): 60,
        ("Campoamor Golf", "Altaona Golf"): 35,

        # Desde Lo Romero Golf
        ("Lo Romero Golf", "La Serena Golf"): 20,
        ("Lo Romero Golf", "Saurines Golf"): 30,
        ("Lo Romero Golf", "El Valle Golf"): 35,
        ("Lo Romero Golf", "Hacienda Riquelme Golf"): 25,
        ("Lo Romero Golf", "Condado Alhama Golf"): 70,
        ("Lo Romero Golf", "Hacienda Del Alamo Golf"): 55,
        ("Lo Romero Golf", "Vistabella Golf"): 30,
        ("Lo Romero Golf", "Altorreal Golf"): 55,
        ("Lo Romero Golf", "Altaona Golf"): 35,

        # Desde La Serena Golf
        ("La Serena Golf", "Saurines Golf"): 20,
        ("La Serena Golf", "El Valle Golf"): 25,
        ("La Serena Golf", "Hacienda Riquelme Golf"): 25,
        ("La Serena Golf", "Condado Alhama Golf"): 50,
        ("La Serena Golf", "Hacienda Del Alamo Golf"): 35,
        ("La Serena Golf", "Vistabella Golf"): 35,
        ("La Serena Golf", "Altorreal Golf"): 45,
        ("La Serena Golf", "Altaona Golf"): 25,

        # Desde Saurines Golf
        ("Saurines Golf", "El Valle Golf"): 20,
        ("Saurines Golf", "Hacienda Riquelme Golf"): 20,
        ("Saurines Golf", "Condado Alhama Golf"): 45,
        ("Saurines Golf", "Hacienda Del Alamo Golf"): 30,
        ("Saurines Golf", "Vistabella Golf"): 45,
        ("Saurines Golf", "Altorreal Golf"): 40,
        ("Saurines Golf", "Altaona Golf"): 20,

        # Desde El Valle Golf
        ("El Valle Golf", "Hacienda Riquelme Golf"): 20,
        ("El Valle Golf", "Condado Alhama Golf"): 45,
        ("El Valle Golf", "Hacienda Del Alamo Golf"): 30,
        ("El Valle Golf", "Vistabella Golf"): 50,
        ("El Valle Golf", "Altorreal Golf"): 30,
        ("El Valle Golf", "Altaona Golf"): 10,

        # Desde Hacienda Riquelme Golf
        ("Hacienda Riquelme Golf", "Condado Alhama Golf"): 50,
        ("Hacienda Riquelme Golf", "Hacienda Del Alamo Golf"): 35,
        ("Hacienda Riquelme Golf", "Vistabella Golf"): 35,
        ("Hacienda Riquelme Golf", "Altorreal Golf"): 40,
        ("Hacienda Riquelme Golf", "Altaona Golf"): 15,

        # Desde Condado Alhama Golf
        ("Condado Alhama Golf", "Hacienda Del Alamo Golf"): 25,
        ("Condado Alhama Golf", "Vistabella Golf"): 75,
        ("Condado Alhama Golf", "Altorreal Golf"): 45,
        ("Condado Alhama Golf", "Altaona Golf"): 45,

        # Desde Hacienda Del Alamo Golf
        ("Hacienda Del Alamo Golf", "Vistabella Golf"): 65,
        ("Hacienda Del Alamo Golf", "Altorreal Golf"): 45,
        ("Hacienda Del Alamo Golf", "Altaona Golf"): 30,

        # Desde Vistabella Golf
        ("Vistabella Golf", "Altorreal Golf"): 45,
        ("Vistabella Golf", "Altaona Golf"): 20,

        # Desde Altorreal Golf
        ("Altorreal Golf", "Altaona Golf"): 25
    }

    while True:
        servicios = []

        calcular_automatico = input("¿Deseas calcular automáticamente el tiempo de espera? (S/N): ").strip().upper()
        while not (respuesta_positiva(calcular_automatico) or respuesta_negativa(calcular_automatico)):
            calcular_automatico = input(
                "Respuesta no válida. ¿Deseas calcular automáticamente el tiempo de espera? (S/N): ").strip().upper()

        while True:
            step = "start"
            data = {}
            servicio = ""

            while step != "done":
                if step == "start":
                    lugar_salida = seleccionar_lugar(lugares)
                    if lugar_salida == "back":
                        step = "start"
                    else:
                        data["lugar_salida"] = lugar_salida
                        step = "destino"

                elif step == "destino":
                    lugar_destino = seleccionar_lugar(lugares)
                    if lugar_destino == "back":
                        step = "start"
                    else:
                        data["lugar_destino"] = lugar_destino
                        step = "fecha"

                elif step == "fecha":
                    fecha = obtener_input_valido("Introduce la fecha del viaje (formato DD/MM/AA o DD/MM/AAAA): ",
                                                 "fecha")
                    if fecha == "back":
                        step = "destino"
                    else:
                        data["fecha"] = fecha
                        if data["lugar_salida"] in ["Alicante Airport", "Murcia Airport"]:
                            step = "hora_llegada_vuelo"
                        elif data["lugar_destino"] in ["Alicante Airport", "Murcia Airport"]:
                            step = "hora_salida_vuelo"
                        else:
                            step = "tee_time"

                elif step == "hora_llegada_vuelo":
                    hora_llegada_vuelo = obtener_input_valido(
                        "Introduce la hora de llegada del vuelo (formato HH:MM): ", "hora")
                    if hora_llegada_vuelo == "back":
                        step = "fecha"
                    else:
                        data["hora_llegada_vuelo"] = hora_llegada_vuelo
                        step = "done"
                        servicio = (
                            f"{data['fecha']} AT {hora_llegada_vuelo} FROM {data['lugar_salida'].upper()} TO {data['lugar_destino'].upper()}. FLIGHT __ ARRIVAL AT {hora_llegada_vuelo}")

                elif step == "hora_salida_vuelo":
                    hora_salida_vuelo = obtener_input_valido("Introduce la hora de salida del vuelo (formato HH:MM): ",
                                                             "hora")
                    if hora_salida_vuelo == "back":
                        step = "fecha"
                    else:
                        data["hora_salida_vuelo"] = hora_salida_vuelo
                        step = "done"
                        tee_time = datetime.strptime(hora_salida_vuelo, "%H:%M")
                        tiempo_transporte_total = int(
                            obtener_tiempo_transporte(data["lugar_salida"], data["lugar_destino"],
                                                      tiempos_transporte)) + 120
                        hora_salida = tee_time - timedelta(minutes=tiempo_transporte_total)
                        hora_salida = redondear_minutos(hora_salida)
                        servicio = (
                            f"{data['fecha']} AT {hora_salida.strftime('%H:%M')} FROM {data['lugar_salida'].upper()} TO {data['lugar_destino'].upper()}. FLIGHT __ DEPARTURE AT {hora_salida_vuelo}")

                elif step == "tee_time":
                    tee_time = obtener_input_valido("Introduce la hora de tee time (formato HH:MM): ", "hora")
                    if tee_time == "back":
                        step = "fecha"
                    else:
                        data["tee_time"] = tee_time
                        step = "numero_pax"

                elif step == "numero_pax":
                    numero_pax = obtener_input_valido("Introduce el número de pasajeros: ", "numerico")
                    if numero_pax == "back":
                        step = "tee_time"
                    else:
                        data["numero_pax"] = int(numero_pax)
                        if respuesta_positiva(calcular_automatico):
                            data["tiempo_espera"] = calcular_tiempo_espera(data["numero_pax"])
                        else:
                            step = "tiempo_espera_manual"

                        if step != "tiempo_espera_manual":
                            step = "done"
                            tiempo_transporte_total = obtener_tiempo_transporte(data["lugar_salida"],
                                                                                data["lugar_destino"],
                                                                                tiempos_transporte)
                            if tiempo_transporte_total == "Tiempo de transporte no disponible":
                                print(tiempo_transporte_total)
                                continue
                            tiempo_transporte_total = int(tiempo_transporte_total)
                            hora_salida = calcular_hora_salida_no_aeropuerto(data["tee_time"], tiempo_transporte_total)
                            hora_regreso = (datetime.strptime(data["tee_time"], "%H:%M") + data["tiempo_espera"])
                            hora_regreso = redondear_minutos(hora_regreso)
                            servicio = (
                                f"{data['fecha']} AT {hora_salida.strftime('%H:%M')} FROM {data['lugar_salida'].upper()} TO {data['lugar_destino'].upper()}. BACK AT {hora_regreso.strftime('%H:%M')}. ({data['numero_pax']} PAX)")

                elif step == "tiempo_espera_manual":
                    tiempo_espera_input = obtener_input_valido(
                        "Introduce el tiempo de espera en el destino (formato HH:MM): ", "hora")
                    if tiempo_espera_input == "back":
                        step = "numero_pax"
                    else:
                        tiempo_espera = datetime.strptime(tiempo_espera_input, "%H:%M")
                        data["tiempo_espera"] = timedelta(hours=tiempo_espera.hour, minutes=tiempo_espera.minute)
                        step = "done"
                        tiempo_transporte_total = obtener_tiempo_transporte(data["lugar_salida"], data["lugar_destino"],
                                                                            tiempos_transporte)
                        if tiempo_transporte_total == "Tiempo de transporte no disponible":
                            print(tiempo_transporte_total)
                            continue
                        tiempo_transporte_total = int(tiempo_transporte_total)
                        hora_salida = calcular_hora_salida_no_aeropuerto(data["tee_time"], tiempo_transporte_total)
                        hora_regreso = (datetime.strptime(data["tee_time"], "%H:%M") + data["tiempo_espera"])
                        hora_regreso = redondear_minutos(hora_regreso)
                        servicio = (
                            f"{data['fecha']} AT {hora_salida.strftime('%H:%M')} FROM {data['lugar_salida'].upper()} TO {data['lugar_destino'].upper()}. BACK AT {hora_regreso.strftime('%H:%M')}. ({data['numero_pax']} PAX)")

                if servicio:
                    servicios.append(servicio)

            print("\nServicios generados:")
            for servicio in servicios:
                print(servicio)

            mas_servicios = input("¿Deseas añadir otro servicio? (S/N): ").strip()
            while not (respuesta_positiva(mas_servicios) or respuesta_negativa(mas_servicios)):
                mas_servicios = input("Respuesta no válida. ¿Deseas añadir otro servicio? (S/N): ").strip()
            if respuesta_negativa(mas_servicios):
                break

        print("\nLista final de servicios generados:")
        for servicio in servicios:
            print(servicio)

        reiniciar = input("¿Deseas calcular nuevos servicios? (S/N): ").strip()
        while not (respuesta_positiva(reiniciar) or respuesta_negativa(reiniciar)):
            reiniciar = input("Respuesta no válida. ¿Deseas calcular nuevos servicios? (S/N): ").strip()
        if respuesta_negativa(reiniciar):
            break


if __name__ == "__main__":
    main()




