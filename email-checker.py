#Author: Abbey Pates
#Date: 25/02/2018
#Title: ************
#Version: 1.0
import re
import dns.resolver

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
      return 0
   
   #check valid mail domain (MX records), so there is at least one server
   #to send email to.
   try:
      records = dns.resolver.query(mailDomain+".", 'MX')
      if len(str(records[0].exchange)) == 0:
         print("Invalid mail domain!")
         return 0 
   except(dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
      print("Invalid mail domain!")
      pass
      return 0
   
   #check if mailbox has valid characters
   if not mailboxRegex.match(mailBox):
      print("Check your mail box (the bit before the @)")
      return 0
   
   #there is no point in doing SMTP check for mailbox existence
   #since wide misuse means that it is blocked by most mail servers
   #So would need to send one use mail verficaction link.
   return 1
   
   

emailAddress = input("Please enter a valid email address:")

if checkAddress(emailAddress):
   print("Valid email address")
                     

                     
                     
