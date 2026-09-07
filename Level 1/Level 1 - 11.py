def main():
    x = int(input("Enter Number: "))
    tens = x // 10
    ones = x % 10
    y = tens + ones
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
