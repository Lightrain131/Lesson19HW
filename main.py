# A program that asks for a base and a power
# Then the program should print the answer LIKE 2*2*2=8
def calculation(base, power):  # Calculate the result
    result = base ** power
    return result


def expression():  # Regard the whole expression as a string
    exp = str(base)
    for x in range(1, power):
        exp += "*" + str(base)
    return exp


base = int(input("Please give me a base: "))  # Ask for base and power
power = int(input("Please give me a power: "))

print(expression(), "=", calculation(base, power))

quit()
