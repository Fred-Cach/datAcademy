import getpass

OPTION_POOL = [3, 1, 2, 3, 1]


def who_win(player_1, player_2):
    odds = OPTION_POOL[player_1 - 1:player_1 + 2]
    p1_ind = odds.index(player_1)
    p2_ind = odds.index(player_2)

    win = "Jugador/a 1" if p1_ind > p2_ind else "Nadie" if p1_ind == p2_ind else "Jugador/a 2"

    return win


def run():

    print("""
¡¡ QUE COMIENZE EL JUEGO !!
                                (╯°`□´°）╯︵ ┻━┻
                                                    🔥  🔥  🔥  🔥""")

    cont1 = 0
    cont2 = 0
    while cont1 < 2 and cont2 < 2:

        player_1 = int(
            getpass.getpass("""
〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰
Elige sabiamente, jugador 1...
                               y no olvides tapar el teclado !! (⌐■_■)
1. Piedra
2. Papel
3. Tijera
"""))
        player_2 = int(
            getpass.getpass("""
〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰
Elige sabiamente, jugador 2...
                               y no olvides tapar el teclado !! (⌐■_■)
1. Piedra
2. Papel
3. Tijera
            """))

        win = who_win(player_1, player_2)

        if win.count("1") != 0:
            cont1 += 1
        if win.count("2") != 0:
            cont2 += 1

        print(f"""
⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  ⚡  
Esta ronda se la lleva... {win} 🎈
                                    pero esto aún no ha terminado...
                                                                     ᓚᘏᗢ
""")
    else:
        print(f"""
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

ARRODÍLLENSE ANTE LA MENTE MAESTRA DE {win.upper()} (╯°`□´°）╯︵ ┻━┻´

🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️🧎‍♂️🧎‍♀️"""
              )


if __name__ == '__main__':
    run()