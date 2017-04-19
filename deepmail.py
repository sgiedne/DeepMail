import sys
import mailbox
import csv
from email.header import decode_header

infile = './Sidd_April16.mbox'
outfile = './Sidd_April16.csv'

def get_message(message):
    if not message.is_multipart():
        return message.get_payload()
    contents = ""
    for msg in message.get_payload():
        contents = contents + str(msg.get_payload()) + '\n'
    return contents

if __name__ == "__main__":

    writer = csv.writer(open("clean_mail.csv", "wb"))
    for message in mailbox.mbox("./Sidd_April16.mailbox"):
        contents = get_message(message)
        writer.writerow([message["subject"], message["from"], message["date"],contents])