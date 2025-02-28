import re


def check_password_strength(password):
    strength = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special_characters': False
    }

    if len(password) >= 8:
        strength['length'] = True

    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True

    if re.search(r'[a-z]', password):
        strength['lowercase'] = True

    if re.search(r'\d', password):
        strength['numbers'] = True

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength['special_characters'] = True

    return strength


def assess_strength(strength):
    feedback = []

    if not strength['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not strength['uppercase']:
        feedback.append("Password should contain at least one uppercase letter.")
    if not strength['lowercase']:
        feedback.append("Password should contain at least one lowercase letter.")
    if not strength['numbers']:
        feedback.append("Password should contain at least one number.")
    if not strength['special_characters']:
        feedback.append("Password should contain at least one special character.")

    return feedback


def password_strength_tool():
    print("Welcome to the Password Strength Checker Tool!")
    password = input("Enter a password to check its strength: ")

    strength = check_password_strength(password)

    feedback = assess_strength(strength)

    if not feedback:
        print("Password is strong!")
    else:
        print("Your password is weak. Here's why:")
        for f in feedback:
            print(f)


if __name__ == "__main__":
    password_strength_tool()
