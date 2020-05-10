
import re
import pyperclip

#create regex for phone numbers


phoneRegex = re.compile(r'''
(((\d\d\d) | (\(\d\d\d\)))?  # area code with or without paranthesis (optional)
(\s|-)      #space or dash
(\d\d\d)    #first 3 digits
(\s|-)      #space or dash
(\d\d\d\d)    #last 4 digits
(((ext(\.)?\s) | x)   #extension txt part
(\d{2,5}))? )    #extension digit part''', re.VERBOSE)
#Create regex for email addresses

emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+         #name part
@           # @ symbol
[a-zA-Z0-9_.+]+         #domain name part
''', re.VERBOSE)

#test of clipboard
text = pyperclip.paste()

#Extract
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

phoneNumbers = []
for phoneNumber in extractedPhone:
    phoneNumbers.append(phoneNumber[0])

#copies results into clipboard
pyperclip.copy('\n'.join(phoneNumbers) + '\n'.join(extractedEmail))


