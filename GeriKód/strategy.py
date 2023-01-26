from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, a: int, b: int, questionNum: int):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class Ă–sszeadĂˇs(Strategy):
    def do_algorithm(self, a: int, b: int, questionNum: int):
        print(questionNum, ". kĂ©rdĂ©s:", a, " + ", b, "= ")
        solution = int(input(""))
        if solution == a + b:
            print("Helyes vĂˇlasz!")
            return True
        else:
            print("Rossz vĂˇlasz!")
            return False


class KivonĂˇs(Strategy):
    def do_algorithm(self, a: int, b: int, questionNum: int):
        print(questionNum, ". kĂ©rdĂ©s:", a, " - ", b, "= ")
        solution = int(input(""))
        if solution == a - b:
            print("Helyes vĂˇlasz!")
            return True
        else:
            print("Rossz vĂˇlasz!")
            return False


class SzorzĂˇs(Strategy):
    def do_algorithm(self, a: int, b: int, questionNum: int):
        print(questionNum, ". kĂ©rdĂ©s:", a, " * ", b, "= ")
        solution = int(input(""))
        if solution == a * b:
            print("Helyes vĂˇlasz!")
            return True
        else:
            print("Rossz vĂˇlasz!")
            return False


class OsztĂˇs(Strategy):
    def do_algorithm(self, a: int, b: int, questionNum: int):
        print(questionNum, ". kĂ©rdĂ©s:", a, " / ", b, "= ")
        solution = int(input(""))
        if solution == a / b:
            print("Helyes vĂˇlasz!")
            return True
        else:
            print("Rossz vĂˇlasz!")
            return False
