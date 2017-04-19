import sys
import mailbox
import csv
from email.header import decode_header
from bs4 import BeautifulSoup
import unicodedata

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
                    elif subpart.get_content_type() == 'text/html':
                        body = BeautifulSoup(subpart.get_payload(decode=True),"lxml").text
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
            elif part.get_content_type() == 'text/html':
                body = BeautifulSoup(part.get_payload(decode=True),"lxml").text
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    elif message.get_content_type() == 'text/html':
        body = BeautifulSoup(message.get_payload(decode=True),"lxml").text
    return body


if __name__ == "__main__":

    writer = csv.writer(open("clean_mail2.csv", "wb"))
    for message in mailbox.mbox("../DeepMail1/Sidd_April16.mbox"):
        m = get_message(message)
        contents = ''
        if isinstance(m, str):
            contents = m
        elif isinstance(m, unicode):
            contents = unicodedata.normalize('NFKD',m).encode('ascii','ignore')
        writer.writerow(["Subject" + str(message["subject"]), "From " + str(message["from"]), "Date " + str(message["date"]), 'Contents ' + contents])
