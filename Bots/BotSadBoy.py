from Bots.Bot import Bot


class BotSadBoy(Bot):
    def __init__(self, nome: str):
        super().__init__(nome, 'BotSadBoy')

    def apresentacao(self) -> str:
        return f'Opa! Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Oi, tudo bem? \n'

    def despedida(self) -> str:
        return 'Flw, espero que você não fique tão sad quanto eu. \n'

