def is_even(x):
    return x % 2 == 0


input_list = range(1, 100)
for x in input_list:
    if is_even(x):
        # Print usando f-strings. É similar à interpolação que existe no JS/TS
        print(f"{x} é par")
    else:
        print(f"{x} é ímpar")

