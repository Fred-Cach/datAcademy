def run():

    measure = input("¿Buscas cambiar kilómetros o millas?: ")
    if measure != "millas":
        kil = float(input("¿Cuántos kilómetros?: "))
        valor_milla = 1.609344
        millas = kil * valor_milla
        millas = round(millas, 2)
        millas = str(millas)
        print("Son un total de " + millas + " millas.")
    else:
        mill = float(input("¿ Cuántos millas?: "))
        valor_km = 1 / 1.609344
        kilom = mill * valor_km
        kilom = round(kilom, 2)
        kilom = str(kilom)
        print("Son un total de " + kilom + " kilómetros.")


if __name__ == '__main__':
    run()
