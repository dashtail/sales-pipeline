from datetime import date
from core.entities.person import Person

def validate_person_informations(person: Person, nr_person: Person) -> bool:
    #validate if match the person informations stored in database.
    return person == nr_person