from abc import ABC, abstractmethod

class Bot(ABC):
    def __init__(self, nome: str, comandos:list[tuple[str]]):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    def mostra_comandos(self) -> None:
        for i in range(len(self.__comandos)):
            print(f'{i}-{self.__comandos[i][0]}')
    
    def get_comando(self, indice: int) -> tuple[str]:
        if indice >= 0 and indice < len(self.__comandos):
            return self.__comandos[indice]

        raise IndexError('Comando inválido')

    def executa_comando(self,cmd):
        if cmd >= 0 and cmd <= len(self.__comandos):
            print(f'E eu te respondo: {self.__comandos[cmd][1]}')
            return

        raise IndexError('Comando inválido')
    
    @abstractmethod
    def apresentacao(self) -> None:
        pass

    @abstractmethod
    def boas_vindas(self) -> None:
        pass
    
    @abstractmethod
    def despedida(self) -> None:
        pass
