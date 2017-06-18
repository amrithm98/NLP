#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'f2b67b34d8824bbfafbde3d2f2a48c8e'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    request.session_id = "tejan-amrith"

    request.query="Get me the image of a cat with milk"

    response = request.getresponse()

    print (response.read())


if __name__ == '__main__':
	main()
