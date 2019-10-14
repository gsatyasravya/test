

from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField,SelectField,FileField,StringField
from wtforms.validators import DataRequired, IPAddress



class GenericFormTemplate(FlaskForm):

    source = SelectField(label='Credentials', choices=[('Please Select', 'Please Select'), ('Upload a CSV file', 'Upload a CSV file'),
                                                      ('Enter Manually', 'Enter Manually')])

    file1 = FileField(label='Please upload a CSV file')

    Address1 = StringField  (
                            label='IP Address ',
                            # is_disabled_on_start=False,
                            validators = [IPAddress(ipv4 = True, message = "Please check format of IP address")],
                            # enable_on_complete=['password']
                            )

    username1 = StringField   (
                                    label='Username',
                                    # is_disabled_on_start=False
                                    )

    password1 = PasswordField(
                            label='Password',
                            default='abc',
                            )

    add_user = SubmitField(label='ADD USER')
    remove_user = SubmitField(label='REMOVE USER')

    submit = SubmitField(label='SUBMIT')    
    save = SubmitField(label='SAVE DETAILS')

    datarake = SelectField(label='Datarake', 
                            choices=[('Please Select', 'Please Select'), ('Upload a Zip file', 'Upload a Zip file'),
                                                      ('File from machine', 'Files from machine')]
                            # enable_on_complete=['submit']
                            )
