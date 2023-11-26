def print_upper_words(words, must_start_with={'h','y'}):
    """Prints each word on a separate line, but in all uppercase."""
    for word in words:
        print(word.upper())
    

def print_upper_words2(words):
    """Print each word uppercased on a separate line, but only if starts with E or e."""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


print_upper_words(['cat', 'dog', 'frog', 'hippo', 'turtle', 'yak'], must_start_with={'h','y'})

def print_upper_words3(words, must_start_with={'h','y'}):
    """Prints each word on a separate line, but in all uppercase."""
    for letter in must_start_with:
        chosen = letter.lower()
        for word in words:
            if(word.lower().startswith(chosen)):
                    print(word.upper())
   

        
