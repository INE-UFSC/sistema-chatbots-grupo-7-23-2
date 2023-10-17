from abc import ABC, abstractmethod
from comando import Comando

class Bot(ABC):
    def __init__(self, nome: str, comandos: list[Comando]):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    def mostra_comandos(self) -> None:
        f=''
        for comando in self.__comandos:
            f+=f'{comando.id} - {comando.mensagem} \n'
        return f
    
    def get_comando(self, id: int):
        for comando in self.__comandos:
            if comando.id == id:
                return comando
        raise IndexError('Comando Inválido!')

    @abstractmethod
    def apresentacao(self) -> None:
        pass

    @abstractmethod
    def boas_vindas(self) -> str:
        pass
    
    @abstractmethod
    def despedida(self) -> None:
        pass
