from flask import make_response, jsonify
from flask_mail import Message
from config import mail, app


def flask_plain_email(recipient, subject, content, cc, bcc):
    with app.app_context():
        #Instantiate a new message
        msg = Message(recipients = [recipient, cc, bcc], subject= subject, body = content)
        try:
            res = mail.send(msg)
            response = {
                'status': 'success',
                'data':{
                    'message': 'Mail sent successfully'
                }
            }
            # return print(res)
            return make_response(jsonify(response), 201)
        except Exception :
            response = {
                'status': 'error',
                'data':{
                    'message': 'Error: Mail was not sent.'
                }
            }
            return make_response(jsonify(response), 500)



#Fucntion to send html/template mail using flask-mail
def flask_template_email(recipient, subject, content, cc, bcc):
    with app.app_context():
        #Instantiate a new message
        msg = Message(recipients = [recipient, cc, bcc], subject= subject, html = content)
        try:
            res = mail.send(msg)
            response = {
                'status': 'success',
                'data':{
                    'message': 'Mail sent successfully'
                }
            }
            # return print(res)
            return make_response(jsonify(response), 201)
        except Exception :
            response = {
                'status': 'error',
                'data':{
                    'message': 'Error: Mail was not sent.'
                }
            }
            return make_response(jsonify(response), 500)