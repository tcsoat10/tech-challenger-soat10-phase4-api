from src.core.ports.customer.i_customer_repository import ICustomerRepository
from src.core.domain.entities.customer import Customer
from src.core.exceptions.entity_not_found_exception import EntityNotFoundException
from src.application.usecases.customer_usecase.is_customer_usecase import IsCustomerUsecase


class GetCustomerByIdUsecase:
    def __init__(self, customer_gateway: ICustomerRepository):
        self.customer_gateway = customer_gateway

    @classmethod
    def build(cls, customer_gateway: ICustomerRepository) -> 'GetCustomerByIdUsecase':
        return cls(customer_gateway)
    
    def execute(self, customer_id: int, current_user: dict) -> Customer:
        if IsCustomerUsecase.is_customer(current_user) and int(current_user['person']['id']) != customer_id:
            raise EntityNotFoundException(entity_name='Customer')
        
        customer = self.customer_gateway.get_by_id(customer_id)
        if not customer:
            raise EntityNotFoundException(entity_name='Customer')
        return customer