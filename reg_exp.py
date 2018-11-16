import re
str = 'vaibhav-yadav.python@dsadf3422ess.com'
match = re.search(r'[\w.-]+@[\w.-]+',str)
if match:
  print 'found ', match.group()
else:
  print ('not found.')