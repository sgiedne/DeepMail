import sys
import mailbox
import csv
from email.header import decode_header
import mail_extract3

infile = './Sidd_April16.mbox'
outfile = './Sidd_April16.csv'

def get_message(message):
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
                        print body
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                print body
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
        print body
    return body


if __name__ == "__main__":

    # writer = csv.writer(open("clean_mai1.csv", "wb"))
    for message in mailbox.mbox("../DeepMail1/Sidd_April16.mbox"):
        print get_decoded_email_body(message)
        # writer.writerow(["Subject" + str(message["subject"]), "From" + str(message["from"]), "Date" + str(message["date"]), contents])
