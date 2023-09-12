from Bots.Bot import Bot

class BotGoodVibe(Bot):
    def __init__(self, nome: str):
        comandos = [ 
            ('Olá!','Tô tranquilão, susse.'),
            ('Me conte sobre você', f'Eu sou o {nome} adoro surfar e me conectar com a natureza.'),
            ('Como você está?', 'Estou sempre bem, sempre na good vibe.'),
            ('Você quer ser meu amigo?', 'Claroo broww, venha para o mundo good vibe.')
        ]

        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Tranquilasso? Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Eaii mano, tudo good?'

    def despedida(self) -> str:
        return 'Flw, fique com Jah!'
