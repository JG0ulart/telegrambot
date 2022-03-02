import telebot
from temperatura import temperatura_city
from consulta import verificar_connection
from cotacao import cotacao


bot = telebot.TeleBot("TOKEN BOT HERE")
@bot.message_handler(commands=['cotacao'])
def cotacaohoje(mensagem):
    cotacaohj = cotacao()
    bot.reply_to(mensagem, cotacaohj)

@bot.message_handler(commands=['tempoarcos'])
def tempoarcos(mensagem):
    city_temp = temperatura_city("Arcos")
    bot.reply_to(mensagem, city_temp)

@bot.message_handler(commands=['tempojapa'])
def tempojapa(mensagem):
    city_temp = temperatura_city("Japaraiba")
    bot.reply_to(mensagem, city_temp)


@bot.message_handler(commands=['status'])
def status(mensagem):
    status_connect = verificar_connection("4857544381D1689C")
    bot.reply_to(mensagem, status_connect)

def verificar_mensagem(mensagem):
    return True

@bot.message_handler(func=verificar_mensagem)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /tempoarcos Temperatura na cidade de Arcos
    /tempojapa  Temperatura na cidade de Japaraiba
    /status     Status da conexão do cliente
    /cotacao    Cotação do dolar, euro e bitcoin de hoje.
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()