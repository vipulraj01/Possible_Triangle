a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))
# if a + b is less than or equal to b + a and b - b
if a+b>=c and b+c>=a and c+a>=b:
    print("Triangle is possible")
else:
    print("Triangle is not possible")
