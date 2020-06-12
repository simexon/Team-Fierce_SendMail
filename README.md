<p align="center">
  <a href="" rel="noopener">
 <!-- <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a> -->
 <img width=200px height=200px src="" alt="SendMail"></a>
</p>

<h3 align="center">SendMail</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/gblend/Team-Fierce_SendMail.svg)](https://github.com/gblend/Team-Fierce_SendMail/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/gblend/Team-Fierce_SendMail.svg)](https://github.com/gblend/Team-Fierce_SendMail/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> SendMail is a microservice project to aid the process of sending email notifications to individual/multiple individuals/mailing list subscribers seamless.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

SendMail is a microservice project to aid the process of sending email notifications to mailing list subscribers. SendMail offers the options of sending emails in plain text format or using html template. SendMail components are decoupled in functionality.



## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run the software locally you need <strong>Python interpreter</strong> (version 3.xx) installed on your machine.

```
www.python.org
```

-To start the system navigate to the project folder, 
<br>
-Open the terminal/cmd and run => <strong>pip install -r requirements.txt</strong> (To install dependencies)
<br>
-On the terminal/cmd execute => <strong>python server.py<strong>
<br>
-Open the link of the local server on the terminal in the browser,
<br>
-Enter the endpoints specified below to access the different actions

The SendMAil API includes the following endpoints:
 <br><br>
 <img width=1000 height=600px src="https://github.com/gblend/Team-Fierce_SendMail/blob/master/static/images/documentation_ui.PNG?raw=true" alt="Project logo"></a>
<br><br>
=>   /v1/documentation
    This endpoint responds with a json version of all endpoint documentation
<br>
=>   /v1/configure
    @Todo ...
1. /v1/sendmail/people 
   This endpoint responds to a request for /v1/sendmail/people
   with the complete lists of people
<br>
2. /v1/sendmail/people/{email} 
    This endpoint responds to a request for /v1/sendmail/people/{email}
    with the details of a person or delete action status
    :param email:   email address of person to get details about or delete
<br>
3. /v1/sendmail/people/{person} 
    This endpoint creates a new person in the people structure
    based on the passed in person data
    :param person:   person object to create
<br>
4. /v1/sendmail/people/{email, people}
    This endpoint updates an existing person in the people structure
<br>
5. /v1/sendmail
    This endpoint sends a plain email to subscriber/subscribers
<br>
6. /v1/sendmailwithtemplate
    This endpoint sends a template email to subscriber/subscribers


## 🎈 Usage <a name="usage"></a>

To checkout the endpoints, navigate to the endpoint url as specified at [Getting Started](#getting_started) section

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language
- [Flask](https://flask.palletsprojects.com/) - Web Framework
- [jQuery](https://jquery.com/) - jQuery

## ✍️ Authors <a name = "authors"></a>

- [@Team-Fierce](https://github.com/gblend/Team-Fierce_SendMail) - Idea & Initial work


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to everyone whose code was used.

