from flask import abort, make_response, jsonify
from datetime import datetime
from config import db
from models import Person, PersonSchema

#init schema
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


def sendemail_with_template(people):
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
    return (mailing_group)