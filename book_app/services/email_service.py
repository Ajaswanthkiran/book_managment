import smtplib



def sendmail(recipient,title,author,publisher):
    mail=smtplib.SMTP('smtp.gmail.com',587)


    print(recipient)

    mail.ehlo()

    mail.starttls()

    sender="a.jaswanthkiran@gmail.com"
    
    recipient="a.jaswanthkiran123@gmail.com"
    
    mail.login(sender,'aqcxcyboqcyrnrgz')

    header='To:'+recipient+'\nFrom:'\
                +sender+'\nSubject: Book Added Successfully\n'

    content=header+f"\nThe Title:{title} added to the list successfully\n Author: {author}\nPublisher: {publisher}"
    mail.sendmail(sender,recipient,content)
    mail.close


if __name__=="__main__":
    sendmail("asd","ajk","ajk","ajk")