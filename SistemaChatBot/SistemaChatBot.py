from Bots.Bot import Bot
import PySimpleGUI as sg
from assets.interface import Interface


class SistemaChatBot:
    def __init__(self, nomeEmpresa: str, lista_bots: list[Bot], janela: Interface):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise TypeError('Um objeto da lista de bots não é do tipo Bot')
                
        self.__lista_bots = lista_bots
        self.__bot: Bot
        self.__over = False
        self.janela = janela
    
    def boas_vindas(self) -> str:
        return f'Bem vindo ao Sistema de Chatbots da {self.__empresa}! \n'

    def mostra_menu(self) -> str:
        s= f'Nossos bots disponíveis no momento são: \n'
        for x in range(len(self.__lista_bots)):
            s += f'{x}- Bot: {self.__lista_bots[x].nome}. Mensagem de apresentação: {self.__lista_bots[x].apresentacao()}. \n'
        s += 'Digite o número do bot com que você quer conversar! \n'
        return s
    
    def escolhe_bot(self, indice):
        self.__bot = self.__lista_bots[int(indice)]

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()

    def le_envia_comando(self, indice: int) -> str: #fazer com que essa função agora receba um valor quando chamada, e não exija um input
        if indice == '-1':
            self.__over=True
            return ''

        f=''
        try :
            comando = self.__bot.get_comando(indice)
        except IndexError as e:
            return (f'{str(e)} \n')

        f+=f'Você disse: {comando.mensagem} \n'
        f+=f'Eu te respondo: {comando.getRandomResposta()} \n'
        return f

    def inicio(self) -> None:
        janela = sg.Window(self.janela.title, self.janela.layout, font=self.janela.font, return_keyboard_events=True, finalize=True)
        janela.Element('bot').Update(self.boas_vindas()+self.mostra_menu())
        while True:
            evento, valores= janela.read()
            if evento== sg.WIN_CLOSED:
                self.__over = True
                break
            elif  evento == 'Enviar':
                self.escolhe_bot(valores['user'])
                break

        janela.Element('bot').Update(self.__bot.boas_vindas()+self.mostra_comandos_bot())

        while not self.__over:
            evento, valores= janela.read()
            if evento== sg.WIN_CLOSED:
                self.__over = True
                break
            elif evento == 'Enviar':
                janela.Element('bot').Update(self.le_envia_comando(valores['user']) + self.mostra_comandos_bot())

        print(self.__bot.despedida())
