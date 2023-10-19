from Bots.Bot import Bot
from comando import Comando

class BotZangado(Bot):
    def __init__(self, nome: str):
        comandos = [ Comando('1','Olá!',[';-;','Oi... :(','Achei que você nunca fosse falar comigo...']), 
                    Comando('2','Me conte sobre você',[f'Eu sou o {nome} vivo sad e triste.','Passo o dia na solidão do meu quarto, sozinho e sad ;-;.',f'Já fui mais alegre, mas esse era outro {nome} :(']),
                    Comando('3','Como você está?',['Estou triste ;-;.','Horrí','Tô tranquilão, susse.']),
                    Comando('4','Você quer ser meu amigo?',['Se eu deixar de ser o bot sozinho e sad, a empresa vai me demitir ;-;', 'Claro! Nunca tive um amigo antes :D' ,'Se a tristeza permitir, podemos sim ser amigos...'])
        ]

        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return f'Ah, outro humano insuportável! Vá embora.'

    def boas_vindas(self) -> str:
        return 'O que você pensa que está fazendo? Deixe-me em paz! \n'

    def despedida(self) -> str:
        return 'Conversar com você foi uma total perda de tempo! Adeus. \n'


#('Olá!','Não fale comigo, idiota!'),
 #           ('Me conte sobre você',f'Eu sou {nome}, e eu odeio conversar com você!'),
  #          ('Como você está?','Com você por aqui? Horrível!'),
   #         ('Você quer ser meu amigo?','Isso é uma pergunta séria? Suma da minha frente!')