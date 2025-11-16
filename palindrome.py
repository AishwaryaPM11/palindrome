import sys

def is_palindrome(s: str) -> bool:
    import re
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def main():
    if len(sys.argv) > 1:
        inp = " ".join(sys.argv[1:])
        print(f"Input (from args): {inp}")
    else:
        try:
            inp = input("Enter a string: ")
        except EOFError:
            print("No input available. Exiting.")
            sys.exit(1)

    if is_palindrome(inp):
        print("Result: The given string IS a palindrome.")
    else:
        print("Result: The given string is NOT a palindrome.")

if _name_ == "_main_":
    main()