##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos:list[tuple[str]]):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome=nome

    def mostra_comandos(self):
        for i in range(len(self.__comandos)):
            print(f'{i}-{self.__comandos[i][0]}')
    
    def get_comando(self,indice):
        return self.__comandos[indice]
        

    def executa_comando(self,cmd):
        if cmd<=len(self.__comandos) and cmd>=1:
            print(f' E eu te respondo: {self.__comandos[cmd][1]}')
        else:
            print('Comando Inválido!') #mudardepois
    
    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
