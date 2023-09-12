from Bots.Bot import Bot

class BotSadBoy(Bot):
    def __init__(self, nome: str):
        comandos = [ 
            ('Olá!','Estou triste ;-;.'),
            ('Me conte sobre você', f'Eu sou o {nome} vivo sad e triste.'),
            ('Como você está?', 'Estou triste hoje, pois não estou feliz.'),
            ('Você quer ser meu amigo?', 'Se a tristeza permitir, podemos sim ser amigos.')
        ]

        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Opa! Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Oi, tudo bem?'

    def despedida(self) -> str:
        return 'Flw, espero que você não fique tão sad quanto eu.'
