#password strength checker
import re
# password strength check condtions:
# min 8 chars, digit, upperqcase, lowercase, special char
""""""
def check_password_strength(password):
    if len(password) < 8:
        return "weak: password must be at least 8 characters long"

    if not any(char.isdigit() for char in password):
        return "weak: password must contain at least one digit"

    if not any(char.isupper() for char in password):
        return "weak: password must contain at least one uppercase letter"

    if not any(char.islower() for char in password):
        return "weak: password must contain at least one lowercase letter"

    if not any(char in "!@#$%^&*()-+" for char in password):
        return "medium: password must contain at least one special character"

    return "strong: password meets all criteria"


def password_checker():
    """
    mmain function ti take user input and check password strength.
    """
    print("welcome to the password strength checker!!!")

    while True:
        password = input("\nEnter your password to check its strength (or type 'exit' to quit):")
        if password.lower() == "exit":
            print("Thank you for using the password strength checker!!!")
            break

        result = check_password_strength(password)
        print(result)

#run the password checker
if __name__ == "__main__":
    password_checker()