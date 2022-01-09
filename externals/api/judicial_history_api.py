import asyncio
from random import randint

from .judicial_history_mocker import get_judicial_history_mocker_response


class JudicialHistoryAPI:
    async def get_person_judicial_history(self, nri):
        await asyncio.sleep(randint(1, 3))
        response = get_judicial_history_mocker_response(nri)

        return response
