# ARB_AIR_CHECKER

[donations are welcome](https://cyberomanov.tech/WTF_donate), if you find this tool helpful.

upd: в ссылке `https://arbitrum.foundation/_next/data/lB0zTjQwwi0nJOMcTT0Td/eligibility.json` надо менять этот `lB0zTjQwwi0nJOMcTT0Td` набор символов каждые N минут. сейчас работает с `lB0zTjQwwi0nJOMcTT0Td`, через час уже значение другое. обновляется какая-то "бд" и невозможно (не понимаю как) сделать универсальную ссылку. чтобы найти новое значение, нужно отследить запрос `https://arbitrum.foundation/eligibility?address=address` и найти актуальную ссылку на "бд". ну или пингануть [@cyberomanov](https://t.me/cyberomanov), подскажу значение.

## Installation
you need `python3.10` and 2 files: `arb.py` and `address.txt`.

```
python3 arb.py

>>> 0x111: 1000.
>>> 0x222: 1500.
>>> 0x333: 750.
>>> total: 3250.
```

