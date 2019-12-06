#!/usr/bin/env python
"""Avanza client."""
import json
import logging
import sys
import time
from random import randint

import begin

from avanza.avanza import Avanza

logger = logging.getLogger(__name__)


@begin.start(auto_convert=True)
@begin.logging
def run(headers=None, cookies=None, cron=False):
    """Login to Avanza and output account values as JSON."""
    root = logging.getLogger()
    hdlr = root.handlers[0]
    hdlr.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    if not headers:
        logger.error("Missing headers JSON file argument")
        sys.exit(1)

    if not cookies:
        logger.error("Missing cookies JSON file argument")
        sys.exit(1)

    with open(headers) as f:
        headers = json.load(f)

    with open(cookies) as f:
        cookies = json.load(f)

    # Only log requests warnings
    requests_log = logging.getLogger("requests")
    requests_log.setLevel(logging.WARNING)

    # Sleep for a random time if cron argument is set
    if cron:
        time.sleep(randint(0, 900))

    avanza = Avanza(headers, cookies)
    print(json.dumps(avanza.get_account_values()))
