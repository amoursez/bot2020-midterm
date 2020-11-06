# connecting Telegram API
import telebot
# importing library for creating buttons
from telebot import types
# module for generating pseudo-random data
import random

bot = telebot.TeleBot('1365713371:AAFmtl25cCSvt5Q_hD9EvBG97LjfYwNX3wg')


# decorator to the function which is triggered by the / start command
@bot.message_handler(commands=["start"])
def start(message):
    # сreating menu and buttons in it
    # ReplyKeyboardMarkup object represents a custom keyboard
    # with reply options
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    foodbtn = types.KeyboardButton(text='Еда')
    shopbtn = types.KeyboardButton(text='Шоппинг')
    funbtn = types.KeyboardButton(text='Развлечения')
    devbtn = types.KeyboardButton(text='Развитие')
    aboutbtn = types.KeyboardButton(text='О боте')
    sezimschoice = types.KeyboardButton(text="Никуда не хочу")
    randombtn = types.KeyboardButton(text='Случайный выбор')
    keyboard.row(foodbtn, shopbtn, funbtn, devbtn)
    keyboard.row(aboutbtn, sezimschoice, randombtn)
# sending message to the user
    bot.send_message(message.chat.id, '''Привет,меня зовут Пип!Я помогу тебе быстро найти место,куда сходить🌇
Выбери категорию ниже👇А если у тебя нет идей вообще, то нажми кнопку
"Cлучайный выбор"''', reply_markup=keyboard)


