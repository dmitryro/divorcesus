from django.contrib.auth.models import User
from django.dispatch import receiver
# Datetime related imports
from datetime import datetime
from datetime import date
from datetime import time
from datetime import tzinfo


from django.core.exceptions import ObjectDoesNotExist
# Email imports
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# smtp imports
import smtplib
import urllib2
from smtplib import SMTPRecipientsRefused
import string
import codecs
from StringIO import StringIO
import urllib2
import random
import json
import os
import re
# Custom Imports
from custom.metaprop.models import ProfileMetaProp


from custom.users.decorators import run_async
from custom.tasks.models import TaskLog
from custom.users.models import Profile
from custom.utils.models import Logger

from signals import payment_send_confirmation_email

@receiver(payment_send_confirmation_email,sender=User)
def payment_send_confirmation_email_handler(sender,**kwargs):
     try:
        contact = kwargs['contact']
        payment = kwargs['payment']

        task = TaskLog.objects.get(user_id=contact.id,job='sending_payment_email')
     except Exception, R:
        task = TaskLog.objects.create(user_id=contact.id,job='sending_payment_email',is_complete=False)
        contact = kwargs['contact']
        log = Logger(log="WE ARE IN SIGNAL AND ARE TRYING TO SEND IT ")
        log.save()
        payment = kwargs['payment']
        process_payment_confirmation_email(payment)

def process_payment_confirmation_email(payment):

    try:
        log = Logger(log="WE ARE TRYING TO SEND IT ")
        log.save()

        timeNow = datetime.now()

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = '<strong>Grinberg & Segal'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = payment.email

        SUBJECT = 'Your payment has been processed'
        try:
            path = "templates/payment_message.html"

            f = codecs.open(path, 'r')

            m = f.read()
            mess = m
            mess = string.replace(m, '[fullname]',payment.fullname)
            mess = string.replace(mess, '[message]', "Your payment has been processed")
            mess = string.replace(mess, '[address1]',payment.address1)
            mess = string.replace(mess, '[address2]',payment.address2)
            mess = string.replace(mess, '[city]',payment.city)
            mess = string.replace(mess, '[state]',payment.state)
            mess = string.replace(mess, '[zip]',payment.zipcode)
            mess = string.replace(mess, '[cardtype]',payment.cardtype)
            mess = string.replace(mess, '[cardnumber]',payment.cardnumber)
            mess = string.replace(mess, '[month]',payment.month)
            mess = string.replace(mess, '[year]',payment.year)
            mess = string.replace(mess, '[phone]',payment.phone)
            mess = string.replace(mess, '[email]',payment.email)
        #    mess = string.replace(mess,'[link]',link)

        except Exception, R:
            log = Logger(log="WE FAILED LOUDLY "+str(R))
            log.save()
        message = mess

        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
                Your mail reader does not support the report format.
                Please visit us <a href="http://www.mysite.com">online</a>!"""

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
        HTML_BODY  = MIMEText(message, 'html','utf-8')
        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string()
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()

    except SMTPRecipientsRefused:
        pass
    except ObjectDoesNotExist:
        pass
    except Exception, R:
        log = Logger(log=str(R))
        log.save()




