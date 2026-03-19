from exceptions import UsernameTooShortError, WeakPasswordError

class User:
    def __init__(self, username, password):
        
        # Check username length
        if len(username) < 3:
            raise UsernameTooShortError(f"Username '{username}' is too short.")

        # Check password strength (1 letter + 1 digit)
        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)

        if not (has_letter and has_digit):
            raise WeakPasswordError("Password must contain at least 1 letter and 1 digit.")

        # Success
        self.username = username
        self.password = password
        print(f"User '{self.username}' successfully created!")