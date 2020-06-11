from flask import render_template, request, make_response, jsonify, redirect
from markupsafe import Markup, escape
import config
from mail.flask_mail import flask_plain_email, flask_template_email, mail
from flask_mail import Message
from config import mail


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


@connex_app.route('/')
def documentation():
    return redirect('/v1/ui')

@connex_app.route('/v1/documentation')
def json_documentation():
    return redirect('/v1/swagger.json')


@connex_app.route('/v1/configure')
def key_value_json():
    return redirect('/v1/ui')

@connex_app.route('/v1/sendmail/interface')
def home():
    return render_template('home.html')

@connex_app.route('/v1/sendmail/demo')
def send_email():
    return render_template('create.html')


@connex_app.route('/sendmail/html', methods=['POST'])
def sendmail_html():
    if request.method == 'POST':
        subject = Markup.escape(request.form['subject'])
        message = '<strong>'+ request.form['message'] +'</strong>'
        recipients = request.form['recipients']
        mail_list = recipients.split(',')
        len_list = len(mail_list) - 1
        if recipients != '' or message != '' or subject != '':
            with mail.connect() as conn:
                while len_list > -1:
                    msg = Message(recipients=[mail_list[len_list]], html=message, subject=subject)
                    
                    try:
                        conn.send(msg)
                        response = {
                            'status': 'success',
                            'data':{
                                'message': 'Mail sent successfully'
                            }
                        }
                        status = 200
                    except Exception:
                        response = {
                            'status': 'error',
                            'data':{
                                'message': 'Error: Mail was not sent.'
                            }
                        }
                        status = 500
                    len_list -= 1
                return make_response(jsonify(response), status)


@connex_app.route('/sendmail/text', methods=['POST'])
def sendmail_text():
    if request.method == 'POST':
        subject = Markup.escape(request.form['subject'])
        message = Markup.escape(request.form['message'])
        recipients = request.form['recipients']
        mail_list = recipients.split(',')
        len_list = len(mail_list) - 1
        if recipients != '' or message != '' or subject != '':
            with mail.connect() as conn:
                while len_list > -1:
                    msg = Message(recipients=[mail_list[len_list]], body=message, subject=subject)
       
                    try:
                        conn.send(msg)
                        response = {
                            'status': 'success',
                            'data':{
                                'message': 'Mail sent successfully'
                            }
                        }
                        status = 200
                    except Exception:
                        response = {
                            'status': 'error',
                            'data':{
                                'message': 'Error: Mail was not sent.'
                            }
                        }
                        status = 500
                    len_list -= 1
                return make_response(jsonify(response), status)
                    
    

if __name__ == '__main__':
    connex_app.run(host='127.0.0.1', port=3000, debug=True)