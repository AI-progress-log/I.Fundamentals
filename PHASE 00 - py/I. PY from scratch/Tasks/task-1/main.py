def validate_email(email: str):
    if not email:
        return False

    if email.count("@") != 1:
        return False

    else:
        dot_index = email.find(".")
        at_index = email.find("@")

        if dot_index == -1:
            return False

        if dot_index < at_index:
            return False

    return True


def extract_username(email: str):
    if email:
        at_index = email.find("@")
        if at_index != -1:
            username = email[:at_index]
            return username

    return ""


def extract_domain(email: str):
    at_index = email.find("@")
    dot_index = email.rfind(".")
    if at_index != -1 and dot_index != -1:
        return email[at_index + 1 : dot_index]

    return ""


def classify_domain(email: str):
    dot_index = email.rfind(".")
    if dot_index != -1:
        domain = email[dot_index:]

        if domain == ".com":
            return "Commercial Domain"

        elif domain == ".edu":
            return "Educational Domain"

        else:
            return "Other Domain"

    return ""


##############################################
## Task2,3,4 ##


def extract_core(message: str):
    if message:
        core = ""
        for symbol in message:
            if (
                (symbol >= "A" and symbol <= "Z")
                or (symbol >= "a" and symbol <= "z")
                or (symbol == " ")
            ):
                core += symbol
        return core
    return ""


def reverse_words(message: str):
    if message:
        reversed_message = ""
        for i in reversed(message):
            reversed_message += i
        return reversed_message
    return ""


def replace_vowels(message: str):
    if message:
        vowels = ["I", "E", "A", "U", "O", "U"]
        replaced_string = ""

        for char in message:
            if char in vowels:
                idx = vowels.index(char)

                char = vowels[idx + 1]

            replaced_string += char

        return replaced_string
    return ""


def main():
    print("Hello from p2!")


if __name__ == "__main__":
    main()
