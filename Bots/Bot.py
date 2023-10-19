from abc import ABC, abstractmethod
import json

from comando import Comando


class Bot(ABC):
    def __init__(self, nome: str, tipo_bot: str):
        self.__nome = nome

        with open('./assets/bot_data.json', 'r') as file:
            comandos_bots = json.load(file)

        self.__comandos: list[Comando] = []
        for i, (mensagem, respostas) in enumerate(comandos_bots[tipo_bot]['commands'].items()):
            for k in range(len(respostas)):
                respostas[k] = respostas[k].replace('{name}', self.__nome)

            self.__comandos.append(Comando(i + 1, mensagem, respostas))

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    def mostra_comandos(self) -> str:
        f=''
        for comando in self.__comandos:
            f+=f'{comando.id} - {comando.mensagem} \n'
        return f

    def get_comando(self, id: int):
        if not isinstance(id, int):
            id = int(id)

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
