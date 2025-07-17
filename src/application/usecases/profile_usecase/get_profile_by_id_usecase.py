from src.core.ports.profile.i_profile_repository import IProfileRepository
from src.core.domain.entities.profile import Profile
from src.core.exceptions.entity_not_found_exception import EntityNotFoundException


class GetProfileByIdUsecase:
    def __init__(self, profile_gateway: IProfileRepository):
        self.profile_gateway = profile_gateway

    @classmethod
    def build(cls, profile_gateway: IProfileRepository):
        return cls(profile_gateway)
    
    def execute(self, profile_id: int) -> Profile:
        profile = self.profile_gateway.get_by_id(profile_id)
        if not profile:
            raise EntityNotFoundException(entity_name='Profile')
        
        return profile