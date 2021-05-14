def isosceles_chance(base, high):
    twin_side = (high **2 + (base/2) **2) **(1/2)

    return twin_side


def run():
    base = float(input("""
Hola! Caulcularé el área de tu triángulo! ╰(*°▽°*)╯

dime, cuál es su base? (╯°□°）╯︵ ┻━┻
    """))
    high = float(input("""
Oh, ya veo... y su altura? ༼ つ ◕_◕ ༽つ
    """))

    area = (base * high)/2
    isosceles_twin_side = isosceles_chance(base, high)
    
    area = str(area)
    isosceles_twin_side = str(isosceles_twin_side)

    print("""
Tu triángulo tiene un área de """ + area + """ y NO puede ser equilátero... ¯\_(ツ)_/¯

peeeeeero sí isósceles, siempre y cuando sus lados iguales midan """ + isosceles_twin_side + """. (⌐■_■)

... sino, simplemente será escaleno, compadre. (┬┬﹏┬┬)
""")


if __name__ == '__main__':
    run()