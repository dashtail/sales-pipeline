import asyncio

from random import randint
from requests_mock import Mocker
from core.entities.person import PERSONS
from .national_registry_mocker import get_national_registry_mocker_response


class NationalRegistryAPI:
    async def get_person_by_NRI(self, nri):
        await asyncio.sleep(randint(1, 3))
        response = get_national_registry_mocker_response(nri)

        return response
