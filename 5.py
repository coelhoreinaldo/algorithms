def reverse_string(input_string):
    reversed_list = []
    for char in input_string:
        reversed_list.insert(0, char)
    return "".join(reversed_list)


if __name__ == "__main__":
    input_string = input("Digite uma string:")
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")
