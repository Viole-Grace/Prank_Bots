import smtplib
from smtplib import SMTPException

import time

def spam_and_kill(from_title, to_email, to_name, number_of_mails):


  my_email = 'example@gmail.com'
  password = 'sample_password'

  message = """From: Pornhub Inquiry Team <pornhub.karnataka@gmail.com>
To: {} <{}>
MIME-Version: 1.0
Content-type: text/html
Subject: Warning - Inappropriate Pornography

Dear {},
<br>
Greetings!
<br>
Pornhub has noticed some objectionable material in your search history. Some of the material watched has been flagged as child pornography.<br>
For your reference, child pornography is any material that may involve sexual depiction of underage individuals. 
<br><br>
This is a warning. Please adhere to norms of cyber intelligence.<br>
<br><br>
To confirm, reply to this mail with 'Received'.
<br><br>
Not {} ? Report inconvenience at Pornhub@India

""".format(to_name, to_email, to_name, to_name)

  i = 0
  while True:
    i+=1

    try:
      print(message+str('\n'))
      smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
      smtpObj.ehlo(); smtpObj.starttls(); smtpObj.ehlo();  
      smtpObj.login(my_email, password)
      smtpObj.sendmail(my_email, to_email, message)
      smtpObj.quit()         
      print ("Successfully sent email to {} {} times\n".format(to_email, i))
    except SMTPException as e:
      print ("{} - Error: unable to send email".format(e))
    time.sleep(1) #sends a mail every 1 second

    if(i==number_of_mails):
      return

spam_and_kill('Me','sample@gmail.com','Pranked Friend', 450) #gmail has a 500 mail/day limit. Keep it under 500.