from smtplib import SMTP
import imaplib
from email.message import EmailMessage
from email import message_from_bytes
studentdic = {'Alice': 'alice@example.com', 'Bob': 'bob@example.com'}
graderdic = {'Adam': 'adam@example.com'}
#Put your test addresses here
testdic = {'John':'john.doe@example.com', 'Jane': 'jane.doe@example.com'}
username = 'me@example.com'
password = 'Your password'
smtp_host = "your_smtp_host"
smtp_port = your_smtp_port
reminder_file = 'reminder.txt' #For reminders
def plainsendemail(email, subject, message, attachment = None):
    server = SMTP(host = smtp_host, port = smtp_port)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    msg = EmailMessage()
    msg['From'] = fromaddress
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(message)
    if attachment != None:
        with open(attachment,'rb') as file:
            data = file.read()
            msg.add_attachment(data, maintype='application/pdf', subtype='pdf',filename = attachment)
    server.send_message(msg)
    server.quit()
def sendemail(first_name, dic, subject, message, attachment = None):
    final_message = 'Hi ' + first_name + ',\n\n' + message + '\n\nCheers,\nCalculus-chan'
    plainsendemail(dic[first_name], subject, final_message, attachment)

def anonsendemail(email, subject, message, attachment = None):
    final_message = 'Hello,\n\n' + message + '\n\nCheers,\nCalculus-chan'
    plainsendemail(email, subject, final_message, attachment)
    
def emailall(dic, subject, message, attachment = None):
    for person in dic:
        sendemail(person, dic, subject, message, attachment)
def emaillist(name_list, dic, subject, message, attachment = None):
    for person in name_list:
        sendemail(person, dic, subject, message, attachment)
def hwlatereminder(name_list, dic, hwset):
    emaillist(name_list,dic,'HW ' + hwset + ' will be due at the end of today!',"It seems that I still don't have your HW. If you haven't turned it in yet please do it by 11:59PM today.")    
def hwearlyreminder(dic, hwset, date):
    emailall(dic,'HW ' + hwset + ' will be due on ' + date,"This is a friendly reminder that HW " + hwset + " will be due on " + date + '. Please feel free to ask questions on Piazza, email <YOUR_NAME>, come to office hours or visit evening help sessions to get your questions about your homework answered.')
def quizreminder(dic, num, covered_materials, date):
    emailall(dic,'Quiz ' + str(num) + ' will be given on ' + date,"This is a friendly reminder that quiz " + str(num) + ' on ' + covered_materials + " will be given on " + date + '. Please feel free to ask questions on Piazza, email <YOUR_NAME>, come to office hours or visit evening help sessions to prepare for the quiz.')
def examreminder(dic, exam_name, covered_materials, date, start_time, finish_time, location):
    emailall(dic, exam_name + ' will be given on ' + date,"This is a friendly reminder that " + exam_name + ' on ' + covered_materials + " will be given from " + start_time + " to " + finish_time + " on "  + date + '. The location of the exam is ' + location + '. Please feel free to ask questions on Piazza, email <YOUR_NAME>, come to office hours or visit evening help sessions to prepare for the exam.')
def hwemailgrader(name, dic, hw):
    sendemail(name, dic, 'Homework', 'Some new homework has been received by the Calculus-chan system. Please grade it.', hw)
def hwreply(email):
    anonsendemail(email, "Your HW has been received", "Your HW has been received and sent to the grader. If you have any questions about the HW set please email <YOUR_NAME>.")
if __name__ == '__main__':
    emailall(studentdic,"<COURSE>: test", "This is a test email.")
