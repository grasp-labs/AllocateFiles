"""
Module for configuration of fixed assets.

Define credentials by setting up environment variables, pull from secret store or other
options that fit your use case.
"""
import os
from dataclasses import dataclass
from typing import AnyStr


@dataclass
class Config:
    client_id: AnyStr = os.environ.get("GRASP_DEMO_CLIENT_ID")
    client_secret: AnyStr = os.environ.get("GRASP_DEMO_CLIENT_SECRET")
    grant_type: AnyStr = "client_credentials"
    token_url: AnyStr = "https://auth-dev.grasp-daas.com/oauth/token/"
    service_url: AnyStr = "http://localhost:8000/api/subscription/v1/allocate/upload-file/"# "https://grasp-daas.com/api/subscription/v1/allocate/upload-file/"


configuration = Config()
