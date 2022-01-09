import json
import requests

from random import randint
from requests_mock import Mocker
from core.entities.person import PERSONS

def get_national_registry_mocker_response(nri):
    with Mocker() as mocker:
        data = [x for x in PERSONS if x.NRI == nri]
        if data:
            data = json.dumps(data[0].__dict__)
            status_code = 200
        else:
            data = 'Person not found in national registry'
            status_code = 404

        mocker.register_uri(
            "GET",
            f"http://example.com/person/{nri}",
            text=data,
            status_code=status_code,
        )

        return requests.get(
            f"http://example.com/person/{nri}",
        )