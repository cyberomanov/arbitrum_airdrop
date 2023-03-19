import json
import re

import requests


def get_addresses(path: str = 'address.txt') -> list:
    with open(path) as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]


def get_token(address: str, db_link: str) -> float:
    response = requests.get(url=f"https://arbitrum.foundation/_next/data/{db_link}/eligibility.json?"
                                f"address={address.lower()}")
    result = json.loads(response.content)['pageProps']
    if result['isEligible']:
        return result['eligibility']['tokens']
    else:
        return 0.0


def get_db_link() -> str:
    response = requests.get(
        "https://arbitrum.foundation/eligibility?address=0x0000000000000000000000000000000000000000")
    return re.search('buildId":"(.{21})"', response.text).group(1)


def main():
    total_amount = 0.0
    db_link = get_db_link()
    for address in get_addresses():
        amount = get_token(address=address, db_link=db_link)
        total_amount += amount
        print(f"{address}: {amount}.")
    print(f"total: {total_amount}.")


if __name__ == '__main__':
    main()
