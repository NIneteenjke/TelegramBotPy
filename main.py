import random
import telebot
#1895493503:AAGroC6poVO6yp1JI-CeWuLqfP0WArNBKEY
bot = telebot.TeleBot("1895493503:AAGroC6poVO6yp1JI-CeWuLqfP0WArNBKEY")

Bot_configcomp={
'comp':[
'Мне нравится твой стиль',
'Твой смех очаровывает!',
'С тобой гораздо интереснее общаться, чем с моими сверстниками,ботами)',
'У тебя всегда самые лучшие идеи',
'С тобой я могу говорить обо всем'
]
}
Bot_configfailcomp={
'failurecomp':[
'Ты все равно прекрасный человек, удачи тебе!',
'Хорошо! У тебя обязательно все получится, хорошего тебе дня!',
'Ну ладно( Желаю тебе счастья!'
]
}


compliment=Bot_configcomp['comp']
failurecompliment=Bot_configfailcomp['failurecomp']

@bot.message_handler (commands=['start','help', 'старт'])
def send_welcome(message):
    bot.reply_to(message, "Привет, для того чтоб получить комплимент, напишите: Хочу! или если тебе это не надо напиши: Не хочу!")

@bot.message_handler (func=lambda m: True)
def echo_all(message):
    if message.text=="Хочу!":
        bot.reply_to(message, random.choice(compliment))
        #bot.reply_to(message, "Не переставай улыбаться, твоя улыбка обворожительна!")
    elif message.text=="Не хочу!":
        bot.reply_to(message, random.choice(failurecompliment))
        #bot.reply_to(message, "Ты все равно прекрасный человек, удачи тебе!")
bot.polling()



