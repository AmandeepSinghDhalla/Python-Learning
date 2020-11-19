def main():
    print("Enter the nth term for fibonacci sequence")
    n = int(input("Enter: "))
    for n in range(0,n):
        print(f"{fs(n)}", " ", end="")


def fs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fs(n - 1) + fs(n - 2)

main()