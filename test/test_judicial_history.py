import asyncio
import unittest
from externals.api.judicial_history_api import JudicialHistoryAPI
from core.entities.person import Person, NRI_PERSON_ONE
from core.utils.validate import validate_person_informations


class TestJudicialHistoryAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.person = Person(
            "00112233", "1992/07/25", "Peter", "Monteiro", "peter.monteiro@example.com"
        )

        self.another_person = Person(
            "00011122",
            "2000/01/01",
            "Maxwell",
            "Stone",
            "max.stone@example.com",
        )

        self.api = JudicialHistoryAPI()

    async def test_check_if_not_exist_any_judicial_records(self):
        response = await self.api.get_person_judicial_history(self.person.NRI)
        self.assertEqual(response, '{"message": "No judicial records found"}')
    
    async def test_check_if_exist_any_judicial_records(self):
        response = await self.api.get_person_judicial_history(self.another_person.NRI)
        self.assertEqual(response, '{"message": "One or more judicial records found."}')

    

if __name__ == "__main__":
    unittest.main()
