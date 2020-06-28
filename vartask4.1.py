def convert_to(num, to_type=None):
    TYPES = {
        'bin': '{:b}',
        'oct': '{:o}',
        'hex': '{:x}'
        }
    try:
        num = int(''.join(c for c in str(num) if c.isdigit()))
    except ValueError as e:
        num = 0
    if to_type and to_type in TYPES.keys():
        return TYPES[to_type].format(num)
    else:
        return num


print(convert_to(num=17, to_type='bin'))
print(convert_to(num=17, to_type='oct'))
print(convert_to(num=17, to_type='hex'))
print(convert_to(num=17, to_type='unsupported'))
print(convert_to(num=17))
print(convert_to(num='not a number'))
print(convert_to(num=''))
print(convert_to(num=None))
