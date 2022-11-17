import requests
import pprint as prnt

target_url = "https://tmp......"

headers = {"Authorization": "api_key"}


def check_tmp_api() -> int:
    response = requests.get(url=target_url, headers=headers)
    print("Status Code:", response.status_code)
    return response.status_code
    # print("JSON Response:")
    # prnt.pprint(response.json())
