import re, paperclip

#create regex for phone numbers
phoneRegex = re.compile(r'''
((\d\d\d) | (\(\d\d\d\)))?  # area code with or without paranthesis (optional)

[a-zA-Z0-9_.+]+         #name part
@           # @ symbol
[a-zA-Z0-9_.+]+         #domain name part
''', re.VERBOSE)
#Create regex for email addresses

emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+         #name part
@           # @ symbol
[a-zA-Z0-9_.+]+         #domain name part
''', re.VERBOSE)

#test of clipboard
text = paperclip.paste()

