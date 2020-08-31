import json
import os
import sys

import yaml

from downloader_app.settings import BASE_DIR

EE_CREDENTIAL_FILE = os.path.join(
    BASE_DIR, 'downloader_app', 'alertadenguecaptura-7ec421287640.json'
)

EE_SERVICE_ACCOUNT = (
    'alertadengue-898@alertadenguecaptura.iam.gserviceaccount.com'
)


DOWNLADER_PATH = os.path.join(BASE_DIR, 'downloader_app')
SETTINGS_PATH = os.path.join(DOWNLADER_PATH, 'settings.yaml')
MYCREDS_PATH = os.path.join(DOWNLADER_PATH, 'mycreds.txt')
SECRETS_PATH = os.path.join(BASE_DIR, 'client_secrets.json')
TOKEN_PATH = os.path.join(BASE_DIR, 'credentials')


# create yaml file
if not os.path.exists(SETTINGS_PATH):
    settings_yaml = os.environ.get("SETTINGS_YAML")
    # Generate configuration file for pyydrive authentication
    with open(os.path.join(SETTINGS_PATH), 'w') as f:
        yaml.dump(settings_yaml, f, default_flow_style=False)
    print('The settings.yaml file has ben created')

# Create client_secrets.json in downloader_app directory
if not os.path.exists(SECRETS_PATH):
    credentials_info = os.environ.get('CREDENTIALS_INFO')
    with open(os.path.join(SECRETS_PATH), 'w') as f:
        json.dump(credentials_info, f)
        print("The client_secrets.json file has ben created!")

# Create mycreds in downloader_app directory
if not os.path.exists(MYCREDS_PATH):
    with open(os.path.join(MYCREDS_PATH), 'w') as f:
        mycreds_info = os.environ.get('MYCREDS_INFO')
        f.write(str(mycreds_info))
        f.close()
        print("The mycreds.txt file has ben created!")

# Create credentials in BASE_DIR
if not os.path.exists(TOKEN_PATH):
    token_info = {
        "refresh_token": os.environ.get('REFRESH_TOKEN'),
    }
    with open(os.path.join(TOKEN_PATH), 'w') as f:
        json.dump(token_info, f)
        print("The credentials file has ben created!")
