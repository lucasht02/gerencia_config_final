import re

class Validator:
    def is_email_valid(self, email):
        """
        Retorna True se o email estiver em um formato válido:
        texto@texto.dominio
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def is_password_strong(self, password):
        """
        Considera senha forte se tiver:
        - ao menos 8 caracteres
        - ao menos uma letra maiúscula
        - ao menos um dígito
        """
        pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
        return bool(re.match(pattern, password))