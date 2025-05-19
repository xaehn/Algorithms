def to_decimal(number: str, base: int) -> int:
    return int(number, base)

def from_decimal(number: int, base: int) -> str:
    if number == 0:
        return "0"
    else:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while 0 < number:
            result = digits[number % base] + result
            number //= base

        return result

def convert_base(number: str, original: int, target: int) -> str:
    return from_decimal(to_decimal(number, original), target)