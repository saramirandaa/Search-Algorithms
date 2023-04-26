###############################
###############################
##### Informacion general #####
'''
    Proyecto: Calcular la heuristica de linea recta entre dos ciudades
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Ari Barrera
    22-marzo-2023
    Versión 0.1.0

    El presente codigo calcula la distancia euclideana entre dos ciudades 
    de los Estados Unidos Mexicanos, utilizando las coordenadas geograficas 
    de un par de ciudades. Esta distancia es utilizada para obtener los
    valores de la heuristica para el proyecto del 2do Parcial de la materia.

    Ejecucion del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python get_euclidean_distance.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
    
    Entradas:
        1) El nombre de una ciudad en Mexico que deseemos sea el destino
    
    Salidas:
        1) Imprime en pantalla los valores calculados de la heuristica de distancia de linea recta
'''

###############################
###############################
##### Dependencias #####
import math

###############################
###############################
##### Variables Globales #####

# diccionario con el nombre de las ciudades contenidas en el grafo y sus correspondientes coordenadas
#   geograficas en formato de latitud y longitud
cities_coordinates = {
    'CANCUN': (21.1213285,-86.9192738)
    ,'VALLADOLID': (20.688114,-88.2204456)
    ,'FELIPECARRILLOPUERTO': (19.5778903,-88.0630853)
    ,'CAMPECHE': (19.8305682,-90.5798365)
    ,'MERIDA': (20.9800512,-89.7029587)
    ,'CIUDADDELCARMEN': (18.6118375,-91.8927345)
    ,'CHETUMAL': (18.5221567,-88.3397982)
    ,'VILLAHERMOSA': (17.9925264,-92.9881407)
    ,'TUXTLA': (16.7459857,-93.1996103)
    ,'FRANCISCOESCARCEGA': (18.6061556,-90.8176486)
    ,'ACAYUCAN': (17.951096,-94.9306961)
    ,'TEHUANTEPEC': (16.320636,-95.27521)
    ,'ALVARADO': (18.7760455,-95.7731952)
    ,'OAXACA': (17.0812951,-96.7707511)
    ,'PUERTOANGEL': (15.6679974,-96.4933733)
    ,'IZUCARDEMATAMOROS': (18.5980563,-98.5076767)
    ,'TEHUACAN': (18.462191,-97.4437333)
    ,'PINOTEPANACIONAL': (16.3442895,-98.1315923)
    ,'CUERNAVACA': (18.9318685,-99.3106054)
    ,'PUEBLA': (19.040034,-98.2630056)
    ,'ACAPULCO': (16.8354485,-99.9323491)
    ,'CIUDADDEMEXICO': (19.3898319,-99.7180148)
    ,'IGUALA': (18.3444,-99.5652232)
    ,'CIUDADALTAMIRANO': (18.3547491,-100.6817619)
    ,'CORDOBA': (18.8901707,-96.9751108)
    ,'CHILPANCINGO': (17.5477072,-99.5324349)
    ,'TLAXCALA': (19.4167798,-98.4471127)
    ,'PACHUCADESOTO': (20.0825056,-98.8268184)
    ,'QUERETARO': (20.6121228,-100.4802576)
    ,'TOLUCADELERDO': (19.294109,-99.6662331)
    ,'ZIHUATANEJO': (17.6405745,-101.5601369)
    ,'VERACRUZ': (19.1787635,-96.2113357)
    ,'TUXPANDERODRIGUEZCANO': (20.9596561,-97.4158767)
    ,'ATLACOMULCO': (19.7980152,-99.89317)
    ,'SALAMANCA': (20.5664927,-101.2176511)
    ,'SANLUISPOTOSI': (22.1127046,-101.0261099)
    ,'PLAYA AZUL': (17.9842581,-102.357616)
    ,'TAMPICO': (22.2662251,-97.939526)
    ,'GUANAJUATO': (21.0250928,-101.3296402)
    ,'MORELIA': (19.7036417,-101.2761644)
    ,'GUADALAJARA': (20.6737777,-103.4054536)
    ,'AGUASCALIENTES': (21.8857199,-102.36134)
    ,'ZACATECAS': (22.7636293,-102.623638)
    ,'DURANGO': (24.0226824,-104.7177652)
    ,'COLIMA': (19.2400444,-103.7636273)
    ,'MANZANILLO': (19.0775491,-104.4789574)
    ,'CIUDADVICTORIA': (23.7409928,-99.1783576)
    ,'TEPIC': (21.5009822,-104.9119242)
    ,'HIDALGODELPARRAL': (26.9489283,-105.8211168)
    ,'MAZATLAN': (23.2467283,-106.4923175)
    ,'SOTOLAMARINA': (23.7673729,-98.2157573)
    ,'MATAMOROS': (25.8433787,-97.5849847)
    ,'MONTERREY': (25.6487281,-100.4431819)
    ,'CHIHUAHUA': (28.6708592,-106.2047036)
    ,'TOPOLOBAMPO': (25.6012747,-109.0687891)
    ,'CULIACAN': (24.8049008,-107.4933545)
    ,'REYNOSA': (26.0312262,-98.3662435)
    ,'MONCLOVA': (26.907775,-101.4940069)
    ,'CIUDADJUAREZ': (31.6538179,-106.5890206)
    ,'JANOS': (30.8898127,-108.208458)
    ,'CIUDADOBREGON': (27.4827355,-110.0844111)
    ,'TORREON': (25.548597,-103.4719562)
    ,'OJINAGA': (29.5453292,-104.4305246)
    ,'NUEVOLAREDO': (27.4530856,-99.6881218)
    ,'AGUAPRIETA': (31.3115272,-109.5855873)
    ,'GUAYMAS': (27.9272572,-110.9779564)
    ,'PIEDRASNEGRAS': (28.6910517,-100.5801829)
    ,'SANTAANA': (30.5345457,-111.1580567)
    ,'HERMOSILLO': (29.082137,-111.059027)
    ,'MEXICALI': (32.6137391,-115.5203312)
    ,'TIJUANA': (32.4966818,-117.087892)
    ,'SANFELIPE': (31.009535,-114.8727296)
    ,'ENSENADA': (31.8423096,-116.6799816)
    ,'SANQUINTIN': (30.5711324,-115.9588544)
    ,'SANTAROSALIA': (27.3408761,-112.2825762)
    ,'SANTODOMINGO': (25.3487297,-111.9975909)
    ,'LAPAZ': (24.1164209,-110.3727673)
    ,'CABOSANLUCAS': (22.8962253,-109.9505077)
}

