# main
import test

if __name__ == '__main__':
    status_code = test.check_tmp_api()
    if status_code == 200:
        print("API IS OK! Status code = 200")
    else:
        print(f"API IS DOWN! Status code: {status_code} Sending alert!")
