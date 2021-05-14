def is_in_range(upper_limit, lower_limit, comparison_number):
    if comparison_number in range(lower_limit, upper_limit):
        return True
    else:
        return False


def run():
    print("""
Hi!!
ready to start?
                (❁´◡`❁)""")
    upper_limit = int(
        input("""
Input one number:
                  (☞ﾟヮﾟ)☞
"""))
    lower_limit = int(
        input("""
Input another number, smaller than the last one:
                                                 ☜(ﾟヮﾟ☜)
"""))

    cont = 0
    while cont < 1:
        comparison_number = int(
            input("""
It's time to try with the last one:
                                    ༼ つ ◕_◕ ༽つ
"""))
        result = is_in_range(upper_limit, lower_limit, comparison_number)

        if result:
            print(f"""
Well done  (╯°□°）╯︵ ┻━┻

    🔥  🔥  🔥 {comparison_number} 🔥  🔥  🔥""")
            cont = 1
        else:
            print(f"""
Try again  ¯\_(ツ)_/¯

    🌊  🌊  🌊 {comparison_number} 🌊  🌊  🌊""")


if __name__ == '__main__':
    run()