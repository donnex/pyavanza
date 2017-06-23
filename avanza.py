import logging
import re

import bs4
import requests

logger = logging.getLogger(__name__)


class Avanza(object):
    BASE_URL = 'https://avanza.se'
    HEADERS = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.109 Safari/537.36'
    }

    def __init__(self, username, password):
        self.session = requests.Session()
        self.username = username
        self.password = password

        self.session.headers.update(self.HEADERS)

    def login(self):
        """Login to Avanza."""

        if not self.username or not self.password:
            logger.error('Missing Avanza login credentials (username: "%s", '
                         'password: "%s")', self.username, self.password)
            return False

        form_data = {
            'j_username': self.username,
            'j_password': self.password
        }

        req = self.session.post(self.BASE_URL + '/ab/handlelogin',
                                data=form_data)

        if req.status_code != requests.codes.ok:
            logger.error('Avanza login failed')
            logger.error(req.text)
            return False

        return True

    def _account_name_from_account_row(self, account_row):
        """Return a cleaned and parsed account name from account row."""

        account_name = account_row.select('.accountLabel')[0].text.strip()
        account_name = re.sub('[^0-9a-zA-Z]+', '-', account_name)

        return account_name

    def _account_balance_from_account_row(self, account_row):
        """Return a cleaned and parsed account balance from account row."""

        account_balance = account_row.select(
            '.totalValue')[0].text.strip().replace(u'\xa0', '')
        account_balance = int(account_balance)

        return account_balance

    def get_balances_all_accounts(self):
        """Fetch the balance page and return balance for accounts as dict."""

        req = self.session.get(
            self.BASE_URL + '/mina-sidor/kontooversikt.html')

        source = bs4.BeautifulSoup(req.content, 'html.parser')

        # Select and looop all accounts table rows
        balances = {}
        account_rows = source.select('.groupAccountTypeTable tbody tr')
        for account_row in account_rows:
            account_name = self._account_name_from_account_row(account_row)
            account_balance = self._account_balance_from_account_row(
                account_row)

            balances[account_name] = account_balance

        return balances
