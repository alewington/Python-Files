# Try & Except with Raise

# Raise is a way to throw an exception.
# It can be used in any place where you want to stop the program and give an
# error message.

password: str = "123456"


def password_strength(password):
    if len(password) < 10:
        raise Exception(" password is too short")


password_strength(password)
print('Program Complete')


# Please notice the error message when run.
