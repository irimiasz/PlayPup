MINIMUM_USERNAME_LENGTH = 5
MINIMUM_PASSWORD_LENGTH = 8

STRONG_PASSOWRD_REGEX = (
    "(?=^.{"
    + str(MINIMUM_PASSWORD_LENGTH)
    + ",}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
)
