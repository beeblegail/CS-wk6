#Author: Abbey Pates
#Date: 25/02/2018
#Title: ************
#Version: 1.0
import re
#import dns.resolver

#These are taken from RFC5322 and are the official validation regexes
mailboxRegex = re.compile("(^[a-zA-Z0-9_.+-]+)")
fqdnRegex = re.compile("([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

def checkAddress(emailAddress):
   #split the email address by the @ symbol
   #e.g. cheesecake@chocolateteapot.101
   mailBox,mailDomain = emailAddress.split("@")
                          
   #check valid dns domain
   if not fqdnRegex.match(mailDomain):
      print("Check the domain of your email address.")
      #check valid mail domain (MX records), so there is at least one server
      #to send email to.
      return 0      
   elif not mailboxRegex.match(mailBox):
      #check if mailbox has valid characters
      print("Check your mail box (the bit before the @)")
   else:
      #there is no point in doing SMTP check for mailbox existence
      #since wide misuse means that it is blocked by most mail servers
      return 1
   
   

emailAddress = input("Please enter a valid email address:")

if checkAddress(emailAddress):
   print("Valid email address")
                     

                     
                     
