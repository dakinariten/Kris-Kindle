import random
import smtplib
import ssl
import csv
import datetime


def kriskind(kk_name_list):

    nameList = kk_name_list             # Set list to list passed in; no validation
    random.shuffle(nameList)            # Shuffle list for greater randomisation
    toBeAssignedList = nameList[:]      # Clone the list for assignment
    assignedList = []                   # List for output

# Iterate through the shuffled list
    for name in nameList:
        # Generate random number between 0 & number of elements in list
        hatDraw = random.randint(0, (len(toBeAssignedList) - 1))
        # If the index location is the same as the random num, the names are the same - must roll dice again
        while name == toBeAssignedList[hatDraw]:
            hatDraw = random.randint(0, (len(toBeAssignedList) - 1))
            # If it's the last element AND the only name left is their own, function called recursivley
            if int(nameList.index(name)) == int((len(nameList) - 1)) and name == toBeAssignedList[hatDraw]:
                return kriskind(nameList)
        # Temp variable - used to append assignedList
        assignedName = toBeAssignedList[hatDraw]
        assignedList.append(assignedName)
        # Remove name from list to prevent double assignments
        toBeAssignedList.remove(assignedName)
    # Temp variable - store 2D list; list 1 is all involved; list 2 is their kris kindle name
    returnList = [nameList, assignedList]
    return returnList


kkNameList = []                           # 1D List; manually typed, or replaced with file
# CSV File should be NAME in one COL, and EMAIL in another
with open('FILENAME.csv', 'r', encoding='utf-8-sig') as krisKindleDetails:
    name2Dlist = list(csv.reader(krisKindleDetails))

nameEmail = {}                              # Empty Dict; added in NAME: EMAIL pairs

for item in name2Dlist:
    nameEmail[item[0]] = item[1]
    kkNameList.append(item[0])

nameRes = kriskind(kkNameList)              # Call Function; 2D List returned

email_port = 465                            # For SSL
email_server_smtp = "smtp.gmail.com"        # Assuming using GMAIL
email_address_sender = ""                   # Enter your address
pword = ''                                  # Hardcoded password; replace with input if desired
currentYear = datetime.date.today().year    # Set year to variable

# Iterate through returned list to sort emails
for i, item in enumerate(nameRes[0]):
    # Search dictionary for name to retrieve email address
    receiver_email = nameEmail.get(item)
    # Set variable for name
    greetingName = item
    kkName = nameRes[1][i]

    message = f"""\
    SENDER NAME HERE

    Hello {greetingName},

    This may be a tad impersonal, considering a robot did it, but "not all robots are bad"!
    After exhaustive testing (read: reminding), this script has decided that for Christmas {currentYear}, you have:
    {kkName}

    Please note - there is no record of who has who, and there are no second chances.
    It is completely random, and I cannot tell you who you got...so please don't delete the email!

    Best regards,
    Robot Santa.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(email_server_smtp, email_port, context=context) as server:
        server.login(email_address_sender, pword)
        server.sendmail(email_address_sender, receiver_email, message)
