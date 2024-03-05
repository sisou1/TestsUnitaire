from src.detecteurPalindrome import DétecteurPalindrome
from .langueStub import LangueStub


class DétecteurPalindromeBuilder:
    __langue = LangueStub()

    def build(self):
        return DétecteurPalindrome(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self