import random, pandas, yagmail
from datetime import datetime

my_email = "testpythonmailer1@gmail.com"
password = "xxxxxxxxxxx"
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_doc:
        contents = letter_doc.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        # initializing the server connection
    try:
        yag = yagmail.SMTP(user=my_email, password=password)
        # sending the email
        yag.send(to=birthday_person["email"],
                 subject='Happy Birthday',
                 contents=f"{contents}")
        print("Email sent successfully")
    except:
        print("Error, email was not sent")
