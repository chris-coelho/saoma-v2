import re


class DocIdUtil:

    @staticmethod
    def validate_cpf(doc_id):
        # extract just numbers
        cpf = ''.join(re.findall('\d', str(doc_id)))

        if (not cpf) or (len(cpf) < 11):
            return False

        # check if not a sequential numbers as 11111111111..99999999999
        if cpf in [''.join([str(j) for i in range(0, 11)]) for j in range(0, 10)]:
            return False

        # Check digits calculator (last 2 digits)
        doc_calculated = list(cpf[:9])
        while len(doc_calculated) < 11:
            mod = (sum([(len(doc_calculated)+1-k) * int(v) for k, v in enumerate(doc_calculated)])) % 11

            digit = 11 - mod
            if digit > 9:
                digit = 0
            doc_calculated.append(str(digit))

        # check if doc_calculated and original doc_id matches
        return ''.join(doc_calculated) == cpf

