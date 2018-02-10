import re


class EmailUtil:

    @staticmethod
    def is_valid(email):

        if not email or len(email) < 5:
            return False

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return False

        return True
