# Automatic Mail Sender
This is a python script which i have written to send emails to many people all at once with each of them not knowing about the mail address of any other person.
<br>
In this i have created a flask app which has a function which can be called with the help of a loop and in that function the recipients can be passed.<br>
Here i have passed the recipients in the function from a csv file which reads the data into a dataframe variable and then the values are take from the respective mail column,in my case df['emails].<br>The csv file which have used here has my various mail ids on which i have sent emails.
<br>
You can either pass simple body to the email in case you want to make the sent mail look simple.<br>
If you want the sent mail to look good and display a html page you can use that too.For this you have to make a templates folder in the root directory and in that you can create your html file.This is necessary because it is a flask app.<br>
If you have any incorrect email in the database then a mail from google will be sent to you saying the address does not exist.
You will get a critical security alert for the first time when you are using it.You just have to tap on "Yes,It was me".<br>
Sometimes there is a case that still the mails are not sent then you can [click here](https://myaccount.google.com/lesssecureapps), login with the respective mail and turn on less secure app.<br>
Note:- Gmail allows only 500 mails to be sent in a day. There may be a case that this shows mails are being sent but if limit is reached mails won't be sent.For a safer side keep the list under 500.
