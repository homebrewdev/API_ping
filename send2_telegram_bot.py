# модуль для рассылки алерта что какой то из APi упал через моего телеграм бота bot API
import settings as s
import requests
from datetime import datetime


def send_bot_alert(host, message):
    print('start send by bot_api ....')
    # узнаем текущие дату время
    datetime_str = str(datetime.now())

    # data = {"chat_id_list": ["322734040", "72205748"],
    data = {"chat_id_list": ["322734040"],
            "message": {
                "quiz": "=========ALERT!===========",
                "Номер телефона": "Dentolo check API service",
                "Результаты опроса": f"Внимание, коллеги!! наше API {s.tmp_endpoint} не отвечает/упало!!",
                "service": "Dentolo check API service",
                "href": f"{s.tmp_endpoint}",
                "Домен": f"{s.tmp_endpoint}",
                "Время": f"{datetime_str}",
            },
            }

    req = requests.post(url=s.bot_api_endpoint, headers=s.bot_api_header, json=data)
    print(req.status_code)
