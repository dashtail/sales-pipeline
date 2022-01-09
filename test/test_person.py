import asyncio
import unittest

from core.entities.person import Person, NRI_PERSON_ONE
from core.utils.validate import validate_person_informations


class TestPerson(unittest.TestCase):
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

    def test_valid_person_informations(self):
        self.assertTrue(validate_person_informations(self.person, NRI_PERSON_ONE))

    def test_invalid_person_informations(self):
        self.assertFalse(
            validate_person_informations(self.another_person, NRI_PERSON_ONE)
        )

  
if __name__ == "__main__":
    unittest.main()
