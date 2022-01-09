import asyncio
import json
import unittest
from externals.api.national_registry_api import NationalRegistryAPI
from core.entities.person import Person, NRI_PERSON_ONE
from core.utils.validate import validate_person_informations


class TestNationalRegistryAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.person = Person(
            "00112233", "1992/07/25", "Peter", "Monteiro", "peter.monteiro@example.com"
        )

        self.another_person = Person(
            "000111",
            "2000/01/01",
            "Maxwell",
            "Stone",
            "max.stone@example.com",
        )

        self.api = NationalRegistryAPI()

    async def test_check_if_person_exist_in_national_registry(self):
        response = await self.api.get_person_by_NRI(self.person.NRI)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, json.dumps(NRI_PERSON_ONE.__dict__))

    async def test_check_if_person_not_exist_in_national_registry(self):
        response = await self.api.get_person_by_NRI(self.another_person.NRI)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, "Person not found in national registry")


if __name__ == "__main__":
    unittest.main()
