import re

# ---------------------------
# Extract Email
# ---------------------------
def extract_email(text):
    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    if email:
        return email[0]

    return "Not Found"


# ---------------------------
# Extract Phone Number
# ---------------------------
def extract_phone(text):

    phone = re.findall(r'(\+91[- ]?)?[6-9]\d{9}', text)

    if phone:
        if isinstance(phone[0], tuple):
            return ''.join(phone[0])
        return phone[0]

    return "Not Found"


# ---------------------------
# Extract Name
# ---------------------------
def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2:

            if line.lower() not in [
                "resume",
                "curriculum vitae",
                "education",
                "skills",
                "projects",
                "experience"
            ]:
                return line

    return "Not Found"


# ---------------------------
# Extract Education
# ---------------------------
def extract_education(text):

    education_keywords = [

        "bca",
        "b.tech",
        "b.e",
        "mca",
        "m.tech",
        "mba",
        "bsc",
        "msc",
        "phd"

    ]

    text = text.lower()

    found = []

    for edu in education_keywords:

        if edu in text:
            found.append(edu.upper())

    return found


# ---------------------------
# Extract Experience
# ---------------------------
def extract_experience(text):

    pattern = r'(\d+)\+?\s*(year|years|yrs)'

    exp = re.findall(pattern, text.lower())

    if exp:

        return exp[0][0] + " Years"

    return "Fresher"