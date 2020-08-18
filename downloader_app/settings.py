import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


EE_CREDENTIAL_FILE = os.path.join(
    BASE_DIR, 'downloader_app', 'alertadenguecaptura-7ec421287640.json'
)

EE_SERVICE_ACCOUNT = (
    'alertadengue-898@alertadenguecaptura.iam.gserviceaccount.com'
)
