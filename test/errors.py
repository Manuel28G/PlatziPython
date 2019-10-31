

countries = {
    'mexico':122,
    'colombia':49,
    'argentina':43,
    'chile':18,
    'peru':31,
}

while True:
    country = str(raw_input('Escribe el nombre de un pais: ').lower())
    try:
        print('La poblacion de {} es de {} millones'.format(country,countries[country]))
    except KeyError:
        print('No tenemos la poblacion de {}'.format(country))
