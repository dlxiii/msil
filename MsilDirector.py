"""
API for fishery right data
Code: Yulong Wang
Date: Jun 17, 2022
"""

# external
import logging
# internal
import Msil

class MsilDirector:

    def __init__(self, name: str, where: str):
        self.name = name
        self.where = where
        self.builder = None

    def _set_builder(self):
        if self.name == 'Fishery Right':
            url = 'https://api.msil.go.jp/fishery/demarcated-fishery-right/'
        else:
            logging.debug('No matching database name')
        self.builder = Msil(
            url,
            self.where
            self.unit
        )

    def get(self):
        self._set_builder()
        return self.builder.get_df()

if __name__ == '__main__':

    name = 'Fishery Right'
    where = 'Hokkaidao'
    msil = MsilDirector(name, where)
    url = msil.get()
    print()