
languages = ['ru']
commands = ['low_price', 'high_price', 'best_deal', 'history']


following_messages = {
    'ru': {
        'hi_message': 'Будь как дома, Путник! Сегодня я помогу тебе с поиском ночлега. ',
        'help_message':
            '''Пожалуйста, выбери одну их опций:
/low_price (низкая цена) - список самых дешевых отелей
/high_price (высокая цена) - список самых дорогих отелей
/best_deal (лучшее предложение) - список самых близких отелей в определенных ценовых рамках
/history - история ваших поисков
/done (закончить запрос) - закончить запрос''',
        'currency_message': 'В какой валюте мне показывать цены?',
        'city_message': 'В каком городе ищем отель?',
        'hotels_quantity_message': 'Какое максимальное количиство отелей я могу тебе предложить?',
        'max_price_message': 'Какая максимальная цена является приемлемой?',
        'lowest_price_message': 'С какой самой низкой цены мне начать поиск?',
        'distance_from_center_message': 'В каком диапазоне от центра города мне искать отели, в км?',
        'history_message': 'Вот твоя история запросов:',
        'no_history': 'Раннее не было запросов.',
        'done_message': 'Твой запрос закрыт. Если нужно, начни новый запрос с помощъю команды /start',
        'best_deal_prices': 'Пожалуйста, укажи ценовой диапазон в формате: минимальная цена - максимальная цена в €.',
        'best_deal_distance':
            'Пожалуйста, укажи возможное максимальное расстояние от центра города для расположения отеля',
        'wrong_prices': 'Вы что-то указали некорректно. Пожалуйста укажи ценовой диапазон в формате:'
                        ' минимальная цена - максимальная цена в €.',
        'city': 'В каком городе ищем отели?',
        'city_confirmation': f'Пожалуйста подтверди город - ',
        'search_result': 'Какое максимальное количиство результатов поиска может быть?',
        'distance_error': 'Расстояние указано не правильно. Пожалуйста введи данные в км еще раз.',
        'request_error': 'Что-то пошло не так. Начни поиск заново.',
        'language_message': 'Выбери язык'
    }
}


buttons = {'ru': {'low_price': 'низкая цена',
                  'high_price': 'высокая цена',
                  'best_deal': 'лучшее предложение',
                  'history': 'история запросов',
                  'done': 'закончить запрос',
                  'yes': 'да',
                  'no': 'нет'}}

