from abc import ABC, abstractmethod
import json

from comando import Comando

class Bot(ABC):
    def __init__(self, nome: str, comandos: list[Comando]):
        with open('./assets/bot_data.json', 'r') as file:
            a = json.load(file)
            print(a)

        # for 

        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    def mostra_comandos(self) -> None:
        for comando in self.__comandos:
            print(f'{comando.id} - {comando.mensagem}')
    
    def get_comando(self, id: int):
        for comando in self.__comandos:
            if comando.id == id:
                return comando
        raise IndexError('Comando Inválido!')

    @abstractmethod
    def apresentacao(self) -> None:
        pass

    @abstractmethod
    def boas_vindas(self) -> None:
        pass
    
    @abstractmethod
    def despedida(self) -> None:
        pass
