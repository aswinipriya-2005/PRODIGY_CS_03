import re

def assess_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
   
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    
    if criteria_met == 0:
        strength = "Very Weak"
    elif criteria_met == 1 or criteria_met == 2:
        strength = "Weak"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    
    feedback = {
        "length": length_criteria,
        "uppercase": uppercase_criteria,
        "lowercase": lowercase_criteria,
        "number": number_criteria,
        "special": special_criteria
    }
    
    return strength, feedback


def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Criteria Met:")
    for criterion, met in feedback.items():
        print(f"  {criterion.capitalize()}: {'Yes' if met else 'No'}")

if _name_ == "_main_":
    main()
