from unittest import TestCase

from src.infra.crosscutting.common.doc_id_util import DocIdUtil


class DocIdUtilTest(TestCase):

    def test_cpf_valid_number(self):
        self.assertTrue(DocIdUtil.validate_cpf('17763686901'))

    def test_cpf_invalid_number(self):
        self.assertFalse(DocIdUtil.validate_cpf('37763686901'))
        self.assertFalse(DocIdUtil.validate_cpf('3'))
        self.assertFalse(DocIdUtil.validate_cpf('abc'))
        self.assertFalse(DocIdUtil.validate_cpf('1a2b3c4d5e6'))
        self.assertFalse(DocIdUtil.validate_cpf('123456789123'))

    def test_cpf_null(self):
        self.assertFalse(DocIdUtil.validate_cpf(None))
        self.assertFalse(DocIdUtil.validate_cpf(''))

    def test_cpf_sequential_number(self):
        self.assertFalse(DocIdUtil.validate_cpf('00000000000'))
        self.assertFalse(DocIdUtil.validate_cpf('11111111111'))
        self.assertFalse(DocIdUtil.validate_cpf('22222222222'))
        self.assertFalse(DocIdUtil.validate_cpf('33333333333'))
        self.assertFalse(DocIdUtil.validate_cpf('44444444444'))
        self.assertFalse(DocIdUtil.validate_cpf('55555555555'))
        self.assertFalse(DocIdUtil.validate_cpf('66666666666'))
        self.assertFalse(DocIdUtil.validate_cpf('77777777777'))
        self.assertFalse(DocIdUtil.validate_cpf('88888888888'))
        self.assertFalse(DocIdUtil.validate_cpf('99999999999'))

