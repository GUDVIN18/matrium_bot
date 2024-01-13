import telebot
from PIL import Image, ImageDraw, ImageFont
import os


bot = telebot.TeleBot('5813302231:AAFcksqurMC5nUd_-XCOYMg0DDbO_x0ozjs')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне фотографию, чтобы начать.\nМне можно отправить , ТОЛЬКО ОДНУ фотографию!")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # получаем информацию о фотографии
    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    # сохраняем фотографию во временном файле
    photo_path = "IMG_9817.jpg"
    with open(photo_path, "wb") as f:
        f.write(file)

    # обрабатываем фотографию
    processed_photo_path = process_photo(photo_path)

    # отправляем обработанную фотографию обратно пользователю
    with open(processed_photo_path, "rb") as f:
        bot.send_document(message.chat.id, f)
        print('Фото отправлено.', 'От: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))

def process_photo(photo_path):
    # загружаем фотографию с помощью PIL
    image = Image.open(photo_path)

    # обрезаем фотографию
    width, height = image.size
    left = 0
    top = 344.6
    right = width
    bottom = 934.0
    image = image.crop((left, top, right, bottom))

    # добавляем текст
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/home/w0461585/domains/my.matrium.ru/tgbot/ng_bots/a.ttf", size=26)
    text = "NIGHT GROUND"
    color = (0, 0, 0)
    x, y = 370, 560 # 385 553
    draw.text((x, y), text, font=font, fill=color)

    # сохраняем обработанную фотографию во временном файле
    processed_photo_path = "processed_photo.jpg"
    image.save(processed_photo_path)

    # удаляем временный файл
    os.remove(photo_path)

    return processed_photo_path
bot.polling()



