from colorama import Fore, Style

def mul(a, b):
    r = a * b
    return r
def div(a, b):
    r = a / b
    return r
def add(a, b):
    r = a + b
    return r
def sub(a, b):
    r = a - b
    return r

result = div(mul(add(1, 2), 3), 4)

print("\n", Style.BRIGHT + "*" * 32, sep = "")
print(Style.RESET_ALL + Fore.GREEN + "The Function Returned --- ", Style.BRIGHT, + result)
print(Style.BRIGHT + Fore.RESET+ "*" * 32, "\n")

