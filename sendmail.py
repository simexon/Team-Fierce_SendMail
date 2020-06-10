from flask import abort, make_response, jsonify
from datetime import datetime
from flask_mail import Message
from config import db, mail, app
from models import Person, PersonSchema
import sendgrid
import settings
import os
from sendgrid.helpers.mail import (Mail, From, To, Subject, Cc, Bcc, PlainTextContent, HtmlContent, Content, SendGridException, Email)

#init schema
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


def sendemail(mail_object):
    """
    This function sends email to subscriber/subscribers
    :param people:  person/people to send email to
    :return:        201 on success, 404 on error
    """
    
    if mail_object is not None:
        sender = mail_object.get('sender')
        subject = mail_object.get('subject')
        recipient = mail_object.get('recipient')
        body = mail_object.get('body')
        bcc = mail_object.get('bcc')
        cc = mail_object.get('cc')
        
        response = flask_plain_email(recipient, subject, body, cc, bcc, sender)
        return response
    

# def sendgrid_plain_email(recipient):
#     sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
#     from_email = Email("femiadenuga@mazzacash.com")
#     to_email = To(recipient)
#     subject = "Newsletter Email"
#     plain_text_content=PlainTextContent('HNG Internship Newsletter Email')
#     # html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>')
#     # message.cc = Cc('test4@example.com')
#     # message.cc = Bcc('test4@example.com')
#     mail = Mail(from_email, to_email, subject, plain_text_content)
#     response = sg.client.mail.send.post(request_body=mail.get())
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
    
    
    
def flask_plain_email(recipient, subject, content, cc, bcc, reply_to):
    #Instantiate a new message
    with app.app_context():
        msg = Message(recipients = [recipient], subject= subject, body = content, cc = cc, bcc = bcc, reply_to = reply_to)
        # msg.subject = subject
        # msg.add_recipient(recipient)
        # # msg.cc = cc
        # # msg.add_bcc = bcc
        # msg.body = content
        
        # with mail.connect() as conn:
        #     for recipient in recipient:
        #         message = '...'
        #         subject = "hello, %s" % recipient.name
        #         msg = Message(recipients=[recipient.email],
        #                     body=message,
        #                     subject=subject)

        #         conn.send(msg)
        try:
            res = mail.send(msg)
            print(msg)
        except Exception :
            print('Failed')
