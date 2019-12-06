# pyavanza

A Python library and client for accessing Avanza account balances.

The client `avanza_client.py` outputs all account balance values as JSON.

Uses a JSON API endpoint to fetch account values.

## Setup and authentication

In order to fetch values from Avanza valid header and cookies has to be setup.

One way to do this is to login to Avanza in a desktop web browser and use the web inspector to copy headers and cookies in order to use the same login session.

## Usage avanza.py

```python
from avanza.avanza import Avanza

headers = {
    ...
}

cookies = {
    ...
}

avanza = Avanza(headers, cookies)
avanza.get_account_values()
```

```python
{
    "account-name-1": 0,
    "account-name-2": 100
}
```

## Usage avanza_client.py

```shell
python avanza_client.py --headers headers.json --cookies cookies.json
```

```json
{
    "account-name-1": 0,
    "account-name-2": 100
}
```
