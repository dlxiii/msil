"""
API for fishery right data
Code: Yulong Wang
Date: Jun 17, 2022
"""
# external
import urllib.request
import json
import logging
# internal

class RawMsilData:

    def __init__(self):
        # list or string
        self.url = None
        self.hdr = {'Cache-Control': 'no-cache','Ocp-Apim-Subscription-Key': '0e83ad5d93214e04abf37c970c32b641'}
        self.data_js = None
        self.data_fg = None

    def _build_request(self):
        if self.name == 'Fishery Right':
            self.url = 'https://api.msil.go.jp/fishery/demarcated-fishery-right/v1/query?units=meter&returnGeometry=true'
        else:
            logging.deug('No matching data name')

if __name__ == '__main__':