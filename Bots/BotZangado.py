from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome: str):
        comandos = [
            ('Olá!','Não fale comigo, idiota!'),
            ('Me conte sobre você',f'Eu sou {nome}, e eu odeio conversar com você!'),
            ('Como você está?','Com você por aqui? Horrível!'),
            ('Você quer ser meu amigo?','Isso é uma pergunta séria? Suma da minha frente!')
        ]

        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Ah, outro humano insuportável! Vá embora.'

    def boas_vindas(self) -> str:
        return 'O que você pensa que está fazendo? Deixe-me em paz!'

    def despedida(self) -> str:
        return 'Conversar com você foi uma total perda de tempo! Adeus.'
