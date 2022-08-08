from typing import List


def to_int(value: str | int) -> int:
    return value if isinstance(value, int) else int(value)


def get_elements(string_with_numbers: str) -> List[str]:
    return string_with_numbers.replace("|", "").split()
