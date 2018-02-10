from unittest import TestCase

from src.infra.crosscutting.common.email_util import EmailUtil


class EmailUtilTest(TestCase):

    def test_valid_email(self):
        self.assertTrue(EmailUtil.is_valid('test@test.com'))

    def test_invalid_email(self):
        self.assertFalse(EmailUtil.is_valid(None))
        self.assertFalse(EmailUtil.is_valid(''))
        self.assertFalse(EmailUtil.is_valid('t.co'))
        self.assertFalse(EmailUtil.is_valid('testtest.com'))


