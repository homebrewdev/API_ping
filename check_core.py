import requests
import pprint as prnt
import settings as s


def check_tmp_api() -> int:
    response = requests.get(url=s.tmp_endpoint, headers=s.tmp_header)
    print("Status Code:", response.status_code)
    return response.status_code
    # print("JSON Response:")
    # prnt.pprint(response.json())


def check_un_api() -> int:
    response = requests.get(url=s.un_endpoint, headers=s.un_header)
    print("Status Code:", response.status_code)
    return response.status_code


def check_main_api() -> int:
    response = requests.get(url=s.api_endpoint, headers=s.api_header)
    print("Status Code:", response.status_code)
    return response.status_code


def check_api(endpoint, headers) -> int:
    response = requests.get(url=endpoint, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        print(f"check API {endpoint} ! Status code: {status_code}")
    else:
        print(f"API {endpoint} IS DOWN! Status code: {status_code} -> Sending alert!")
    return response.status_code
