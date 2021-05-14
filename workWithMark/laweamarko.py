def run():
    dato1 = 0
    dato2 = 0

    while dato1 <= 0:
        dato1 = float(input("¿Cuál es la altura del triángulo? "))

    while dato2 <= 0:
        dato2 = float(input("¿Cuál es la base del triángulo? "))

    area = dato1 * dato2 / 2
    area = str(area)
    print("Acá tenés el área, dejate de romper las bo... " + area)


if __name__ == '__main__':
    run()