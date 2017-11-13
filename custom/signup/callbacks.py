from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.signals import request_finished
from django.core.cache import cache
from django.db.models import Q,Min,Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage as storage
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes

# Datetime related imports
from datetime import datetime
from datetime import date
from datetime import time
from datetime import tzinfo


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
from signals import  user_send_email
from custom.utils.models import Logger
from custom.users.decorators import run_async
from custom.tasks.models import TaskLog
from custom.users.models import Profile

from signals import facebook_strategy_used
from signals import twitter_strategy_used
from signals import linkedin_strategy_used 
from signals import facebook_authenticated
from signals import googleplus_strategy_used 
from signals import user_account_activated
from signals import register_redirect 
from signals import user_send_email
from signals import user_resend_activation
from signals import user_pending_activation
from signals import user_account_activated 
from signals import new_user_created 
from signals import new_user_cleared 
from signals import new_user_resend_notification 
from signals import user_needs_recovery 
from signals import user_password_reset 
from signals import log_new_user 
from signals import facebook_strategy_new_user 
from signals import facebook_strategy_existing_user
from signals import facebook_strategy_used 
from signals import twitter_strategy_used 
from signals import linkedin_strategy_used 
from signals import facebook_authenticated 
from signals import googleplus_strategy_used 
from signals import googleplus_strategy_fails 
from signals import googleplus_strategy_succeeds 
from signals import instagram_strategy_used 
from signals import default_strategy_used 
from signals import default_strategy_succeeds 
from signals import default_strategy_fails 
from signals import facebook_strategy_fails 
from signals import facebook_strategy_succeeds 
from signals import new_mailchimp_subscriber 



@receiver(user_send_email,sender=User)
def user_send_email_handler(sender,contact,**kwargs):
    try:
       task = TaskLog.objects.get(user_id=contact.id,job='sending_user_email')
    except Exception, R:
       task = TaskLog.objects.create(user_id=contact.id,job='sending_user_email',is_complete=False)  
       process_user_email(contact)

@run_async
def process_user_email(contact):

    try:
        timeNow = datetime.now()

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = '<strong>Grinberg & Segal'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = profile.email
        SUBJECT = 'New message from a customer'
        try:
            path = "templates/new_message.html"

            f = codecs.open(path, 'r')

            m = f.read()
            mess = string.replace(m, '[name]',contact.name)
            mess = string.replace(mess, '[message]', contact.message)
            mess = string.replace(mess, '[phone]',contact.phone)
            mess = string.replace(mess,'[email]',contact.email)
        #    mess = string.replace(mess,'[link]',link)

        except Exception, R:
            log = Logger(log=str(R))
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


########################
# Request Finished     #
########################

@receiver(request_finished)
def notify_new_user(sender, **kwargs):
    print("Request finished!")

def split_uppercase(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string).split()

################################################
# Facebook Strategy is used - update profile  #
################################################

@receiver(facebook_strategy_used, sender=User)
def facebook_profile_handler(sender, instance, is_new, email, facebook_id, request,  **kwargs):
    try:
        task = TaskLog.objects.get(user_id=instance.id,job='facebook_profile_created',is_complete=False)
        task = TaskLog.objects.get(user_id=instance.id,
                                   job='facebook_profile_created')
        task.is_complete=True
        task.save()()
        
    except Exception as e:
        task = TaskLog.objects.create(user_id=instance.id,
                                      username=instance.username,
                                      job='facebook_profile_created',
                                      is_complete=False)
        task.save()
        facebook_profile(sender, instance, is_new, email, facebook_id, request)



def facebook_profile(sender, instance, is_new, email, facebook_id, request):
    
    profile = Profile.objects.get(id=instance.id)

    if not profile.is_facebook_signup_used:
        new_account_created(instance=instance)
        profile.is_facebook_signup_used=True
        profile.save()



@receiver(twitter_strategy_used, sender=User)
def twitter_profile_handler(sender, instance, is_new, email, profile_picture, **kwargs):
    try:
        task = TaskLog.objects.get(user_id=instance.id,
                                   job='twitter_profile_created')

        task.is_complete=True
        task.save()
    except Exception,R:
        task = TaskLog.objects.create(user_id=instance.id,
                                      username=instance.username,
                                      job='twitter_profile_created',
                                      is_complete=False)
        task.save()
        twitter_profile(sender, instance, is_new, email, profile_picture)


