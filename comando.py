import random

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, mensagem, respostas = []):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    # get id
    @property
    def id(self):
        return self.__id

    # get mensagem
    @property
    def mensagem(self):
        return self.__mensagem

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        random_resp = random.choice(self.__respostas)
        return random_resp
    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)
    # remove resposta (opcional)
    def delResposta(self, resposta):
        self.__respostas.remove(resposta)