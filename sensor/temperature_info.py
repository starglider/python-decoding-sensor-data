from house_info import HouseInfo
from datetime import (date, datetime)


class TemperatureData(HouseInfo):

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super("temperature", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super("temperature", rec_date)
        return self._convert_data(recs)