def twitter_profile(sender, instance, is_new, email, profile_picture, **kwargs):

    profile = Profile.objects.get(id=instance.id)

    if is_new:
        new_account_created(instance=instance)





###################################################
# Google Plus Strategy is used - update profile  #
###################################################

@receiver(googleplus_strategy_used, sender=User)
def googleplus_profile_handler(sender, instance, is_new, email, profile_picture, **kwargs):
    try:
        task = TaskLog.objects.get(user_id=instance.id,job='google_profile_created')
        task = TaskLog.objects.get(user_id=instance.id,
                                   job='google_profile_created')
        task.is_complete=True
        task.save()

    except Exception,R:
        task = TaskLog.objects.create(user_id=instance.id,
                                      username=instance.username,
                                      job='google_profile_created',
                                      is_complete=False)
        task.save()
        google_profile(sender, instance, is_new, email, profile_picture)


@run_async
def google_profile(sender, instance, is_new, email, profile_picture):

    log = Logger(log='IN GOOGLE PROFILE CREATION')
    log.save()

    profile = Profile.objects.get(id=instance.id)

    new_account_created(instance=instance)


 

@receiver(user_account_activated, sender=User)
def greet_user(sender,instance,**kwargs):
    try:
        send_welcome(instance=instance)
    except Exception, R:
        lg = Logger(log='some shit'+str(R))




######################
# Create New Profile #
######################

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        task = TaskLog.objects.get(user_id=instance.id,
                                   job='new_profile_notification')
        task.is_complete=True
    except Exception,R:
        task = TaskLog.objects.create(user_id=instance.id,
                                      username=instance.username,
                                      job='new_profile_notification',
                                      is_complete=False)
        task.save()
        create_user_profile(instance)  

                 
@run_async
def create_user_profile(instance): 


    user = instance
    mess = 'Activate Accout.'

    try:
        profile = Profile.objects.get(id=instance.id)
        profile.is_active=True
        profile.is_new=False
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.email = instance.email
        profile.username = instance.username.lower()
        profile.save()
        activate = False
       
    except ObjectDoesNotExist:
        try:
            log = Logger(log='IN CREATING PROFILE - PROFILE DOES NOT EXIST')
            log.save()
            instance.username=str(instance.id)
            instance.save() 
            instance.username=str(instance.id)
            password = instance.password
            instance.set_password(password)
            instance.save()

            profile = Profile.objects.create(id=int(instance.id),
                                             first_name=instance.first_name,
                                             last_name=instance.last_name,
                                             email=instance.email,
                                             user=instance,
                                             is_new=1,
                                             profile_image_path=settings.PROFILE_IMAGE_PATH,
                                             username=instance.username.lower())
 

            profile.save()
            log = Logger(log='WE RE TRYING TO SEND BEFORE')
            log.save()

            new_account_created(instance=instance)
            log = Logger(log='WE RE TRYING TO SEND')
            log.save()
        except Exception as e:
            log = Logger(log='WE FAILED TO CREATE NEW PROFILE %s'%str(e))
            log.save()

@run_async
def send_activation_link(contact):
    log = Logging(log='WILL SEND ACTIVATION')
    log.save()

    mess = 'Please activate your account.'    
    try:
        timeNow = datetime.now()

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = '<strong>Grinberg & Segal'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = profile.email
        SUBJECT = 'New message from a customer'
        try:
            path = "templates/new_message.html"

            f = codecs.open(path, 'r')

            m = f.read()
            mess = string.replace(m, '[name]',contact.name)
            mess = string.replace(mess, '[message]', contact.message)
            mess = string.replace(mess, '[phone]',contact.phone)
            mess = string.replace(mess,'[email]',contact.email)
        #    mess = string.replace(mess,'[link]',link)

        except Exception as R:
            log = Logger(log='WE FAILED SENDING ACTIVATION %s'%str(R))
            log.save()

        message = mess

        HTML_BODY  = MIMEText(message, 'html','utf-8')
        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string()
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()

    except Exception as R:
        log = Logger(log='WE FAILED SENDING ACTIVATION %s'%str(R))
        log.save()





