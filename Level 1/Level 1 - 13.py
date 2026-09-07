def main():
    x = int(input("Enter Number: "))
    a = x // 10   # Tens digit
    b = x % 10    # Ones digit
    y = b * 10 + a
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
