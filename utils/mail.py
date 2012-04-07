from django.utils.encoding import force_unicode
from django.core.mail import EmailMultiAlternatives, EmailMessage
from mailer.models import make_message
from mailer import PRIORITY_MAPPING
from os.path import basename

def send_mail(attachments=[]):

    attach_t = []
    for attachment in attachments:
        filename = basename(attachment)
        content = open(attachment, 'rb').read()
        attach_t.append((filename, content, None)) #Guess mimetype
    
    email = EmailMessage('Hello',
                 'BodyGoesHere',
                 'sac@tootalk.com',
                 ['jolaechea@bitzeppelin.com', 'pirata@gmail.com'],
                 attachments=attach_t
                 )
    email.send()

def send_html_mail_with_attachments(subject, message, message_html, from_email, recipient_list,
                   priority="medium", fail_silently=False, auth_user=None,
                   auth_password=None, attachments=[]):
    """
    Function to queue HTML e-mails
    path = list of paths to attachments
    ####
    attachments.append((filename, content, mimetype))
    """

    
    priority = PRIORITY_MAPPING[priority]
    
    # need to do this in case subject used lazy version of ugettext
    subject = force_unicode(subject)
    message = force_unicode(message)

    attach_t = []
    for attachment in attachments:
        filename = basename(attachment)
        content = open(attachment, 'rb').read()
        attach_t.append((filename, content, None)) #Guess mimetype
    
    msg = make_message(subject=subject,
                       body=message,
                       from_email=from_email,
                       to=recipient_list,
                       priority=priority,
                       attachments=attach_t)

    email = msg.email
    email = EmailMultiAlternatives(email.subject, email.body, email.from_email, email.to, attachments=email.attachments)
    email.attach_alternative(message_html, "text/html")
    msg.email = email
    msg.save()
    return 1
