import re


def get_num_and_unit(s: str) -> (int, str):
    number_p = r'\d+'
    unit_p = r'[k|K|m|M]?[b|B]'

    return (int(re.search(number_p, s).group()), re.search(unit_p, s).group().upper())
