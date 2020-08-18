import pandas as pd

from downloader_app.tasks import download


def main():
    # Parameters
    point1 = [-44.88834, -20.763056]
    point2 = [-40.957431, -23.367102]
    source = 'LandDAAC-v5-day'
    dates = pd.date_range('2016-07-20', '2016-10-30', freq='8D')
    # import pdb; pdb.set_trace()
    options = {
        'plot': True,
        'keep_original': True,
        'regrid': [3, 'bilinear'],
        'close_browser': True,
    }

    # Call funcrion
    download.delay(source, dates.to_list(), point1, point2, options)

    print("ee initialized!!!")


if __name__ == "__main__":
    main()
