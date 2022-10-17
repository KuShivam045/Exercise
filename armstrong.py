a = int(input("Enter the number \t"))
sum = 0
order = len(str(a))
copy_a = a
while a>0:
    digit = a % 10
    sum += digit ** order
    a = a//10

if (sum == copy_a):
    print(f"{copy_a} is The number Armstrong number")
else:
    print(f"{copy_a} is not an Armstrong number")
