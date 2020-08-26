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


# create yaml file
if not os.path.exists(SETTINGS_PATH):
    settings_yaml = {
        'client_config_backend': 'settings',
        'client_config': {
            'client_id': 'alertadengue-898@alertadenguecaptura.iam.gserviceaccount.com',
            'client_secret': "UtGbw1kGcikW-QUaQzUg2-Hy",
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
            "client_id": "1067506997807-0as4uropo9u6jjatu8660k7q14g0l757.apps.googleusercontent.com",
            "project_id": "alertadenguecaptura",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "UtGbw1kGcikW-QUaQzUg2-Hy",
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
    mycreds_info = "{'access_token': 'ya29.a0AfH6SMDj_548JxXTbTFikT524Mt3QeUeh2GAYeGlob6JEEEhQc95dYZUtnqofkcgYsfj44yZlrEZlF0RB0WRfD-YBaW519azxbEkBjPWIocLev4I7lg7lJEDI2Phuz3Sqi-nD77GdUwr5IzX5AkYg-GlmSJv7IC2GSM', 'client_id': '1067506997807-0as4uropo9u6jjatu8660k7q14g0l757.apps.googleusercontent.com', 'client_secret': 'UtGbw1kGcikW-QUaQzUg2-Hy', 'refresh_token': null, 'token_expiry': '2020-08-26T13:10:20Z', 'token_uri': 'https://oauth2.googleapis.com/token', 'user_agent': null, 'revoke_uri': 'https://oauth2.googleapis.com/revoke', 'id_token': null, 'id_token_jwt': null, 'token_response': {'access_token': 'ya29.a0AfH6SMDj_548JxXTbTFikT524Mt3QeUeh2GAYeGlob6JEEEhQc95dYZUtnqofkcgYsfj44yZlrEZlF0RB0WRfD-YBaW519azxbEkBjPWIocLev4I7lg7lJEDI2Phuz3Sqi-nD77GdUwr5IzX5AkYg-GlmSJv7IC2GSM', 'expires_in': 3599, 'scope': 'https://www.googleapis.com/auth/drive', 'token_type': 'Bearer'}, 'scopes': ['https://www.googleapis.com/auth/drive'], 'token_info_uri': 'https://oauth2.googleapis.com/tokeninfo', 'invalid': false, '_class': 'OAuth2Credentials', '_module': 'oauth2client.client'}"
    with open(os.path.join(MYCREDS_PATH), 'w') as f:
        f.write(mycreds_info)
        f.close()
        print("The mycreds.txt file has ben created!")
