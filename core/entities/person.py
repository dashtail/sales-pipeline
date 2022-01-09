from datetime import datetime


class Person:
    def __init__(
        self,
        NRI: str,
        birth_date: datetime,
        first_name: str,
        last_name: str,
        email: str,
        prospect: bool = False,
        score: int = 0,
    ):
        self.NRI = NRI
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
            self.NRI == other.NRI
            and self.birth_date == other.birth_date
            and self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.email == other.email
        )


NRI_PERSON_ONE = Person(
    "00112233", "1992/07/25", "Peter", "Monteiro", "peter.monteiro@example.com"
)
NRI_PERSON_TWO = Person(
    "99887766", "1993/05/05", "LUCAS", "SILVA", "lucas.silva@example.com"
)
NRI_PERSON_THREE = Person(
    "11445599", "1993/01/19", "DAVID", "LUIS", "david.luis@example.com"
)

PERSONS = [NRI_PERSON_ONE, NRI_PERSON_TWO, NRI_PERSON_THREE]
