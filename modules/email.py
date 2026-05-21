def email_scan(email):
    return f"""
email report

email: {email}

google:
https://www.google.com/search?q={email}

breach:
https://haveibeenpwned.com/
"""
