def converttobinary(n):
    if n > 1:
        converttobinary(n//2 )
print(n%2 , end= " ")

dec = float(input("enter a number to find its binary value"))

converttobinary(dec)
print()

dec=float(input("enter a number to find its binary value"))

def converttobinary(n//2 ):
    if n > 1:
        converttobinary(n//2 )
    print(n%2 , end= " ")

converttobinary(dec)
print()