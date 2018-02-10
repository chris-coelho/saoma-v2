from unittest import TestCase

from src.domain.services.customer_service import CustomerService
from src.infra.data.customer.customer_repository import CustomerRepository


class CustomerServiceTest(TestCase):

    def test_get_customer(self):
        customer_repo = CustomerRepository()
        customer_service = CustomerService(customer_repo)

        self.assertIsNotNone(customer_service.get_customer('418f5f846e1149e28b5f5310bc7ea8c5'))
