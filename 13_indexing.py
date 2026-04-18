#13 INDEXING: Accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]
credit_number = "1234-2552-8790-4578"
print(credit_number[5])
print(credit_number[1:5])
print(credit_number[3::2])
print(credit_number[::3])
''' Read from right to left '''
print(credit_number[-1])
''' Exercise '''
last_digits = "1234-2552-8790-4578"
reverse_numbers = "1234-2552-8790-4578"
print(f"xxxx-xxxx-xxxx-{last_digits[-4:]}")
print(f"Reverse number is: {reverse_numbers[::-1]})")