#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotGoodVibe import BotGoodVibe
from Bots.BotSadBoy import BotSadBoy
from assets.interface import Interface, layout

lista_bots = [BotZangado("Yoda"), BotGoodVibe('Marley'), BotSadBoy('Johnny')]

window= Interface('Sistema Chatbot', layout, ('Helvetica',14))
sys = scb.SistemaChatBot("CrazyBots", lista_bots, window)
sys.inicio()
