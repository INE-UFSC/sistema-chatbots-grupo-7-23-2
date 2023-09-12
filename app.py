#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotGoodVibe import BotGoodVibe
from Bots.BotSadBoy import BotSadBoy

lista_bots = [BotZangado("Yoda"), BotGoodVibe('Marley'), BotSadBoy('Johnny')]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
