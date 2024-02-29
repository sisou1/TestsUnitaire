import os


class DétecteurPalindrome:
<<<<<<< HEAD
    def __init__(self, langue):
        self.__langue = langue

    def détecter(self, chaîne):
        miroir = chaîne[::-1]

        début = (self.__langue.saluer()
=======
    @classmethod
    def détecter(cls, chaîne):
        miroir = chaîne[::-1]

        début = ('Bonjour'
>>>>>>> TestsUnitaire-Fabien/master
                 + os.linesep
                 + miroir
                 + os.linesep)

<<<<<<< HEAD
        return ((début + self.__langue.féliciter()
                if chaîne == miroir
                else début)
                + "Au revoir")
=======
        return (début + "Bien dit !" if chaîne == miroir else début) + "Au revoir"
>>>>>>> TestsUnitaire-Fabien/master
