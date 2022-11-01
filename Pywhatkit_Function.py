import pywhatkit as kit

def info():
    query = input("Enter your Command : ")
    print(kit.info(query,lines=3))
if __name__ == "__main__":
    info()    

def search():
    query = input("Enter your Command : ")
    kit.search(query)
if __name__ == "__main__":
    search()

def mail():
    mail_to = input("Whom do you want send the mail : ")
    content = input("Content ; ")
    kit.sendMail('adityasatapathy603@gmail.com','19.06.2004',mail_to,content)
if __name__ == "__main__":
    mail()