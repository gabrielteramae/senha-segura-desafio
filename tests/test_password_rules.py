import unittest
from app.password_rules import validate_password

class PasswordRulesTest(unittest.TestCase):
    def test_senha_forte_nao_tem_erro(self):
        self.assertEqual(validate_password("Senha123!"), [])

    def test_senha_curta_sem_numero_lista_as_falhas(self):
        errors = validate_password("abc")
        self.assertTrue(any("8 caracteres" in item for item in errors))
        self.assertTrue(any("digito" in item for item in errors))

if __name__ == "__main__":
    unittest.main()
