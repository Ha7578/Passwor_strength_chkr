import re

def check_password_strength(password):
    # Define the strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate overall strength
    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    feedback = []

    # Provide suggestions
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# User input
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}/5")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")
