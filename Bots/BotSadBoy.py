from Bots.Bot import Bot
from comando import Comando

class BotSadBoy(Bot):
    def __init__(self, nome: str):
        comandos = [ Comando('1','Olá!',[';-;','Oi... :(','Achei que você nunca fosse falar comigo...']), 
                    Comando('2','Me conte sobre você',[f'Eu sou o {nome}, vivo sad e triste.','Passo o dia na solidão do meu quarto, sozinho e sad ;-;.',f'Já fui mais alegre, mas esse era outro {nome} :(']),
                    Comando('3','Como você está?',['Estou triste ;-;.','Na bad, como sempre :(','Solitário...']),
                    Comando('4','Você quer ser meu amigo?',['Se eu deixar de ser o bot sozinho e sad, a empresa vai me demitir ;-;', 'Claro! Nunca tive um amigo antes :D' ,'Se a tristeza permitir, podemos sim ser amigos...']) ]
        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Opa! Aqui é o {self.nome}'

    def boas_vindas(self) -> str:
        return 'Oi, tudo bem? \n'

    def despedida(self) -> str:
        return 'Flw, espero que você não fique tão sad quanto eu. \n'
