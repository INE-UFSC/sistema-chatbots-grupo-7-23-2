import random


class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, mensagem, respostas = []):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    # get id
    @property
    def id(self) -> int:
        return self.__id

    # get mensagem
    @property
    def mensagem(self) -> str:
        return self.__mensagem

    # retorna uma resposta aleatória
    def getRandomResposta(self) -> str:
        random_resp = random.choice(self.__respostas)
        return random_resp

    # adiciona resposta
    def addResposta(self, resposta: str) -> None:
        self.__respostas.append(resposta)
    # remove resposta (opcional)
    def delResposta(self, resposta: str) -> None:
        self.__respostas.remove(resposta)