###############################
###############################
##### Funciones o Clases de Apoyo #####

# calcula la distancia euclideana entre dos ciudades por medio de las coordenas geograficas
# entrada:
#   origin = tupla que contiene la latitud y longitud de la ciudad de origen
#   goal = tupla que contiene la latitud y longitud de la ciudad destino
# salida:
#   regresa el valor numerico de la distancia euclideana redondeado
def euclidean_distance_between_cities(origin,goal):
    # calcula la distancia euclideana entre dos ciudades y regresa su valor redondeado
    return round(math.dist(origin,goal))

###############################
###############################
##### Funciones o Clases Principales #####

# calcula la heuristica para una ciudad objetivo
# entrada:
#   goal_city = nombre de la ciudad objetivo
# salida:
#   regresa un diccionario con los valores numericos de la heuristica para la ciudad objetivo
#       introducida por el usuario
def calcular_heuristica_distancia_de_linea_recta(goal):
    # obtiene las coordenadas de la ciudad destino
    coordinate_goal = cities_coordinates[goal.upper()]

    # diccionario que contendra los valores de la heuristica de distancia de linea recta para
    # la ciudad de destino ingresada
    heuristic_linear_straight_distance = {}

    # itera a traves de todas las ciudades disponibles en el grafo
    for city_origin, coordinate_origin in cities_coordinates.items():
        # obtiene la distancia euclideana de las dos ciudades correspondientes
        euclidean_distance = euclidean_distance_between_cities(coordinate_origin,coordinate_goal)
        # agrega al diccionario de heuristica la ciudad de origen y su valor de distancia de linea recta
        heuristic_linear_straight_distance[city_origin] = euclidean_distance
    
    # regresa el diccionario con los valores de la heuristica para la ciudad objetivo correspondiente
    return heuristic_linear_straight_distance


    
# funcion que encapsula la estructura general del programa
# entrada:
#   sin parametros
# salida:
#   imprime en pantalla los valores calculados de la heuristica de distancia de linea recta para las
#   ciudades del grafo de Mexico
def get_heuristic(goal_city):
    
    # manda llamar a la funcion para calcular la heuristica
    hlsd = calcular_heuristica_distancia_de_linea_recta(goal_city)
    
    # imprime en pantalla la heuristica correspondiente
    print('La heuristica para la ciudad objetivo {} es {}'.format(goal_city,hlsd))
    print(hlsd['CANCUN'])

# se manda llamar la funcion principal
