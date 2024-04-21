import json

with open('../osvar/email.txt') as f:
    a = f.read()
email = json.loads(a)

#print(email['name'])


import sys
import os.path
import smtplib

if len(sys.argv) <= 2:
    print('Usage:')
    print('  $ python ' + sys.argv[0] + ' mailfrom rcptto <emlfile>')
    print
    print('Parameter:')
    print('  mailfrom: MAIL FROM address.')
    print('  rcptto:   RCPT TO address.')
    print('  emlfile:  Message file in eml format. When emlfile is not specified, an empty message will be send.')
    print
    print('Example:')
    print('  $ python ' + sys.argv[0] + ' mailfrom@example.com rcptto@example.com mail.eml')
    #sys.exit(0)
    

server = 'localhost'
port = 25
mailfrom = sys.argv[0]
#rcptto = sys.argv[1].split(',')
print(sys.argv)
