#!/usr/bin/env/python3
# Este archivo Python usa la siguiente codificación: utf-8

# ===== #
# Edu Olivares
# Doctors Eye: https://github.com/BullsEye0
# Sitio web: http://www.hipotesi.org
# ===== #

# ===== #
# Creado el 01/09/2020 | Copyright (c) 2020 Edu olivares.
# ===== #

########################################################################

# Un aviso para todos los nerds y n00bs ...
# ¡Si copia el trabajo del desarrollador, no lo convertirá en un hacker ..!
# Respeta a todos los desarrolladores, hacemos esto porque es divertido ...

########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Dorks Eye v1.0


if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Dorks Eye Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDorks Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "[1;31m"
    CBLUE2 = "[1;34m"
    ENDC = "[1;30m"


banner = ("""

 _______    ______     ______ .___________.  ______        _______.    _______ ____    ____  _______
|       \  /  __  \   /      ||           | /  __  \      /       |   |   ____|\   \  /   / |   ____|
|  .--.  ||  |  |  | |  ,----'`---|  |----`|  |  |  |    |   (----`   |  |__    \   \/   /  |  |__
|  |  |  ||  |  |  | |  |         |  |     |  |  |  |     \   \       |   __|    \_    _/   |   __|
|  '--'  ||  `--'  | |  `----.    |  |     |  `--'  | .----)   |      |  |____     |  |     |  |____
|_______/  \______/   \______|    |__|      \______/  |_______/       |_______|    |__|     |_______| v1.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  Edu Olivares | Hipotesi
                Github:  https://github.com/Hipotesi
                Website: http://www.hipotesi.org \n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHola, quieres jugar a un juego..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] ¿Le gustaria guardar la salida en un archivo? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] Interrupción de usuario detectada..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Me gusta verte.. Hackear \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Dale un nombre al archivo: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Guardado omitido...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Ingrese la consulta de búsqueda del Doctor: ")
        amount = input("[+] Ingrese el número de sitios web para mostrar: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Interrupción de usuario detectada..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Me gusts verte.. Hackear \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Hecho... Saliendo...")
    print ("\n\t\t\t\t\033[34mDoctors Eye\033[0m")
    print ("\t\t\033[1;91m[!] Me gusta verte.. Hackear \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
