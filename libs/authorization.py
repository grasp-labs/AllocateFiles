"""Module for authorization."""
import base64
from typing import Dict

import requests

from config import configuration, Config


def _get_basic_auth_header(client_id, client_secret) -> Dict:
    """
    Function to create a Basic-Auth header object.
    @param client_id: Client ID.
    @param client_secret: Client secret.
    @return: Base64 encoded Authorization header.
    """
    credentials = "{0}:{1}".format(client_id, client_secret)
    auth_string = base64.b64encode(credentials.encode("utf-8"))
    auth_headers = {
        "Authorization": "Basic " + auth_string.decode("utf-8"),
    }
    return auth_headers


def get_access_token(config: Config) -> Dict:
    """
    Function to obtain an access token in a Oauth2.0 client credential grant flow.
    @param config: Configuration object.
    @return: Authorization header object.
    """
    basic_auth_headers = _get_basic_auth_header(
        client_id=configuration.client_id, client_secret=config.client_secret
    )
    data = {
        "grant_type": config.grant_type,
    }
    response = requests.post(configuration.token_url, data=data, headers=basic_auth_headers)
    if response.status_code != 200:
        raise PermissionError(
            f"Failed to collect application token {response.status_code}"
        )

    return {"Authorization": f"Bearer {response.json().get('access_token')}"}
