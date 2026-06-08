def reverse(input_str):
    # Reverse the string and swap the case of characters
    reversed_str = input_str[::-1].swapcase()
    return reversed_str
print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))
