import re, pyperclip

# REGEX FOR PHONE NUMBERS
phone_regex = re.compile(
    r'''
    (
    # 415-555-0000, 555-0000, (912) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    # area code - optional
    ((\d\d\d)|(\(\d\d\d\)))?
    # first separator
    (\s|-)
    # first 3 digits
    \d\d\d
    # second separator
    -
    # final four digits
    \d\d\d\d
    # extension - optional
    (((ext(\.)?\s)|x)(\d{2,5}))?
    )
    ''',
    re.VERBOSE)

# CREATE REGEX FOR EMAIL ADDRESSES
email_regex = re.compile(
    r'''
    # some.+_thing@something.com - emails can have all kinds of crazy characters
    # name
    [a-zA-Z_.+]+[a-zA-Z0-9]*
    # @ symbol
    @
    # domain name 
    [a-zA-Z0-9_.+]+
    ''',
    re.VERBOSE)

# GET TEXT OFF CLIPBOARD
text = pyperclip.paste()
# EXTRACT EMAIL/PHONE FROM THIS TEXT
# COPY EXTRACTED EMAIL/PHONE TO THE CLIPBOARD
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phones = []
for phone_number in extracted_phone:
    all_phones.append(phone_number[0])
print('phone numbers are: ', '\n'.join(all_phones))
print('emails are: ', '\n'.join(extracted_email))
results = '\n'.join(extracted_email) + '\n'.join(all_phones)
pyperclip.copy(results)