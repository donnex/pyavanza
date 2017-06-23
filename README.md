# pyavanza

A simple Python library for accessing your balance from Avanza. It uses web scraping to login and to parse the data.

## Usage

```
import json

from avanza import Avanza

avanza = Avanza(USERNAME, PASSWORD)
avanza_login_ok = avanza.login()

if avanza_login_ok:
    current_balances = avanza.get_balances_all_accounts()
    print(json.dumps(current_balances))

{"Account name 1": 0, "Account name 2": 100}
```
