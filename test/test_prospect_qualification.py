import asyncio
import unittest

from unittest.mock import patch
from core.entities.person import Person, NIN_PERSON_TWO
from core.services.prospect import ProspectService
from externals.api.judicial_history_api import JudicialHistoryAPI
from externals.api.national_registry_api import NationalRegistryAPI
from externals.api.judicial_history_mocker import get_judicial_history_mocker_response
from externals.api.national_registry_mocker import get_national_registry_mocker_response


class TestProspectQualification(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.person = Person(
            "99887766", "1993/05/05", "LUCAS", "SILVA", "lucas.silva@example.com"
        )

        self.another_person = Person(
            "3344220000",
            "2000/01/01",
            "Paul",
            "Walker",
            "paul.walker@example.com",
        )

        self.prospect_service = ProspectService()

    @patch.object(JudicialHistoryAPI, "get_person_judicial_history")
    @patch.object(NationalRegistryAPI, "get_person_by_NIN")
    @patch.object(ProspectService, "get_score")
    async def test_person_prospect_qualification_score_greater_then_60(
        self, mock_get_score, mock_get_person_by_NIN, mock_get_person_judicial_history
    ):
        mock_get_person_judicial_history.return_value = (
            get_judicial_history_mocker_response("99887766")
        )
        mock_get_person_by_NIN.return_value = get_national_registry_mocker_response(
            "99887766"
        )
        mock_get_score.return_value = 75
        await self.prospect_service.qualification(self.person)
        self.assertGreaterEqual(self.person.score, 60)
        self.assertTrue(self.person.prospect)

    @patch.object(JudicialHistoryAPI, "get_person_judicial_history")
    @patch.object(NationalRegistryAPI, "get_person_by_NIN")
    @patch.object(ProspectService, "get_score")
    async def test_person_prospect_qualification_score_less_then_60(
        self, mock_get_score, mock_get_person_by_NIN, mock_get_person_judicial_history
    ):
        mock_get_person_judicial_history.return_value = (
            get_judicial_history_mocker_response("99887766")
        )
        mock_get_person_by_NIN.return_value = get_national_registry_mocker_response(
            "99887766"
        )
        mock_get_score.return_value = 32
        await self.prospect_service.qualification(self.person)
        self.assertLess(self.person.score, 60)
        self.assertFalse(self.person.prospect)

    @patch.object(JudicialHistoryAPI, "get_person_judicial_history")
    @patch.object(NationalRegistryAPI, "get_person_by_NIN")
    async def test_if_person_nin_not_exist_in_national_registry(
        self, mock_get_person_by_NIN, mock_get_person_judicial_history
    ):
        mock_get_person_judicial_history.return_value = (
            get_judicial_history_mocker_response("3344220000")
        )
        mock_get_person_by_NIN.return_value = get_national_registry_mocker_response(
            "3344220000"
        )

        with self.assertRaises(Exception, msg="Person not found in national registry"):
            await self.prospect_service.qualification(self.person)

    def test_if_score_is_generated_betweem_0_100(self):
        score = self.prospect_service.get_score([], self.person)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)


if __name__ == "__main__":
    unittest.main()
