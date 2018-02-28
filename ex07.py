# File : chaos.py
# A simple program illustrating chaotic behavios.

def main():
    print("This program illustrades a chaotic function")
    x,y = eval(input("Enter a two numbers between 0 and 1 separated by a comma: "))
    print("input",x,"  ",y)
    print("--------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(round(x,6),"  ",round(y,6))
main()

