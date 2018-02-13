from unittest import TestCase, mock

from src.domain.modules.customer_module.customer import Customer
from src.domain.services.customer_service import CustomerService


class CustomerServiceTest(TestCase):

    def test_get_customer(self):
        mock_customer_repo = mock.Mock()
        mock_customer_repo.get_by_id.return_value = Customer('23164217765',
                                                             'Maria Rita',
                                                             'maria.rita@test.com',
                                                             '418f5f846e1149e28b5f5310bc7ea8c5')
        customer_service = CustomerService(mock_customer_repo)

        customer = customer_service.get_customer('418f5f846e1149e28b5f5310bc7ea8c5')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'Maria Rita')

