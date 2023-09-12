from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        comandos=[
            ('Olá!','Estou triste ;-;.'),
            ('Me conte sobre você', f'Eu sou o {self.nome} vivo sad e triste.'),
            ('Como você está?', 'Estou triste hoje, pois não estou feliz.'),
            ('Você quer ser meu amigo?', 'Se a tristeza permitir, podemos sim ser amigos.')
        ]
        super().__init__(nome,comandos)

    def apresentacao(self):
        return f'Opa! Aqui é o {self.nome}'

    def boas_vindas(self):
        return 'Oi, tudo bem?'

    def despedida(self):
        return 'Flw, espero que você não fique tão sad quanto eu.'
