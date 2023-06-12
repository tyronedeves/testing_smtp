import smtplib
import datetime as dt
import random
my_email = "walterenebeliuzor@gmail.com"
my_password = "aeuzsiljajaeogwk"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as qoute_file:
         all_qoutes = qoute_file.readlines()
         qoute = random.choice(all_qoutes)

    print(qoute)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"subject: Monday Motivation\n\n{qoute} ")
