
def digits(num):
    digit = num % 10
    num_last = digit

    num = num // 10

    while num > 0:
             digit = num % 10
             num = num // 10
             num_last = num_last * 10 + digit
    return num_last

print(digits(1010))
print(digits(999999999999))
print(digits(12345))
print(digits(900000008))




