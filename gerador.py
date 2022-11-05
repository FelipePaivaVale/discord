import re
import random
from unicodedata import digit

def get_digit(cpf: str) -> int:
    lencpf = len(cpf) + 1

    multiplicantion = []
    for cpf_index, multiplier in enumerate(range(lencpf, 1, -1)):
        multiplicantion.append(int(cpf[cpf_index])*multiplier)

    total_sum = sum(multiplicantion)
    digit = 11 - (total_sum % 11)
    return digit if digit < 10 else 0

def get_digit1(cpf: str) -> int:
    return get_digit(cpf[:9])

def get_digit2(cpf: str) -> int:
    return get_digit(cpf[:10])

def remove_not_numbers(cpf: str) -> str:
    return re.sub(r'\D','', cpf)

def tem_onze_numeros(value: str) -> bool:
    return len(value) == 11

def sequencia(value: str) -> bool:
    return (value[0] * len(value)) == value

def is_valid(cpf: str) -> bool:
    clean_cpf = remove_not_numbers(cpf)

    if not tem_onze_numeros(clean_cpf):
        return False

    if sequencia(clean_cpf):
        return False

    digit_one = get_digit1(clean_cpf)
    
    digit_two = get_digit2(clean_cpf)

    new_cpf = f'{clean_cpf[:9]}{digit_one}{digit_two}'

    if new_cpf == clean_cpf:
        return True

    return False

def generate() -> str:
    nine_digits = ''.join([str(random.randint(0, 9)) for x in range(9)])
    digit_one = get_digit1(nine_digits)
    digit_two = get_digit2(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
    return new_cpf

def formater(cpf: str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

if __name__ == "__main__":
    cpf = generate()
    cpf_formatado = formater(cpf)
    print(cpf, cpf_formatado)