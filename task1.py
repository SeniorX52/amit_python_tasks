def validate_email(email):
    """
    This function validates if an email address meets the following conditions:
    1. It contains exactly one '@' symbol.
    2. It contains at least one '.' (dot) after the '@' symbol.

    If any of these conditions are not met, the function will return "Invalid email".
    If the conditions are met, the function will return "Valid email".

    :param email: str - The email address to validate.
    :return: str - "Valid email" if the email passes validation, otherwise "Invalid email".
    """
    if email.count("@") != 1:
        return "Invalid email"

    local_part, domain_part = email.split('@')

    if '.' not in domain_part:
        return "Invalid email"

    return "Valid Email"

# Example usage of the function
email_address = "Amit_ml@gmail.edu"
validation_result = validate_email(email_address)
print(validation_result)
