def run():
    contador = 0

    while contador == 0:
        dato1 = float(input("¿Cuál es la altura del triángulo? "))
        if dato1 >= 1:
            print('exelente, siguiente pregunta')
            contador += 1

    while contador == 1:
        dato2 = float(input("¿Cuál es la base del triángulo? "))
        if dato2 >= 1:
            print('bien, continuemos')
            contador += 1

    area = dato1 * dato2 / 2
    area = str(area)
    print("Acá tenés el área, dejate de romper las bo... " + area)


if __name__ == '__main__':
    run()