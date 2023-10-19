from Bots.Bot import Bot, Comando

class BotGoodVibe(Bot):
    def __init__(self, nome: str):
        comandos = [ Comando('1','Olá!',['Eae, brother!','Opa, tudo sussa?','Fala ae bro, mó vibe!']), 
                    Comando('2','Me conte sobre você',[f'Eu sou o {nome}, adoro surfar e me conectar com a natureza.','Já quiz ser porgramador uma vez, mas hoje vivo outra vibe.','Moro lá no Campeche, prefiro sentir a energia da natureza.']),
                    Comando('3','Como você está?',['Estou sempre bem, sempre na good vibe.','Tô na paz mano, como sempre.','Tô tranquilão, susse.']),
                    Comando('4','Você quer ser meu amigo',['Bora, quer surfar um dia desses?', 'Claroo broww, venha para o mundo good vibe.' ,'Tu já é meu parça, não tenho inimigos.']) ]
        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Tranquilasso? Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Eaii mano, tudo good? \n'

    def despedida(self) -> str:
        return 'Flw, fique com Jah! \n'
