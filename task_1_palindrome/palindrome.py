def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    print(is_palindrome("довод"))  
    print(is_palindrome("А роза упала на лапу Азора"))  
    print(is_palindrome("программирование"))