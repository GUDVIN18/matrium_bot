from datetime import datetime
import schedule
import telebot
from pycbrf import ExchangeRates
import random
import time
#import config
from telebot import types
from cbrf.models import DailyCurrenciesRates
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import os, sys
activate_this = '/home/w0461585/python/bin/activate_this.py'
with open(activate_this) as f:
     exec(f.read(), {'__file__': activate_this})


bot = telebot.TeleBot('5871761173:AAGzSfS3RSD5-cAh79U5omOEB2-P0X3mmZM')

@bot.message_handler(commands=['start'])
def start(message):
    is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
    if is_subscribed is True:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn2 = telebot.types.KeyboardButton('📈 Курс')
        item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
        item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
        #item4 = telebot.types.KeyboardButton("😊 Как дела?")
        item5 = telebot.types.KeyboardButton("🎁 Акции")
        item6 = telebot.types.KeyboardButton("📞 Обратная связь")
        item7 = telebot.types.KeyboardButton("🙌 Отзывы")
        markup.add(itembtn2,item5, item3, item6, item2, item7)
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЗаинтересовались покупкой в нашем магазине? Бот поможет рассчитать стоимость товара по актуальному курсу!".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)


    else:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item3 = types.InlineKeyboardButton("Подписаться", url='https://t.me/NIGHT_GROUND')

        markup.add(item3)
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nДля пользования ботом вам необходимо быть подписчиком нашего канала!".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn2 = telebot.types.KeyboardButton('Готово!')
        markup.add(itembtn2)
        time.sleep(2)
        bot.send_message(message.chat.id, "Нажмите на Готово, как все сделаете".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)