# Function that is triggered when sending any text to bot
@bot.message_handler(content_types=['text'])
def options(message):
    if message.text == 'Еда':
        bot.send_message(message.chat.id, "Одну секунду...⏳")
        bot.send_message(message.chat.id,
                         '🔺Chicken star\n🔺Арт-кафе\n🔺Средний чек-500 cом.Живая'
                         'музыка\n🔺Адрес-https://go.2gis.com/igyth')
        # sending photo to the user
        bot.send_photo(message.chat.id,
                       'http://biglife.kg/uploads/Кафе/ЧикенСтра/DSC_0031.jpg')
        bot.send_message(message.chat.id,
                         '''🔺DuЭт coffee & restaurant\n🔺Ресторан\n
                         \n🔺Средний чек-500 cом.Турецкая '''
                         'кухня.\n🔺Адрес-https://go.2gis.com/zylhn')
        bot.send_photo(message.chat.id,
                       'https://duetbishkek.kg/wp-content/uploads/2019'
                       '/11/KIPYATCOM_084-2-1-min.png')
        bot.send_message(message.chat.id,
                         '''🔺Облако 53\n🔺Лаундж-бар
                         \n🔺Средний чек-700 cом. Винная '''
                         "карта\n🔺Адрес-https://go.2gis.com/gzryh")
        bot.send_photo(message.chat.id,
                       'https://avatars.mds.yandex.net/get-altay'
                       '/1909414/2a0000016b343d67c060691c0b7aaaa8b8aa/XXXL')
        bot.send_message(message.chat.id,
                         '''🔺Горький Preparty Place\n🔺Кафе-бар
                         \n🔺Средний чек-500 cом. Живая музыка.
                         Бизнес-ланчи от'''
                         "120сом!\n🔺Адрес-https://go.2gis.com/3q8tf")
        bot.send_photo(message.chat.id,
                       'https://mir-s3-cdn-cf.behance.net/project_modules'
                       '/1400/400d3a28742485.55cfeb28f0bca.png')
        bot.send_message(message.chat.id,
                         '''🔺MADFOOD\n🔺Ресторан быстрого питания
                         \n🔺Средний чек-400 cом. Паназиатская '''
                         "кухня\n🔺Адрес-https://go.2gis.com/le4k43")
        bot.send_photo(message.chat.id, 'https://i1.photo.2gis.com/images'
                                        '/branch/50/7036874424466645_3e52.jpg')
    elif message.text == 'Шоппинг':
        bot.send_message(message.chat.id,
                         '''🔹Евразия\n🔹Торговый-бизнес центр
                         \n🔹Удобное расположение в центре города, '''
                         '''красивый и интересный интерьер
                         \n🔹Адрес-https://go.2gis.com/9h5f8''')
        bot.send_photo(message.chat.id,
                       'https://avatars.mds.yandex.net/get-altay'
                       '/2701558/2a000001705b3cac5c2fc430f8e8f2b8e701/XXXL')
        bot.send_message(message.chat.id,
                         '🔹IMall\n🔹Торгово-развлекательный центр'
                         '\n🔹Имеется детская зона\n'
                         "🔹Адрес-https://go.2gis.com/19k26")
        bot.send_photo(message.chat.id, 'https://im0-tub-ru.yandex.net'
                       '/i?id=1182ae5a992a4c7b9cb875fa5a8346e3&n=13')
        bot.send_message(message.chat.id,
                         '🔹AsiaMall\n🔹Торгово-развлекательный центр'
                         '\n🔹Торговый центр высокого'
                         "класса\n🔹Адрес-https://go.2gis.com/s4s7b")
        bot.send_photo(message.chat.id, 'http://steelex.asia/wp-content'
                       '/uploads/2015/05/AsiaMollLite.png')
        bot.send_message(message.chat.id,
                         '''🔹Дордой Плаза\n🔹Торгово-развлекательный центр
                         \n🔹Больший и красивый торговый'''
                         "дом.\n🔹Адрес-https://go.2gis.com/ghgmql")
        bot.send_photo(message.chat.id,
                       'https://www.modernglass.ru/upload/iblock'
                       '/84d/Steklopakety-Modern-Glass-na-proekte-Dordoi'''
                       '-Plaza_-Bishkek-1.jpg')
    elif message.text == 'Развлечения':
        bot.send_message(message.chat.id,
                         '''⚪️Проклятый лагерь\n⚪️Квест в реальной жизни\
                         ⚪️ 🔥Профессиональные актеры 🔥3 уровня'''
                         "сложности\n⚪️Адрес-https://go.2gis.com/su87z")
        bot.send_photo(message.chat.id,
                       'https://sankt-peterburg.spravka.ru/uploads'
                       '/0/0/F2/vYei-eR1T7qWk1VOZoiKEFKTmTAMoa'
                       '/original_5678f97c1cecb369388b4571_56a0b145422bc.jpg')

        bot.send_message(message.chat.id,
                         '⚪️Scorpion\n⚪️Пейнтбольный клуб\n⚪️Персональный '
                         'инструктор обучит всему'
                         "бесплатно\n⚪️Адрес-https://go.2gis.com/j8kl6")
        bot.send_photo(message.chat.id,
                       'https://pb-tmb.ru/wp'
                       '-content/uploads/2019/09/pejntbol1111-1024x683.jpg')
        bot.send_message(message.chat.id,
                         "⚪️The story\n⚪️Антикинотеатр\n⚪️Кабинки "
                         "для компаний от 2 до 20 человек. От 200 "
                         "сом/час.\n⚪️Адрес-https://go.2gis.com/d213w")
        bot.send_photo(message.chat.id,
                       "http://biglife.kg/uploads/"
                       "Развлечение/The story/slide1.jpg")
        bot.send_message(message.chat.id,
                         "⚪️Zoobishkek\n⚪️Реабилитационный "
                         "зоопарк\n⚪️Спасенные "
                         "счастливые животные, большую часть из "
                         "которых можно погладить.Цены "
                         "смешные, а впечатлений на "
                         "миллион\n⚪️Адрес-https://go.2gis.com/djlf1")
        bot.send_photo(message.chat.id,
                       "http://biglife.kg/uploads/Раз"
                       "влечение/Зоосмешарики/1.jpg")
    elif message.text == 'Развитие':
        bot.send_message(message.chat.id,
                         "📚Coffee arte gallery\n📚Арт-центр "
                         "кофейня\n📚Заведение для любителей кофе и "
                         "искусства.Имеются картины знаменитых художников,"
                         "музыкальные инструменты и приятная "
                         "музыка.\n📍Адрес-https://go.2gis.com/5d5i4")
        bot.send_photo(message.chat.id,
                       "https://www.artranked.com/images"
                       "/c1/c1100a9758b6dcbd58e5b53da332421c.jpg")
        bot.send_message(message.chat.id,
                         "📚Республиканская библиотека "
                         "для детей и юношества им. К. "
                         "Баялинова\n📚Библиотека\n📚Доступно для инвалидов."
                         "Имеется маркет-плэйс.Огромное количество "
                         "книг\n📍Адрес-https://go.2gis.com/k1tncn")
        bot.send_photo(message.chat.id,
                       "https://pbs.twimg.com/media/EJeC8ArXYAAZVIK.jpg")
        bot.send_message(message.chat.id,
                         "📚Мемориальный дом-музей им. М.В. "
                         "Фрунзе\n📚Музей\n📚В этом музее можно ознакомится с "
                         "историей образования города "
                         "Фрунзе со всеми предметами быта того "
                         "времени.\n📍Адрес-https://go.2gis.com/sc4ho")
        bot.send_photo(message.chat.id,
                       "http://www.photo.kg/uploads/posts"
                       "/2015-02/1422948033_imgl3186.jpg")
        bot.send_message(message.chat.id,
                         "📚Asanbay Center\n📚Культурный центр\n📚Необычное п"
                         "ространство для нашего города.Очень "
                         "интересно внутри. Проводят совершенно "
                         "разные по направленности "
                         "мероприятия\n📍Адрес-https://go.2gis.com/gbi5j")
        bot.send_photo(message.chat.id,
                       "https://pbs.twimg.com/media/"
                       "DNKBHI1W0AAJ0TG?format=jpg&name=large")
    elif message.text == "О боте":
        bot.send_message(message.from_user.id,
                         "Этот бот был создан начинающим "
                         "программистом для мидтерма в Международном "
                         'университете '
                         'Ала-Тоо🙊Я очень надеюсь,что мой бот был '
                         'хоть чем-то полезен вам и вы нашли для себя '
                         'интересное место для посещения!')
    elif message.text == 'Случайный выбор':
        random_place = random.choice(sezim_list)
        bot.send_message(message.chat.id, random_place)
    elif message.text == "Никуда не хочу":
        bot.send_message(message.from_user.id,
                         'Тогда вот 7 идей,чем ты можешь заняться🏡\n'

                         '1. Потанцевать. Под любимую музыку, конечно!💃\n'

                         '2. Протестировать новую игру. Например, '
                         'Morphite или Alto’s Odyssey💻\n'

                         '3. Посмотреть все серии «Игры престолов» '
                         'одним махом. Если хватит выходных, конечно🙈\n'

                         '4. Сделать много селфи, выбрать лучшие и '
                         'обновить аватарки в мессенджерах и соцсетях☺\n'

                         '5. Перемерить всю актуальную одежду, '
                         'скомпоновав несколько стильных образов👗\n'

                         '6. Передвинуть мебель, чтобы освежить интерьер🛋\n'
                         'Любые изменения окружающего пространства'
                         ' идут на пользу клеткам головного '
                         'мозга, улучшают память и настроение.\n'

                         '7. Сделать планку✔')
