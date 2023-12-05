from datetime import datetime

maintenant = datetime.now()
if maintenant.hour < 18:
    print("Bonjour il est : " + maintenant.strftime("%H:%M:%S"))
else:
    print("Bonsoir il est : " + maintenant.strftime("%H:%M:%S"))

x = input("ça va renvoyer ce que vous écrivez a l'envers :")


def lenvers(phrase, result):
    if phrase != "":
        return lenvers(phrase[:-1], result + phrase[-1])
    else:
        return result

print(lenvers(x, ""))
if x == lenvers(x, ""):
    print("bien dis !")


if x == "exit":
    if maintenant.hour < 18:
        print("aurevoir il est : " + maintenant.strftime("%H:%M:%S"))
    else:
        print("aurevoir il est : " + maintenant.strftime("%H:%M:%S"))
