import smtplib
my_email="subhendudemo@gmail.com"
password="ldfewiopivgqkwyw"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()#transport layer security to secure email server
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="ssadhikari1512@gmail.com",
                        msg="Subject:hello\n\n Dude hii")
