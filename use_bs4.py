import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'success! Response = {response.status_code}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f"Hasil Pemanggilan {url}")
        # mencetak title dengan bentuk string
        print(f"Title: {soup.title.string}")
    else:
        print(f'Whoops, ada kesalahan requests {response.status_code}')
except Exception as e:
    print(f'There is an error!{e}')
print('Program ended!')