@bot.message_handler(content_types=['text'])
def message(message):
    if message.chat.type == 'private':
        if message.text == 'Готово!':
            is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
            if is_subscribed is True:
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    itembtn2 = telebot.types.KeyboardButton('📈 Курс')
                    item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
                    item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
                    #item4 = telebot.types.KeyboardButton("😊 Как дела?")
                    item5 = telebot.types.KeyboardButton("🎁 Акции")
                    item6 = telebot.types.KeyboardButton("📞 Обратная связь")
                    item7 = telebot.types.KeyboardButton("🙌 Отзывы")
                    markup.add(itembtn2,item5, item3, item6, item2, item7)
                    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЗаинтересовались покупкой в нашем магазине? Бот поможет рассчитать стоимость товара по актуальному курсу!".format(message.from_user, bot.get_me()),
                        parse_mode='html', reply_markup=markup)


            else:
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Подписаться", url='https://t.me/NIGHT_GROUND')
                markup.add(item3)
                # bot.send_message(message.chat.id, "ХЕР!".format(message.from_user, bot.get_me()),
                #     parse_mode='html', reply_markup=markup)


        is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
        if is_subscribed is True:
            if message.text == '✅ Расчитать стоимость':


                    # daily = DailyCurrenciesRates()
                    # daily.date
                    # daily.get_by_id('R01375').name
                    # global price
                    # a = float(daily.get_by_id('R01375').value)

                    ################################################################################################################################################################

                    #price = a / 10
                    price = 13.94

                    ################################################################################################################################################################

                    print(round((price), 2), 'Расчет.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))

                    v = bot.send_message(message.chat.id, 'Введи стоимость товара в Юанях')
                    bot.register_next_step_handler(v, returning)


            elif message.text == 'Рандомное число':
                        bot.send_message(message.chat.id, str(random.randint(0,1000)))




            elif message.text == '📈 Курс':
                    # daily = DailyCurrenciesRates()
                    # daily.date
                    # daily.get_by_id('R01375').name

                    # a = float(daily.get_by_id('R01375').value)

                    ################################################################################################################################################################

                    #price = a / 10
                    price = 13.94

                    ################################################################################################################################################################

                    print(price, 'Курс.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))
                    bot.send_message(message.chat.id, f'Курс юаня на сегодня: {round((price), 2)}')

            elif message.text == '🎁 Акции':

                    bot.send_message(message.chat.id, '''Сейчас мы проводим акцию "ПРИВЕДИ ДРУГА".

    Если вы приводите друга, который оформляет заказ вмести с вами - скидка 500 руб на ваш заказ!''')
                    print('Акции.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


            elif message.text == '🙌 Отзывы':
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    item3 = types.InlineKeyboardButton("Перейти", url='https://t.me/+izYbQgg7gD84ODRi')
                    markup.add(item3)
                    bot.send_message(message.chat.id, f'Наши отзывы', reply_markup=markup)
                    print('Отзывы.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))




            elif message.text == '📞 Обратная связь':
                    feedback = bot.send_message(message.chat.id, 'Остались вопросы? Напиши нам!')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_button = types.KeyboardButton('Назад')
                    markup.add(back_button)
                    bot.send_message(chat_id=message.chat.id, text="Нажмите кнопку 'Назад', если хотите вернуться.", reply_markup=markup)
                    bot.register_next_step_handler(feedback, feedback_send)
                    print('Обратная связь.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))



            elif message.text == 'Назад':
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                            itembtn2 = telebot.types.KeyboardButton('📈 Курс')
                            item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
                            item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
                            #item4 = telebot.types.KeyboardButton("😊 Как дела?")
                            item5 = telebot.types.KeyboardButton("🎁 Акции")
                            item6 = telebot.types.KeyboardButton("📞 Обратная связь")
                            item7 = telebot.types.KeyboardButton("🙌 Отзывы")
                            markup.add(itembtn2,item5, item3, item6, item2, item7)
                            bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)

                            print('Назад', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))









            elif message.text == '🎉 Розыгрыши':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                        #item5 = telebot.types.KeyboardButton("Участвовать")
                        # item6 = telebot.types.KeyboardButton("Количество участников")
                        item7 = telebot.types.KeyboardButton("Назад")
                        markup.add(item7)
                        bot.send_message(chat_id=message.chat.id, text="Новый розыгрыш состоится уже совсем скоро! \nСледите за новостями в нашем канале.", reply_markup=markup)




            # elif message.text == 'Участвовать':
            #     def is_user_in_file(user_id):
            #         with open('participants.txt', 'r') as file:
            #             global users
            #             users = file.readlines()
            #             global num_lines
            #             num_lines = len(users)

            #             for user in users:
            #                 if str(user_id) == user.strip():
            #                     return True
            #         return False
            #     user_id = message.chat.username
            #     if is_user_in_file(user_id):

            #         markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            #         item5 = telebot.types.KeyboardButton("Назад")
            #         markup.add(item5)

            #         bot.reply_to(message, f"Вы уже участвуете!", reply_markup=markup)

            #     else:

            #         with open('participants.txt', 'a') as file:
            #             file.write(str(user_id) + '\n')

            #         markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            #         item5 = telebot.types.KeyboardButton("Назад")
            #         markup.add(item5)
            #         bot.reply_to(message, f"Спасибо за участие!", reply_markup=markup)

            #         print('Розыгрыш.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


            # elif message.text == 'Количество участников':
            #     with open('participants.txt', 'r') as file:
            #         users = file.readlines()
            #         members_len = len(users)
            #         bot.reply_to(message, f"Количество участников: {members_len}")
            #         print('Кол-во участников', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))









            elif message.text == 'Готово!':
                print('fake_error', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


            else:
                    bot.send_message(message.chat.id, '''Я не знаю что ответить 😢
        Нажмите /start''')
        else:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Подписаться", url='t.me/NIGHT_GROUND')

            markup.add(item3)
            bot.send_message(message.chat.id, "Для пользования ботом вам необходимо быть подписчиком нашего канала!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn2 = telebot.types.KeyboardButton('Готово!')
            markup.add(itembtn2)
            time.sleep(2)
            bot.send_message(message.chat.id, "Нажмите на Готово, как все сделаете".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)




@bot.message_handler(commands=['return'])
def returning(message):
    if message.text.isdigit():
        d = int(message.text)
        curce = 13.94

        if d >= 100000000 or d <= 10:
            print("Слишком много")
            bot.send_message(message.chat.id, f'Не допустимое значение!')
        else:
           if d <= 500:
                m = round((d *(curce)+1400+1000))
                bot.send_message(message.chat.id, f'Итоговая стоимость без доставки {m} руб.')
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Связаться", url='https://t.me/MANAGER_NIGHT_GROUND')
                markup.add(item3)
                bot.send_message(message.chat.id, f'Для расчета стоимости доставки и оформления заказа, свяжитесь с менеджером.', reply_markup=markup)

                print(message.text)

           elif d >= 501:
                m = (d *(curce) + 1000)
                last_price = round((m + (m/100*12)))
                bot.send_message(message.chat.id, f'Итоговая стоимость без доставки {last_price} руб.')
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Связаться", url='https://t.me/MANAGER_NIGHT_GROUND')
                markup.add(item3)
                bot.send_message(message.chat.id, f'Для расчета стоимости доставки и оформления заказа, свяжитесь с менеджером.', reply_markup=markup)

                print(message.text)

    else:
        bot.reply_to(message, f'Введите только число!')


def feedback_send(message):
    if message.text == 'Назад':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn2 = telebot.types.KeyboardButton('📈 Курс')
        item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
        item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
        #item4 = telebot.types.KeyboardButton("😊 Как дела?")
        item5 = telebot.types.KeyboardButton("🎁 Акции")
        item6 = telebot.types.KeyboardButton("📞 Обратная связь")
        item7 = telebot.types.KeyboardButton("🙌 Отзывы")
        markup.add(itembtn2,item5, item3, item6, item2, item7)
        bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    else:
        feedback_sms = str(message.text)
        print(f'Пользователь оставил сообщение: {feedback_sms}')
        username = message.from_user.username # Получаем id отправителя сообщения
        bot.send_message(message.chat.id, '''Ваш вопрос успешно получен! Ожидайте, в скором времени менеджер с вами свяжется.''')
        user_id = '5703202303'  # Здесь нужно указать ID пользователя, которому будут пересылаться сообщения
        bot.send_message(user_id, f'Сообщение от пользователя @{username}: {feedback_sms}')  # Пересылаем текст сообщения



# bot.polling(none_stop=True)
# Функция для запуска опроса каждые 900 секунд
def run_polling():
    while True:
        schedule.run_pending()
        time.sleep(900)

schedule.every(900).seconds.do(start)

# Запуск опроса и проверки подписок в отдельном потоке
import threading
polling_thread = threading.Thread(target=run_polling)
polling_thread.daemon = True  # Установите daemon в True, чтобы поток работал в фоновом режиме
polling_thread.start()

# Отсюда начинается основной поток, в котором обрабатываются сообщения
bot.infinity_polling()