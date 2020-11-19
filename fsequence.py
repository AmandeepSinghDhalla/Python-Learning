def main():
    print("Enter the nth term for fibonacci sequence")
    n = int(input("Enter: "))
    for n in range(0,n):
        print(f"{fs(n)}", " ", end="")

term_cache = {}

def fs(n):
    if n in term_cache:
        return  term_cache[n]

    if n == 0:
        term = 0
    elif n == 1:
        term = 1
    elif n > 1:
        term = fs(n - 1) + fs(n - 2)

    term_cache[n] = term
    return term

main()