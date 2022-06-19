"""
API for fishery right data
Code: Yulong Wang
Date: Jun 17, 2022
"""

# external
import json
import pandas as pd
# internal
from UmiShiruAPI.rawData import RawData

class UmiShiru:
    def __init__(self, name: str):
        self.data_js = None
        self.data_df = None
        self.data_raw = RawData(name).get_data()

    def get_js(self):
        # Change raw data to json format
        self.data_js = json.loads(self.data_raw)
        return self.data_js

    def get_df(self):
        # Change json data to df format
        self.data_js = self.get_js()
        self.data_df = pd.json_normalize(self.data_js["features"])
        self.data_df["geometry.rings"] = self.data_df["geometry.rings"].apply(lambda x: [tuple(xy) for xy in x[0]])
        self.data_df['geometryType'] = self.data_js['geometryType']
        self.data_df['spatialReference.wkid'] = self.data_js['spatialReference']['wkid']
        self.data_df.rename(columns = {'attributes.都道府県': 'attributes.prefectures'}, inplace=True)
        return self.data_df

if __name__ == '__main__':
    name = 'Demarcated Fishery Right'
    data_raw = UmiShiru(name).get_df()
    print()
'''
    'displayFieldName': '都道府県',
    'fieldAliases': {'都道府県': '都道府県'},
    'geometryType': 'esriGeometryPolygon',
    'spatialReference': {'wkid': 4326, 'latestWkid': 4326},
    'fields': [{'name': '都道府県', 'type': 'esriFieldTypeString', 'alias': '都道府県', 'length': 254}],
    'features':[]
'''