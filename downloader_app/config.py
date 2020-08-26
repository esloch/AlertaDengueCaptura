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
    settings_yaml = {
        'client_config_backend': 'settings',
        'client_config': {
            'client_id': os.environ.get('CLIENT_ACCOUNT_ID'),
            'client_secret': os.environ.get('CLIENT_SECRET'),
            'auth_uri': "https://accounts.google.com/o/oauth2/auth",
            'token_uri': "https://oauth2.googleapis.com/token",
            'redirect_uri': [
                "http://localhost:8090/",
                "http://localhost:8080/",
            ],
        },
        'save_credentials': True,
        'save_credentials_backend': 'file',
        'save_credentials_file': 'credentials.json',
        'get_refresh_token': True,
        'oauth_scope': [
            'https://www.googleapis.com/auth/drive',
            "https://accounts.google.com/o/oauth2/auth",
        ],
    }

    # Generate configuration file for pyydrive authentication
    with open(os.path.join(SETTINGS_PATH), 'w') as f:
        yaml.dump(settings_yaml, f, default_flow_style=False)

    print('Please configure your settings file (%s).' % SETTINGS_PATH)

# Create client_secrets.json in downloader_app directory
if not os.path.exists(SECRETS_PATH):
    credentials_info = {
        "web": {
            "client_id": os.environ.get('CLIENT_ID'),
            "project_id": os.environ.get('PROJECT_ID'),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": os.environ.get('CLIENT_SECRET'),
            "redirect_uris": [
                "http://localhost:8090/",
                "http://localhost:8080/",
            ],
            "javascript_origins": [
                "http://localhost:8080",
                "http://localhost:8090",
            ],
        }
    }

    with open(os.path.join(SECRETS_PATH), 'w') as f:
        json.dump(credentials_info, f)
        print("The client_secrets.json file has ben created!")

# Create mycreds in downloader_app directory
if not os.path.exists(MYCREDS_PATH):
    with open(os.path.join(MYCREDS_PATH), 'w') as f:
        f.write("")
        f.close()
        print("The mycreds.txt file has ben created!")

# Create credentials in BASE_DIR
if not os.path.exists(TOKEN_PATH):
    token_info = {
        {
            "refresh_token": os.environ.get('REFRESH_TOKEN'),
        }
    }

    with open(os.path.join(TOKEN_PATH), 'w') as f:
        json.dump(token_info, f)
        print("The credentials file has ben created!")
