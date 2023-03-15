# config
COOKIE_MAX_AGE = 3600

# validation
MINIMUM_PASSWORD_LENGTH = 8
MINIMUM_USERNAME_LENGTH = 5
STRONG_PASSWORD_REGEX = (
    "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{"
    + str(MINIMUM_PASSWORD_LENGTH)
    + ",}$"
)

# error messages
MESSAGE_USERNAME_TOO_SHORT = (
    f"Username should be at least {MINIMUM_USERNAME_LENGTH} characters long"
)
MESSAGE_USERNAME_STARTS_WITH_NUMBER = "Username cannot start with a number"
MESSAGE_PASSWORD_TOO_WEAK = (
    f"Password is not strong enough. Should have: at least {MINIMUM_PASSWORD_LENGTH} signs, "
    f"at least one capital letter, at least one digit, and at least one special character"
)
