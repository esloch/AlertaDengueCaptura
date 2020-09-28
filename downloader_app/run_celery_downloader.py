#!/usr/bin/env python


import os
import sys

import pandas as pd

from downloader_app import shapefile_module as shpm
from downloader_app.tasks import add, download_source

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORK_DIR = os.path.join(BASE_DIR, "downloader_app")
sys.path.insert(0, WORK_DIR)


# Set the filepath and load in a shapefile.
SHP_PATH = os.path.join(
    WORK_DIR, "shape_region/RJ_Mun97_region/RJ_Mun97_region.shp"
)
DOWNLOADFILES_PATH = os.path.join(WORK_DIR, "DownloadedFiles")


try:
    add.delay(3, 5)
except Exception as e:
    print(e)


if __name__ == "__main__":
    pass


class DownloaderSources:
    def LandDAAC_v5_day():
        # Parameters
        # Extract bounding box from shapefile by uf
        point1, point2 = shpm.extract_shp_boundingbox(SHP_PATH)
        # iterate source list
        source = 'LandDAAC-v5-day'
        # date_start date_end last week
        # argparser(dt_start, dt_end)
        dates = (
            pd.date_range('2016-07-20', '2016-08-05', freq='8D')
            .strftime("%Y-%m-%d")
            .tolist()
        )
        print(dates)
        options = {
            'regrid': [3, 'cubic'],
            'keep_original': False,
            'time_series': True,
            'close_browser': True,
        }

        # Call taks
        download_source.delay(source, dates, point1, point2, options)

    def LandDAAC_v5_night():
        # Parameters
        # Extract bounding box from shapefile by uf
        point1, point2 = shpm.extract_shp_boundingbox(SHP_PATH)
        # iterate source list
        source = 'LandDAAC-v5-night'
        # date_start date_end last week
        # argparser(dt_start, dt_end)
        dates = (
            pd.date_range('2016-07-20', '2016-08-05', freq='8D')
            .strftime("%Y-%m-%d")
            .tolist()
        )
        print(dates)
        options = {
            'regrid': [3, 'cubic'],
            'keep_original': False,
            'time_series': True,
            'close_browser': True,
        }

        # Call taks
        download_source.delay(source, dates, point1, point2, options)


if __name__ == "__main__":
    DownloaderSources.LandDAAC_v5_day()
    # DownloaderSources.LandDAAC_v5_night()
