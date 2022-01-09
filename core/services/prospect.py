import asyncio
import json
from random import randint

from core.utils.validate import validate_person_informations
from core.entities.person import Person
from externals.api.judicial_history_api import JudicialHistoryAPI
from externals.api.national_registry_api import NationalRegistryAPI

class ProspectService:
    async def qualification(self, person: Person):
        judicial_api = JudicialHistoryAPI()
        national_registry_api = NationalRegistryAPI()

        judicial_records, national_registry_response = await asyncio.gather(
            judicial_api.get_person_judicial_history(person.NIN),
            national_registry_api.get_person_by_NIN(person.NIN),
        )

        if national_registry_response.status_code == 200:
            nr_person = json.loads(national_registry_response.text)
            nr_person = Person(**nr_person)

            if validate_person_informations(person, nr_person):
                score = self.get_score(judicial_records, person)
                person.set_person_score(score)

            if person.score >= 60:
                person.set_person_as_prospect()

        else:
            raise Exception(national_registry_response.text)

    def get_score(self, judicial_records: list, person: Person) -> int:
        return randint(0, 100)
    