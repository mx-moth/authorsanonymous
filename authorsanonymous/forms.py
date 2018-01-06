import textwrap

from django import forms
from django.core.mail import EmailMessage

from .models import ContactDetails


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    prefix = 'contact'

    subject_template = "Message from {name}"
    body_template = textwrap.dedent(
        """
        "{name}" has sent you a message. You can email them at "{email}" by
        replying to this message. Their message is:

        ---

        {message}
        """
    )

    def send(self, request):
        contact_details = ContactDetails.for_site(request.site)
        data = self.cleaned_data

        message = EmailMessage(
            subject=self.subject_template.format(**data),
            body=self.body_template.format(**data),
            to=[contact_details.email],
            reply_to=['"{name}" <email>'.format(**data)],
        )
        return message.send()