########################
# Send Welcome Letter  #
########################
@run_async
def send_welcome(instance):

    mess = 'Welcome to Art Revolution.'

    try:
    #    global_link = settings.BASE_URL+'/signin'
        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = '<strong>Art Revolution'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = instance.email
        global_link = settings.BASE_URL+'/signin'

        try:
           email = instance.email
        except Exception as R:
           email = ''

        f = codecs.open("templates/welcome_inline.html", 'r')
        m = f.read()
        mess = m
        mess = string.replace(m, '[global_link]',global_link)
        mess = string.replace(mess,'email_address@email.com',email.encode('utf-8')) #email)
       # mess = string.replace(mess,'[email]',email)
       # mess = string.replace(mess,'[global_link]',global_link)
        #mess = string.replace(mess,'[email]',instance.email)
     #   mess = string.replacce(mess, '[global_link]',global_link)
       # mess = string.replace(mess,'[link]','')

       # message = mess.escape(string_to_escape, quote=True)
        SUBJECT = 'Welcome to Grinberg and Segal!'

        message = mess


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
                Your mail reader does not support the report format.
                Please visit us <a href="http://www.mysite.com">online</a>!"""

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
        log = Logger(log='---ERROR---'+str(R))
        log.save()




# Record the MIME types of both parts - text/plain and text/html.



##########################
## Recover User Profile ##
##########################
@receiver(user_needs_recovery, sender=User)
def recover_profile(sender, instance, request, email,**kwargs):
    user = User.objects.get(email=email)
    mess = 'Welcome to Art Revolution.'

    try:
        member = Profile.objects.get(id=int(user.id))
    except Exception,R:
        member = Profile.objects.get(id=int(instance.id))


    try:
        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = 'Art Revolution <info@artrevolution.com>'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = email
    #contstruct the message
        # BODY='<html><head><style>.color{color:#FFAA44;}</style></head><body><div class="color"><strong>USERNAME</strong> %s'%user.username
        # BODY+='</strong></div><br/><strong>EMAIL</strong> %s'%user.email
        # BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        # BODY+='</strong><br/><strong>PLEASE FOLLOW THE LINK TO RECOVER: </strong> '
        # BODY+='<a href="%s">reset your password</a>.'%link
        # BODY+='</strong></body></html>'
        f = codecs.open("templates/recover_password.html", 'r')
        m = f.read()
        mess = m
        mess = string.replace(mess, '[reset_link]', link)
        mess = string.replace(mess, '[email]', user.email)
        mess = string.replace(mess, '[first_name]', user.first_name)

        SUBJECT = 'Account recovery notification for %s'%user.username
        message = mess

        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
                Your mail reader does not support the report format.
                Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(message, 'html','utf-8')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.


        MESSAGE.attach(HTML_BODY)
        msg = MESSAGE.as_string()
        server = smtplib.SMTP(SERVER+':'+PORT)
        server.ehlo()
        server.starttls()
        server.login(USER,PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()
  #      log_new_user.send(sender='create_profile', message='created new user', level=1)
#        raise ForceResponse(HttpResponseRedirect(reverse('success',kwargs={'code': 'success'})))

    except SMTPRecipientsRefused:
        pass

    except ObjectDoesNotExist:
        pass

@receiver(user_resend_activation, sender=User)
def resend_activation_handler(sender, instance, **kwargs):
    try:
        task = TaskLog.objects.get(user_id=instance.id,job='activation')   
        task.is_complete=True
        task.delete()
        #task.delete()
    except Exception,R:
        task = TaskLog.objects.create(user_id=instance.id,username=instance.username,job='activation',is_complete=False)
        task.save()
        send_activation_link(instance,ignore=True)

@receiver(facebook_strategy_fails, sender=User)
def facebook_strategy_fails_handler(sender, instance, request, **kwargs):
    pass


def new_account_created(instance):

    try:    
        profile = ProfileMetaProp.objects.get(pk=1)
        new_account_notify(instance, profile.to_email)
        #new_account_notify(instance, profile.to_email_secondary)
        #new_account_notify(instance, profile.to_email_third) 
        send_activation_link(instance, ignore=True)
    except ObjectDoesNotExist:
        pass


def new_account_notify(instance, email):

    try:


        log = Logger(log='WILL TRY TO NOTIFY')
        log.save()
        max_id= User.objects.all().aggregate(id=Max('id'))
        user = User.objects.get(id=max_id['id'])


        users = User.objects.all()#filter(is_active=True).order_by("-date_joined")[:100]

        usrs = []

        for usr in users:
            if usr.date_joined.day==user.date_joined.day:
               if usr.date_joined.month==user.date_joined.month:
                  if usr.date_joined.year==user.date_joined.year:
                            usrs.append(usr)
        today = len(usrs)

        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = 'Grinberg and Segal <info@divorcesus.com>'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = email

        if instance.first_name:
           first_name = instance.first_name
        else:
           first_name = user.profile.first_name

        if instance.last_name:
           last_name = instance.last_name
        else:
           last_name = instance.profile.last_name

        if user.profile.is_facebook_signup_used:
           strategy='Facebook'
           try:
                fb  = FacebookProfile.objects.get(id=instance.id)
                facebook_id = fb.facebook_id
           except ObjectDoesNotExist:
                facebook_id = None

        elif user.profile.is_google_signup_used:
           strategy='Google'
           try:
                gp  = GooglePlusProfile.objects.get(id=instance.id)
                google_id = gp.google_id
           except ObjectDoesNotExist:
                google_id = None

        else:
           strategy = 'Regular Signup'

        time = str(instance.date_joined.time())
        time = time[0:-7]
        year = instance.date_joined.year
        month = instance.date_joined.month
        day = instance.date_joined.day
    #contstruct the message
        BODY='<html><body><strong>A NEW USER HAS REGISTERED'
        BODY+='</stroing><br/><strong>SERVER</strong> %s'%settings.BASE_URL
        BODY+='</stroing><br/><strong>DATE JOINED </strong> %s-%s-%s %s'%(year,month,day,time)
        BODY+='</stroing><br/><strong>USERNAME</strong> %s'%instance.username
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%instance.email
        BODY+='</strong><br/><strong>FIRST NAME</strong> %s'%first_name
        BODY+='</strong><br/><strong>LAST NAME</strong> %s'%last_name
        BODY+='</strong><br/><strong>SIGNED UP USING</strong> %s'%strategy
        if strategy=='Facebook':
           if facebook_id:
               BODY+='</strong><br/><strong>FACEBOOK ID </strong> %s'%str(facebook_id)
        if strategy=='Google':
           if google_id:
               BODY+='</strong><br/><strong>GOOGLE ID </strong> %s'%str(google_id)

        BODY+='</strong><br/><strong>USER ID </strong> %d'%instance.id
        BODY+='</strong><br/><strong>USER PPROFILE </strong> %s'%settings.BASE_URL+'/'+instance.username
        BODY+='</strong><br/><strong>TOTAL USERS </strong> %s'%str(len(User.objects.all()))
        BODY+='</strong><br/><strong>OF THEM TODAY </strong> %s'%str(today)
        BODY+='</body></html>'
        SUBJECT = 'A new user signed up'
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
                Your mail reader does not support the report format.
                Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
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
        log = Logger(log='SOME SHIT PREVENTED US FROM SENDING '+str(R))
        log.save()


@receiver(user_password_reset, sender=User)
def reset_password(sender, instance, request, email, password, **kwargs):
    user = User.objects.get(email=email)
    mess = 'Your password has been successfully reset.'

    try:
        profile = ProfileMetaProp.objects.get(pk=1)
        FROM = 'Art Revolution <info@artrevolution.com>'
        USER = profile.user_name
        PASSWORD = profile.password
        PORT = profile.smtp_port
        SERVER = profile.smtp_server
        TO = email
    #contstruct the message
        BODY='<html><body><strong>USERNAME</strong> %s'%user.username
        BODY+='</strong><br/><strong>EMAIL</strong> %s'%user.email
        BODY+='</strong><br/><strong>MESSAGE</strong> %s'%mess
        BODY+='</strong><br/><strong>YOUR PASSWORD HAS BEEN UPDATED. </strong>'
        BODY+='</body></html>'
        SUBJECT = 'Password reset notification for %s'%user.username
        message = 'Subject: %s\n\n%s' % (SUBJECT, BODY)


        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
                Your mail reader does not support the report format.
                Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY  = MIMEText(BODY.encode('utf-8'), 'html','utf-8')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
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

@receiver(new_user_resend_notification,sender=User)
def new_user_resend_notification_handler(sender,instance,**kwargs):
    new_account_created(instance)


@receiver(facebook_authenticated, sender=User)
def read_facebook_profile(sender,instance,**kwargs):
    log = Logger(log='ffffffff')
    log.save()


