def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

def main():
    text = "A man a plan a canal Panama"
    print("Checking:", text)
    
    if is_palindrome(text):
        print("Result: IS a palindrome")
    else:
        print("Result: NOT a palindrome")

if __name__ == "__main__":
     main()