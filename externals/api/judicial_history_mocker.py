import requests
from requests_mock import Mocker

JUDICIAL_RECORDS = ["66227711", "99771155", "00991154", "00011122"]

def get_judicial_history_mocker_response(nin):
    with Mocker() as mocker:
        if not nin in JUDICIAL_RECORDS:
            response = '{"message": "No judicial records found"}'
        else:
            response = '{"message": "One or more judicial records found."}'

        mocker.register_uri(
            "GET",
            f"http://example.com/judicial/history/{nin}",
            text=response,
            status_code=200,
        )
        return requests.get(f"http://example.com/judicial/history/{nin}").text
