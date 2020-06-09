from flask import render_template
import config

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


@connex_app.route('/')
def home():
    return render_template('home.html')


@connex_app.route('/sendemail')
def send_email():
    return render_template('create.html')




if __name__ == '__main__':
    connex_app.run(host='127.0.0.1', port=3000, debug=True)