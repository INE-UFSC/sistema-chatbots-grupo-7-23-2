from Bots.Bot import Bot


class BotGoodVibe(Bot):
    def __init__(self, nome: str):
        super().__init__(nome, 'BotGoodVibe')

    def apresentacao(self) -> str:
        return f'Tranquilasso? Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Eaii mano, tudo good? \n'

    def despedida(self) -> str:
        return 'Flw, fique com Jah! \n'
