from flask import abort, make_response, jsonify
from datetime import datetime
from config import db
from models import Person, PersonSchema
import sendgrid
import settings
import os
from sendgrid.helpers.mail import (Mail, From, To, Subject, Cc, Bcc, PlainTextContent, HtmlContent, Content, SendGridException, Email)
# #SMTP SERVER SETTINGS SENDGRID
SENDGRID_API_KEY = settings.SENDGRID_API_KEY

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY

#init schema
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


def sendemail(people):
    """
    This function sends email to subscriber/subscribers
    :param people:  person/people to send email to
    :return:        201 on success, 404 on error
    """
    mailing_list = []
    len_people = len(people)
    if people is not None:
        while len_people > 0:
            email = people.get('email')
            mailing_list.append(email)
            len_people -= 1
        mailing_group = list(dict.fromkeys(mailing_list))
        response = send_plain_email(mailing_group)
        return (response)
    

def send_plain_email(recipient):
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    from_email = Email("femiadenuga@mazzacash.com")
    to_email = To(recipient)
    subject = "Newsletter Email"
    plain_text_content=PlainTextContent('HNG Internship Newsletter Email')
    # html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>')
    # message.cc = Cc('test4@example.com')
    # message.cc = Bcc('test4@example.com')
    mail = Mail(from_email, to_email, subject, plain_text_content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

