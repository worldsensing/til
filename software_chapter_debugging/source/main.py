#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import logging

from configurelogging import ConfigureLogging
from configmanager import ConfigManager


logger = logging.getLogger(__name__)
config = ConfigManager().configuration


TILTMETER_COS_RESPONSE = {
    "custom_fields": {
        "axis_one": {
            "time": "2018-10-30T14:20:00Z",
            "type": "timeseries",
            "value": -18.146667
        },
        "axis_two": {
            "time": "2018-10-30T14:20:00Z",
            "type": "timeseries",
            "value": -0.587853
        },
        "coordinates": {
            "coordinates": [41.380858, 2.141304],
            "type": "Point"
        },
        "date": {
            "type": "date", "value": "2018-10-30T14:20:00Z"
        },
        "loadsensing_tiltmeter_id": {
            "type": "external_id",
            "value": "7292"
        },
        "temperature": {
            "time": "2018-10-30T14:20:00Z",
            "type": "timeseries",
            "value": 24.1
        }
    },
    "id": 1,
    "refs": {},
    "type": "loadsensing_tiltmeter"
}


def main():
    import pdb
    pdb.set_trace()

    # import ipdb
    # ipdb.set_trace()

    # import pudb
    # pudb.set_trace()

    # pretty printed
    pp = pprint.PrettyPrinter()
    pp.pprint(TILTMETER_COS_RESPONSE)

    # logger
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.error("This is an error log")

    # curlify
    import curlify
    import requests
    response = requests.get("http://google.com")
    curl = curlify.to_curl(response.request)
    print(curl)


if __name__ == "__main__":
    ConfigureLogging(**config["logger"])
    main()
