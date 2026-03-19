# Base class for all our app errors
class UserRegistrationError(Exception):
    pass

# Specific error for short usernames
class UsernameTooShortError(UserRegistrationError):
    pass

# Specific error for weak passwords
class WeakPasswordError(UserRegistrationError):
    pass