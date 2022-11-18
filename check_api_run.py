# checker module for API`s
import check_core as core
import settings as s


# Основной запуск проверки API по эндпоинтам
def run_check():
    status_code = core.check_api(endpoint=s.tmp_endpoint, headers=s.tmp_header)
    print(status_code)
    status_code = core.check_api(endpoint=s.un_endpoint, headers=s.un_header)
    print(status_code)
    status_code = core.check_api(endpoint=s.api_endpoint, headers=s.api_header)
    print(status_code)

