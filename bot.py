import telebot
from telebot import types

TOKEN = "8655535173:AAHlhUzqH1JhUhQ4WwgzJc0jOvbki40jnQU"

bot = telebot.TeleBot(TOKEN)
OPERATOR_LINK = "https://t.me/@operator_orbitt"
REVIEWS_LINK = "https://t.me/your_reviews"

products = {
    "item1": {
        "button": "📦 Ассортимент",
        "name": "Приветствуем Вас, в магазине ORBIT",
        "photo": "photos/item1.jpg",
        "points": [
            "Ассортимент магазина (09:00-01:00 по МСК)",
            "Добро пожаловать",
            "Лучшие товары",
            "Быстрая связь с оператором",
            "Гарантия качества",
            "Актуальность цен уточняйте у оператора"
        ]
    },

    "item2": {
        "button": "MDMA",
        "name": "MDMA",
        "photo": "photos/item2.jpg",
        "points": [
            "1 грамм - 4800₽",
            "2 грамм - 8800₽",
            "3 грамм - 13400₽",
            "5 грамм - 21500₽",
            "10 грамм - 41600₽",
            "Кол-во больше обсуждается отдельно"
        ]
    },

    "item3": {
        "button": "ЭКСТАЗИ",
        "name": "XTC/MIX",
        "photo": "photos/item3.jpg",
        "points": [
            "2 шт - 4500₽",
            "3 шт - 6550₽",
            "5 шт - 10400₽",
            "10 шт - 18700₽",
            "Лучшее качество",
            "Кол-во больше обсуждается отдельно"
        ]
    },

    "item4": {
        "button": "КОКАИН",
        "name": "КОКАИН",
        "photo": "photos/item4.jpg",
        "points": [
            "0.5 грамм - 9700₽",
            "1 грамм - 18900₽",
            "2 грамм - 34800₽",
            "3 грамм - 50300₽",
            "Чистый продукт",
            "Кол-во больше обсуждается отдельно"
        ]
    },

    "item5": {
        "button": "МЕТАМФЕТАМИН",
        "name": "МЕТАМФЕТАМИН",
        "photo": "photos/item5.jpg",
        "points": [
            "1 грамм - 5300₽",
            "2 грамм - 10300₽",
            "3 грамм - 15000₽",
            "5 грамм - 24700₽",
            "10 грамм - 52800₽",
            "Кол-во больше обсуждается отдельно"
        ]
    },

    "item6": {
        "button": "Шишки WHITE WIDOW",
        "name": "Шишки WHITE WIDOW",
        "photo": "photos/item6.jpg",
        "points": [
            "2 г - 4500₽",
            "3 г - 6550₽",
            "5 г - 10200₽",
            "10 г - 18500₽",
            "Высокое качество",
            "Кол-во больше обсуждается отдельно"
        ]
    },

    "item7": {
        "button": "МЕФЕДРОН",
        "name": "МЕФЕДРОН",
        "photo": "photos/item7.jpg",
        "points": [
            "1 грамм - 4400₽",
            "2 грамм - 8000₽",
            "3 грамм - 12400₽",
            "5 грамм - 21500₽",
            "10 грамм - 42600₽",
            "Лучшее предложение"
        ]
    },

    "item8": {
        "button": "ЛИРИКА",
        "name": "ЛИРИКА",
        "photo": "photos/item8.jpg",
        "points": [
            "Pfizer 14 шт - 6200₽",
            "Pfizer 28 шт - 12100₽",
            "Оригинал",
            "Высокое качество",
            "Наличие уточнять",
            "Поставка напрямую"
        ]
    }
}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        "📜 Правила магазина",
        "📦 Ассортимент",
        "👨‍💻 Оператор",
        "💼 Вакансии",
        
    )
    return markup


def intro_catalog_button():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Открыть каталог", callback_data="open_catalog"))
    return markup


def assortment_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for key, item in products.items():
        markup.add(types.InlineKeyboardButton(item["button"], callback_data=key))
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в ORBIT SHOP\n\n"
        "📦 У нас ты найдёшь:\n"
        "— качественный ассортимент\n"
        "— быстрый ответ\n"
        "— удобную покупку\n\n"
        "👇 Выбери раздел ниже",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "📦 Ассортимент")
def assortment_intro(m):
    text = (
        "📦 Ассортимент магазина\n\n"
        "Добро пожаловать.\n"
        "Актуальность цен и наличие уточняйте у оператора."
    )

    with open("photos/welcome.jpg", "rb") as photo:
        bot.send_photo(
            m.chat.id,
            photo,
            caption=text,
            reply_markup=intro_catalog_button()
        )


@bot.callback_query_handler(func=lambda call: call.data == "open_catalog")
def open_catalog(call):
    bot.send_message(
        call.message.chat.id,
        "Выбери товар:",
        reply_markup=assortment_menu()
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data in products)
def show_product(call):
    item = products[call.data]

    text = (
        f"{item['name']}\n\n"
        f"• {item['points'][0]}\n"
        f"• {item['points'][1]}\n"
        f"• {item['points'][2]}\n"
        f"• {item['points'][3]}\n"
        f"• {item['points'][4]}\n"
        f"• {item['points'][5]}"
    )

    with open(item["photo"], "rb") as photo:
        bot.send_photo(call.message.chat.id, photo, caption=text)

    bot.answer_callback_query(call.id)


@bot.message_handler(func=lambda m: m.text == "👨‍💻 Оператор")
def operator(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Написать оператору", url=OPERATOR_LINK))
    bot.send_message(m.chat.id, "Связь с оператором:", reply_markup=markup)





@bot.message_handler(func=lambda m: m.text == "📜 Правила магазина")
def rules(m):
    text = (
        "📜 Правила магазина\n\n"
        "1. Уточняйте наличие перед заказом.\n"
        "2. Уточняйте цену перед оплатой.\n"
        "3. Все детали обсуждаются заранее.\n"
        "4. Условия доставки согласуются отдельно.\n"
        "5. Возврат и обмен по условиям магазина.\n"
        "6. Оформляя заказ, вы соглашаетесь с правилами."
    )
    bot.send_message(m.chat.id, text)


@bot.message_handler(func=lambda m: m.text == "💼 Вакансии")
def jobs(m):
    text = (
        "💼 Вакансии\n\n"
        "По поводу вакансий обращайтесь к оператору."
    )
    bot.send_message(m.chat.id, text)


bot.infinity_polling()
