from user_models import User
from exceptions import UserRegistrationError

def create_new_account(name, pwd):
    try:
        User(name, pwd)
    except UserRegistrationError as error:
        
        # Catch any registration error and print it nicely
        print(f"Registration Failed: {error}")

if __name__ == "__main__":
    # Should fail (Too short)
    create_new_account("Jo", "pass123")

    # Should fail (No digit)
    create_new_account("Alice", "password")

    # Should work
    create_new_account("Alice", "pass123")