# a list of all places for the random module
sezim_list = ['🔺Chicken star\n🔺Арт-кафе\n🔺Средний чек-500 cом.Живая '
              'музыка\n🔺Адрес-https://go.2gis.com/igyth',
              '🔺DuЭт coffee & restaurant\n🔺Рест'
              'оран\n🔺Средний чек-500 cом.Турецкая '
              'кухня.\n🔺Адрес-https://go.2gis.com/zylhn',
              '🔺Облако 53\n🔺Лаундж-бар\n🔺Средний чек-700 cом. Винная'
              'карта\n🔺Адрес-https://go.2gis.com/gzryh',
              '🔺Горький Preparty Place\n🔺Кафе-бар\n🔺'
              'Средний чек-500 cом. Живая музыка.Бизнес-ланчи от '
              "120сом!🔺Адрес-https://go.2gis.com/3q8tf",
              "🔺MADFOOD\n🔺Ресторан быстрого питания\n🔺Ср"
              "едний чек-400 cом. Паназиатская "
              "кухня\n🔺Адрес-https://go.2gis.com/le4k43",
              "🔹Евразия\n🔹Торговый-бизнес центр\n🔹"
              "Удобное расположение в центре города, "
              "красивый и интересный интерьер\n🔹"
              "Адрес-https://go.2gis.com/9h5f8",
              "🔹IMall\n🔹Торгово-развлекательный "
              "центр\n🔹Имеется детская зона\n"
              "🔹Адрес-https://go.2gis.com/19k26",
              "🔹AsiaMall\n🔹Торгово-развлекательный "
              "центр\n🔹Торговый центр высокого "
              "класса\n🔹Адрес-https://go.2gis.com/s4s7b",
              "🔹Дордой Плаза\n🔹Торгово-развлекательный"
              " центр\n🔹Больший и красивый торговый "
              "дом.\n🔹Адрес-https://go.2gis.com/ghgmql",
              "⚪️Проклятый лагерь\n⚪️Квест в реальной "
              "жизни\n⚪️ 🔥Профессиональные актеры 🔥3 уровня "
              "сложности\n⚪️Адрес-https://go.2gis.com/su87z",
              "⚪️Scorpion\n⚪️Пейнтбольный клуб\n⚪️"
              "Персональный инструктор обучит всему "
              "бесплатно\n⚪️Адрес-https://go.2gis.com/j8kl6",
              "⚪️The story\n⚪️Антикинотеатр\n⚪️"
              "Кабинки для компаний от 2 до 20 человек. От 200 "
              "сом/час.\n⚪️Адрес-https://go.2gis.com/d213w",
              "📚Coffee arte gallery\n📚Арт-центр "
              "кофейня\n📚Заведение для любителей кофе и "
              "искусства.Имеются картины знаменитых "
              "художников,музыкальные инструменты и приятная "
              "музыка.\n📍Адрес-https://go.2gis.com/5d5i4",
              "📚Республиканская библиотека для детей и юношества им. К. "
              "Баялинова\n📚Библиотека\n📚Доступно для и"
              "нвалидов.Имеется маркет-плэйс.Огромное количество "
              "книг\n📍Адрес-https://go.2gis.com/k1tncn",
              "📚Asanbay Center\n📚Культурный центр\n📚Н"
              "еобычное пространство для нашего города.Очень "
              "интересно внутри. Проводят "
              "совершенно разные по направленности "
              "мероприятия\n📍Адрес-https://go.2gis.com/gbi5j",
              "📚Мемориальный дом-музей им. М.В. "
              "Фрунзе\n📚Музей\n📚В этом музее можно ознакомится с "
              "историей образования города "
              "Фрунзе со всеми предметами быта того "
              "времени.\n📍Адрес-https://go.2gis.com/sc4h",
              "⚪️Zoobishkek\n⚪️Реабилитационный зоопарк\n"
              "⚪️Спасенные счастливые животные,"
              "большую часть из которых можно погладить."
              "на миллион\n⚪️Адрес-https://go.2gis.com/djlf1"]
# launching bot constantly checking for messages
bot.polling(none_stop=True, interval=0)
