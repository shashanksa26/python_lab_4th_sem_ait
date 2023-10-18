binary_value = input("Enter the binary value : ")
octa_value = input("Enter the octa value: ")

def binary_to_decimal():
    decimal = int(binary_value,2)
    print(f"The decimal value of binary {binary_value} is = {decimal}")

def octa_to_hexa():
    decimal_eqivalent = int(octa_value,8)
    hexadecimal = hex(decimal_eqivalent)
    print(f"The hexadecimal value of octa {octa_value} is = {hexadecimal}")
binary_to_decimal()
octa_to_hexa()