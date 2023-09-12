from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa: str, lista_bots: list[Bot]):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise TypeError('Um objeto da lista de bots não é do tipo Bot')
                
        self.__lista_bots = lista_bots
        self.__bot: Bot
        self.__over = False
    
    def boas_vindas(self) -> None:
        print(f'Bem vindo ao Sistema de Chatbots da {self.__empresa}!')

    def mostra_menu(self) -> None:
        print('Nossos bots disponíveis no momento são:')
        for x in range(len(self.__lista_bots)):
            print(f'{x}- Bot: {self.__lista_bots[x].nome}. Mensagem de apresentação: {self.__lista_bots[x].apresentacao()}.')
    
    def escolhe_bot(self):
        indice_bot = int(input('Digite o número do bot com que você quer conversar:'))
        self.__bot = self.__lista_bots[indice_bot]

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        indice_comando = int(input('Digite o comando desejado (ou -1 para sair):'))
        if indice_comando == -1:
            self.__over=True
            return

        else:
            print(f'Você disse: {self.__bot.get_comando(indice_comando)[0]}')
            self.__bot.executa_comando(indice_comando)

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        while not self.__over:
            self.mostra_comandos_bot()
            self.le_envia_comando()

        print(self.__bot.despedida())
