import requests
import json
from bs4 import BeautifulSoup

def get_addresses(path: str = 'address.txt') -> list:
    with open(path) as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]

def get_token(address: str) -> float:
    url = "https://arbitrum.foundation/eligibility?address=" + str(address.lower())
    request = requests.get(url).text
    soup = BeautifulSoup(request,"html.parser")
    script = soup.find('script',type="application/json")
    my_json = str(script)[51:-9]
    result = (json.loads(my_json)['props']['pageProps'])
    if result['isEligible']:
        return result['eligibility']['tokens']
    else:
        return 0.0

if __name__ == '__main__':
    total_amount = 0.0
    session = requests.session()
    for address in get_addresses():
        amount = get_token(address=address)
        total_amount += amount
        print(f"{address}: {amount}.")
    print(f"total: {total_amount}.")
