import math


def volume_formulas(figure, radius, high):

    if figure == 1:
        volume = math.pi * radius**2 * high
    elif figure == 2:
        volume = math.pi * radius**2 * high / 3
    else:
        volume = (4 * math.pi * radius**2) / 3

    return volume


def volume_calculator(figure):
    if figure == 1:
        fig = " cilindro"
    elif figure == 2:
        fig = " cono"
    else:
        fig = "a esfera"

    radius = float(
        input(f"""
        🤓🤓🤓
    Okey, así que un{fig}, eh?
    Bueno, dime su radio:


    """))

    if figure == 3:
        high = None
    else:
        high = float(
            input("""
        🤓🤓🤓
    Vamos muy bien,
    Solo me falta la altura:


    """))

    volume = volume_formulas(figure, radius, high)

    return volume


def run():
    figure = 4
    while figure > 3 or figure < 1:
        figure = int(
            input("""
        🤓🤓🤓
    Bienvenido humano,
    ¿listo para calcular?

    Elije una figura:
    1. Cilindro
    2. Cono
    3. Esfera

    """))

        volume = round(volume_calculator(figure), 2)
        print(f"""
        🤓🤓🤓
    Aquí está el volumen aproximado
    de tu maraviillosa figura...
        
        {volume}m³

    Vuelve pronto !!
    ༼ つ ◕_◕ ༽つ
    """)


if __name__ == '__main__':
    run()