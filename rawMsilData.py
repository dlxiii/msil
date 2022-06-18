"""
API for fishery right data
Code: Yulong Wang
Date: Jun 17, 2022
"""
# external
import urllib.request
import logging
# internal

class RawMsilData:

    def __init__(self, name: str):
        # list or string
        self.name = name
        self.hdr = {'Cache-Control': 'no-cache','Ocp-Apim-Subscription-Key': '0e83ad5d93214e04abf37c970c32b641'}
        self.data_raw = None
        self.data_js = None
        self.data_fg = None

    def _build_request(self):
        if self.name == 'Demarcated Fishery Right':
            # 区画漁業権
            self.url = 'https://api.msil.go.jp/fishery/demarcated-fishery-right/v1/query?units=meter&returnGeometry=true'
        elif self.name == 'Common Fishery Right':
            # 共同漁業権
            self.url = 'https://api.msil.go.jp/fishery/demarcated-fishery-right/v1/query?units=meter&returnGeometry=true'
        elif self.name == 'Fixed Gear Fishery Right':
            # 定置漁業権
            self.url = 'https://api.msil.go.jp/fishery/fixed-gear-fishery-right/v1/query?units=meter&returnGeometry=true'
        else:
            logging.deug('No matching data name')
        self.req = urllib.request.Request(self.url, headers=self.hdr)
        return self.req

    def get_data(self):
        self._build_request()
        self.req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(self.req)
        self.data_raw = response.read()
        return self.data_raw

    def get_fig(self):
        # todo: supporting figure query
        pass

if __name__ == '__main__':
    name = 'Common Fishery Right'
    data_raw = RawMsilData(name).get_data()
    print()
