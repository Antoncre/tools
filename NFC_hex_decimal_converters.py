# This type of conversion comes handy when you need to convert values
# from ACR122U to format that is read by ACR1281U-C2 and vice-versa
# Can also have many other use cases

# Converts little-endian to hex
def to_hex(little_endian: int):
    two_digits = ''
    hex_ = ''
    for _ in range(8):
        remainder = little_endian % 16
        match remainder:
            case 10:
                remainder = 'a'
            case 11:
                remainder = 'b'
            case 12:
                remainder = 'c'
            case 13:
                remainder = 'd'
            case 14:
                remainder = 'e'
            case 15:
                remainder = 'f'

        little_endian = int(little_endian / 16)
        two_digits = str(remainder) + two_digits
        if len(two_digits) == 2:
            hex_ += str(f'{two_digits} ')
            two_digits = ''
    return hex_.strip()

# converts hex to little-endian
def to_little_endian(hex_: str):
    try:
        int_little = int(hex_)
    except ValueError:
        little_hex = bytearray.fromhex(hex_)
        little_hex.reverse()
        str_little = ''.join(format(x, '02x') for x in little_hex)
        int_little = int(str_little, 16)
    return int_little