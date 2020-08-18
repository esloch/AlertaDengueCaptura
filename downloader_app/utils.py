import os

import ee

from downloader_app.settings import EE_CREDENTIAL_FILE, EE_SERVICE_ACCOUNT


def ee_authenticate():
    if not os.path.exists(EE_CREDENTIAL_FILE):
        raise Exception("CREADENTIAL FILE DOESN'T EXIST")
    raise
    credentials = ee.ServiceAccountCredentials(
        EE_SERVICE_ACCOUNT, EE_CREDENTIAL_FILE
    )
    ee.Initialize(credentials)
