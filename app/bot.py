import requests
from environs import Env
#from urllib.parse import quote

env = Env()
env.read_env()

def send_message(text):
    BOT_TOKEN = env("BOT_TOKEN")
    CHAT_ID = env("CHAT_ID")
    Text=text
   # encoded_text = quote(text)  # Matnni URL uchun mos formatga keltirish

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={Text}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Message sent successfully, status code: {response.status_code}")
        print(f"Response content: {response.text}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        print(f"Response content: {response.text}")
    except Exception as err:
        print(f"Other error: {err}")