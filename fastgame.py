import config #это файл с токеном бота
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):  #сообщение которое приходит в самом начале
    sti = open("./path/"'stiker.png', 'rb') #открытие стикера (путь, имя)
    bot.send_sticker(message.chat.id, sti) #вывод стикера в чат
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # пять строчек с кнопками на панели
    item3 = types.KeyboardButton("Приложения")
    item2 = types.KeyboardButton("Мероприятия")
    item1 = types.KeyboardButton('О нас')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,  #вывод сообщения в чат
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, бот команды Projector в НГТУ, "
                     "создан для того, "
                     "чтобы помочь Вам влиться в нашу команду,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\n\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    if message.chat.type == 'private':

        if message.text == 'О нас':
            keyboard1 = types.InlineKeyboardMarkup(row_width=1) #мы установили row_width = 1, что обозначает самую широкую грань одной кнопки, поэтому они и будут расположены друг под другом.
            boo = types.InlineKeyboardButton(text="Тыщ на кнопку и ты уже в Google", url="https://www.google.ru")
            boo1 = types.InlineKeyboardButton('Рандомное число', callback_data='gd2')
            boo2 = types.InlineKeyboardButton("Калькулятор", callback_data='bd2')
            boo3 = types.InlineKeyboardButton("Хочу узнать погоду в моем городе/стране", callback_data='gd3')
            boo4 = types.InlineKeyboardButton("Как твои дела?", callback_data='bd4')
            keyboard1.add(boo, boo1, boo2, boo3, boo4)
            bot.send_message(message.chat.id, "{0.first_name}, окей, смотри, что у нас есть тут:\n"
                            .format(message.from_user), parse_mode="html", reply_markup=keyboard1)
        elif message.text == 'Приложения':
            keyboard = types.InlineKeyboardMarkup(row_width=1)#мы установили row_width = 1, что обозначает самую широкую грань одной кнопки, поэтому они и будут расположены друг под другом.
            itemboo = types.InlineKeyboardButton(text="Тыщ на кнопку и ты уже в Google", url="https://www.google.ru")
            itemboo1 = types.InlineKeyboardButton('Рандомное число', callback_data='good2')
            itemboo2 = types.InlineKeyboardButton("Калькулятор", callback_data='bad2')
            itemboo3 = types.InlineKeyboardButton("Хочу узнать погоду в моем городе/стране", callback_data='good3')
            itemboo4 = types.InlineKeyboardButton("Как твои дела?", callback_data='bad4')
            keyboard.add(itemboo, itemboo1, itemboo2, itemboo3, itemboo4)
            bot.send_message(message.chat.id, "{0.first_name}, окей, смотри, что у нас есть тут:\n"
                            .format(message.from_user), parse_mode="html", reply_markup=keyboard)

        elif message.text == "Мероприятия":
            one_markup = types.InlineKeyboardMarkup(row_width=1)#мы установили row_width = 1, что обозначает самую широкую грань одной кнопки, поэтому они и будут расположены друг под другом.
            ite1 = types.InlineKeyboardButton("Ближайшие мероприятия", callback_data="one")
            ite2 = types.InlineKeyboardButton("Проведенные мероприятия", callback_data="two")
            ite3 = types.InlineKeyboardButton("Волонтерство на мероприятие", callback_data="three")
            ite4 = types.InlineKeyboardButton("Действующие проекты в НГТУ", callback_data="fourth")
            ite5 = types.InlineKeyboardButton("Мероприятия Межвузовского центра", callback_data="five")
            one_markup.add(ite1, ite2, ite3, ite4, ite5)
            bot.send_message(message.chat.id, "{0.first_name}, у нас <u>ежемесячно</u> проводится множество " "мероприятий,\nмы постарались разбить их на следующие составляющие:"
                             .format(message.from_user), parse_mode="html", reply_markup=one_markup)

            # МЕРОПРИЯТИЯ

@bot.callback_query_handler(func=lambda call:True ) # call.data in ['one', 'two', 'three', 'fourth', 'five'])
def callback_inline_one(call):
        if call.message:

#Мероприятия

            if call.data == 'one':  # Ближайшие мероприятия

                 # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь") #При таком методе ответ заменит кнопки со списком выбора!!
                 #ключевые моменты               #При таком методе ответ заменит кнопки со списком выбора!!
                 #bot.edit_message_text(chat_id=        ,message_id=     ,text='        ')      #При таком методе ответ заменит кнопки со списком выбора!!

                bot.send_message(chat_id=call.message.chat.id, text=
                                 "Итак,<b>ближайшие мероприятия</b>:\n\n"  # Здесь будут ссылки ещё
                                 "Форум «Байкал»\n"
                                 "Конкурс «Цифровой ветер»\n"
                                 "PRONETI", parse_mode="html")
                # bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пыщь!") #всплывающее окно вверхней части экрана
                # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Пыщь!") #всплывающее окно на весь экран с подтверждением


            elif call.data == 'two':  # Проведённые мероприятия
                bot.send_message(call.message.chat.id, "Вот список <b>проведённых мероприятий</b>:\n\n"
                                                       "МНТК\n"
                                                       "Семинары по проектной деятельности\n"
                                                       "Встреча с представителями предприятий",
                                 parse_mode="html")
            elif call.data == 'three':  # Волонтерство на мероприятие
                bot.send_message(call.message.chat.id, "Волонтерство на мероприятие", parse_mode="html")
            elif call.data == 'fourth':  # Действующие проекты в НГТУ
                bot.send_message(call.message.chat.id, "Действующие проекты в НГТУ", parse_mode="html")
            elif call.data == 'five':  # Мероприятия Межвузовского центра
                bot.send_message(call.message.chat.id, "Мероприятия Межвузовского центра",
                                 parse_mode="html")

# О НАС
            elif call.data == 'gd2':
                bot.send_message(call.message.chat.id, " О нас 2 кнопка",
                                 parse_mode="html")
            elif call.data == 'bd2':
                bot.send_message(call.message.chat.id, " О нас 3 кнопка",
                                 parse_mode="html")
            elif call.data == 'gd3':
                bot.send_message(call.message.chat.id, " О нас 4 кнопка",
                                 parse_mode="html")
            elif call.data == 'bd4':
                bot.send_message(call.message.chat.id, " О нас 5 кнопка",
                                 parse_mode="html")

#ПРИЛОЖЕНИЯ
            elif call.data == 'good2':
                bot.send_message(call.message.chat.id, " Приложение 2 кнопка",
                                 parse_mode="html")
            elif call.data == 'bad2':
                bot.send_message(call.message.chat.id, " Приложение 3 кнопка",
                                 parse_mode="html")
            elif call.data == 'good3':
                bot.send_message(call.message.chat.id, " Приложение 4 кнопка",
                                 parse_mode="html")
            elif call.data == 'bad4':
                bot.send_message(call.message.chat.id, " Приложение 5 кнопка",
                                 parse_mode="html")



#bot.polling(none_stop=True)  # команда для постоянного цикла работы бота

# RUN
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")