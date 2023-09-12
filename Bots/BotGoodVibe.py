from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        comandos=[
            ('Olá!','Oii'),
            ('Me conte sobre você','p'),
            (),
            ()
        ]
        super().__init__(nome,comandos)

    def apresentacao(self):
        return f'Tranquilasso? Aqui é o {self.nome}'

    def boas_vindas(self):
        return 'Eaii mano, tudo good?'

    def despedida(self):
        return 'Flw, fique com Jah!'
