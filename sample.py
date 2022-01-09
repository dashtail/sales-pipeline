import sys
import asyncio
from core.services.prospect import ProspectService
from core.entities.person import NRI_PERSON_ONE


async def main():
    prospect_service = ProspectService()
    await prospect_service.qualification(NRI_PERSON_ONE)
    print(NRI_PERSON_ONE.__dict__)


asyncio.run(main())
