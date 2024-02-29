import os
import unittest

from src.detecteurPalindrome import DétecteurPalindrome

cas_test_non_palindrome = ['test', 'epsi']


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        for chaîne in cas_test_non_palindrome:
            with self.subTest(chaîne):
                # QUAND je demande si elle est un palindrome
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS j'obtiens cette chaîne en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_bien_dit(self):
        # ETANT DONNE un palindrome
        palindrome = 'radar'

        # QUAND on le fournit au détecteur
        résultat = DétecteurPalindrome.détecter(palindrome)

        # ALORS on obtient cette chaîne suivie de "Bien dit !"
        attendu = palindrome + os.linesep + 'Bien dit !'
        self.assertIn(attendu, résultat)

    def test_absence_bien_dit(self):
        # ETANT DONNE un non-palindrome
        for chaîne in cas_test_non_palindrome:
            with self.subTest(chaîne):
                # QUAND on le fournit au détecteur
                résultat = DétecteurPalindrome.détecter(chaîne)

                # ALORS "Bien dit !" n'apparaît pas
                self.assertNotIn('Bien dit !', résultat)

    def test_bonjour(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND je demande si elle est un palindrome
        résultat = DétecteurPalindrome.détecter(chaîne)

        # ALORS la première ligne est "Bonjour"
        premiere_ligne = résultat.split(os.linesep)[0]
        self.assertEqual('Bonjour', premiere_ligne)

    def test_au_revoir(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND je demande si elle est un palindrome
        résultat = DétecteurPalindrome.détecter(chaîne)

        # ALORS la dernière ligne est "Au revoir"
        lignes = résultat.split(os.linesep)
        dernière_ligne = lignes[-1]
        self.assertEqual('Au revoir', dernière_ligne)


if __name__ == '__main__':
    unittest.main()