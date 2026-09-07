def main():
    x = int(input("Enter Number: "))
    a = x // 100          # Hundreds digit
    b = (x // 10) % 10   # Tens digit
    c = x % 10           # Ones digit
    y = a + b + c
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
