"""
API for fishery right data
Code: Yulong Wang
Date: Jun 17, 2022
"""

# external
import logging
# internal
from msil import Msil

class MsilDirector:

    def __init__(self, name: str, area = None):
        self.name = name
        self.area = area
        self.builder = None

    def _set_builder(self):
        if self.area == "HKD":
            self.prefecture = ["Hokkaido"]
        elif self.area == "THK":
            self.prefecture = ["Akita", "Aomori", "Fukushima", "Iwate", "Miyagi", "Yamagata"]
        elif self.area == "TKY":
            self.prefecture = ["Chiba", "Gunma", "Ibaraki", "Kanagawa", "Saitama", "Tochigi", "Tokyo"]
        elif self.area == "CHB":
            self.prefecture = ["Aichi", "Fukui", "Gifu", "Ishikawa", "Nagano", "Niigata", "Shizuoka", "Toyama", "Yamanashi"]
        elif self.area == "KNS":
            self.prefecture = ["Hyogo", "Kyoto", "Mie", "Nara", "Osaka", "Shiga", "Wakayama"]
        elif self.area == "CGK":
            self.prefecture = ["Hiroshima", "Okayama", "Shimane", "Tottori", "Yamaguchi"]
        elif self.area == "SKK":
            self.prefecture = ["Ehime", "Kagawa", "Kochi", "Tokushima"]
        elif self.area == "KYU":
            self.prefecture = ["Fukuoka", "Kagoshima", "Kumamoto", "Miyazaki", "Nagasaki", "Oita", "Okinawa", "Saga"]
        else:
            logging.debug('No matching area name')
        self.builder = Msil(
            self.name
        )

    def get(self):
        self._set_builder()
        return self.builder.get_df()

if __name__ == '__main__':

    name = 'Demarcated Fishery Right'

    msil = MsilDirector(name)
    df = msil.get()
    print()