import textwrap

from django import forms
from django.core.mail import EmailMessage
from django.utils.html import format_html
from mailchimp3.helpers import get_subscriber_hash
from wagtail.admin.forms import WagtailAdminModelForm

from .models import ContactDetails, MailchimpSettings


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=255)
    email = forms.EmailField(label="Your email address")
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
            reply_to=['"{name}" <{email}>'.format(**data)],
        )
        return message.send()


class MailchimpSettingsForm(WagtailAdminModelForm):
    api_key = forms.CharField(
        help_text=format_html(
            """
            See <a href="{}">About API Keys</a> in the Mailchimp documentation
            form more information.
            """,
            "https://mailchimp.com/help/about-api-keys/"))

    newsletter_list = forms.ChoiceField(
        choices=[], required=False, help_text=(
            "Subscribing to the newsletter will add people to this list."))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        newsletter_list = self.fields['newsletter_list']
        if self.instance.api_key:
            client = self.instance.get_client()
            lists = client.lists.all(
                get_all=True, fields="lists.name,lists.id")
            newsletter_list.choices = [('', '---------')] + [
                (l['id'], l['name']) for l in lists['lists']]
        else:
            newsletter_list.help_text = "Enter your Mailchimp API key first"
            newsletter_list.required = False
            newsletter_list.choices = []
            newsletter_list.disabled = True


class NewsletterSubscribeForm(forms.Form):
    prefix = 'newsletter'

    email = forms.EmailField(label="Email address", widget=forms.TextInput())

    def save(self, request):
        email = self.cleaned_data['email']

        mailchimp_settings = MailchimpSettings.for_site(request.site)
        client = mailchimp_settings.get_client()
        list_id = mailchimp_settings.newsletter_list
        hash = get_subscriber_hash(email)

        client.lists.members.create_or_update(list_id, hash, {
            'email_address': email,
            'status': 'subscribed',
            'status_if_new': 'subscribed',
        })
