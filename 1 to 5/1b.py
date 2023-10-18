num = int(input("num:"))
num_str = str(num)
reverse_str = num_str[::-1]
if num_str == reverse_str:
    print(f"The no. {num} is a Palindrome")
else:
    print(f"The no. {num} is not a Palindrom")

# for occurence
print("The occurence for each number in the given input:")
for r in set(num_str):
    num_str.count(r)
    print(f"{r}= {num_str.count(r)}")