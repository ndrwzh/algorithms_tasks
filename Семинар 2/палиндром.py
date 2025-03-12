from collections import deque

def is_palindrome_deque(text):
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    if not processed_text:
        return True 
    d = deque(processed_text)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

