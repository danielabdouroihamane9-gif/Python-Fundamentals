#19 NESTED LOOPS: A loop within another loop (outer, inner)
#                   outer loop:
#                       inner loop:

for x in range(3):
    for x in range(0, 11):
        print(x, end=" ")
    print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbols = input("Enter the symbols: ")

for x in range(rows):
    for y in range(columns):
        print(symbols, end= " ")
    print()


