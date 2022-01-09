from datetime import datetime


class Person:
    def __init__(
        self,
        NIN: str,
        birth_date: datetime,
        first_name: str,
        last_name: str,
        email: str,
        prospect: bool = False,
        score: int = 0,
    ):
        self.NIN = NIN
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.prospect = prospect
        self.score = score

    def set_person_as_prospect(self):
        self.prospect = True

    def set_person_score(self, score):
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (
            self.NIN == other.NIN
            and self.birth_date == other.birth_date
            and self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.email == other.email
        )


NIN_PERSON_ONE = Person(
    "00112233", "1992/07/25", "Peter", "Monteiro", "peter.monteiro@example.com"
)
NIN_PERSON_TWO = Person(
    "99887766", "1993/05/05", "LUCAS", "SILVA", "lucas.silva@example.com"
)
NIN_PERSON_THREE = Person(
    "11445599", "1993/01/19", "DAVID", "LUIS", "david.luis@example.com"
)

PERSONS = [NIN_PERSON_ONE, NIN_PERSON_TWO, NIN_PERSON_THREE]
