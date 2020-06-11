import sendgrid
import settings
import os
from sendgrid.helpers.mail import (Mail, From, To, Subject, Cc, Bcc, PlainTextContent, HtmlContent, Content, SendGridException, Email)

def sendgrid_plain_email(recipient):
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
    return response