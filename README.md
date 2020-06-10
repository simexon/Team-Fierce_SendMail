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

<p align="center"> SendMail is a microservice project implemented to aid the process email notifications to mailing subscribers, email notifications.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

SendMail is a microservice project implemented to aid the process email notifications to mailing subscribers, email notifications. SendMail offers the options of sending emails in plain text format or using html template. SendMail components are decoupled in functionality.



## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

To run the software locally you need Python interpreper (version 3.xx) installed on your machine.

```
www.python.org
```

To start the sytem navigate to the project folder,
Open the terminal and execute python server.py
Open the link of local server on the terminal in the browser,
Enter the endpoints specified below to access the different actions

The SendMAil API includes the following endpoints:

1. /api/v1/people 
   This endpoint responds to a request for /api/v1/people
   with the complete lists of people

2. /api/v1/people/{email} 
    This endpoint responds to a request for /api/v1/people/{email}
    with the details of a person or delete action status
    :param email:   email address of person to get details about or delete

3. /api/v1/people/{person} 
    This endpoint creates a new person in the people structure
    based on the passed in person data
    :param person:   person object to create

4. /api/v1/people/{email, people}
    This endpoint updates an existing person in the people structure

5. /api/v1/sendmail
    This endpoint sends a plain email to subscriber/subscribers

6. /api/v1/sendmailwithtemplate
    This endpoint sends a template email to subscriber/subscribers
    

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


## 🎈 Usage <a name="usage"></a>

To checkout the endpoints, navigate to the endpoint url as specified at [Getting Started](#getting_started) section

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language
- [Flask](https://flask.palletsprojects.com/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@Team-Fierce](https://github.com/gblend/Team-Fierce_SendMail) - Idea & Initial work


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration

