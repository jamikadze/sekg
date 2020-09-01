import telebot
import pyodbc
from telebot import types

bot = telebot.TeleBot('1242843344:AAGNZivdNYLnw3q9Z4vSXMZih2qbZbL1PCU')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.19.5;'
                      'Database=Meters;'
                      'uid=sa;'
                      'pwd=Akay12345.'
                      )
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, Вас приветствует Бот Северэлектро, введите лицевой счет чтобы узнать баланс!')


@bot.message_handler(commands=['url'])
def start_message(message):
    # bot.send_message(message.chat.id,
    #                  'Круглосуточный Call-центр: 1209\n')
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на наш сайт", url="https://se.kg/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Круглосуточный Call-центр: 1209", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):


    str="SELECT cspot2,address1,address2,ybalance11 ,ybalance21,ybalance31,ccounter FROM Meters.dbo.All_call_spots  where cspot like '"+message.text+"'"
    cursor.execute(str)
    for row in cursor:
        print(row)
        if len(message.text) == 9:
            bot.send_message(message.chat.id, "Ф.И.О: "+row[0]+"\nАдрес: "+row[1]+" "+row[2]+"\n№ счетчика: "+row[6]+"\nБаланс: "+row[3]+"\nПеня: "+row[4]+"\nАкт нарушения: "+row[5])
        elif len(message.text) == 11:
            bot.send_message(message.chat.id, "Ф.И.О: " + row[0] + "\nАдрес: " + row[1] + " " + row[2] + "\n№ счетчика: " + row[6] + "\nБаланс: " + row[3] + "\nПеня: " + row[4] )
        elif(len(message.text) != 9 and len(message.text) != 11):
            bot.send_message(message.chat.id, "Введите л/счет правильно!!! ")


while True:
    try:
        bot.polling(none_stop=True)
        #bot.infinity_polling(True)

    except Exception as e:
        logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
#bot.polling()