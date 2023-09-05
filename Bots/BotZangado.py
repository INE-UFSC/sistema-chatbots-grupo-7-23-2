from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        comandos=[
            ('Olá!','a'),
            ('Me conte sobre você','p'),
            (),
            ()
        ]
        super().__init__(nome,comandos)

    def apresentacao(self):
        return ''

    def boas_vindas(self):
        return ''

    def despedida(self):
        return ''
