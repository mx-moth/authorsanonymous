from .forms import ContactForm, NewsletterSubscribeForm
from .models import MailchimpSettings


def contact_form(request):
    return {
        'show_contact_form': True,
        'contact_form': ContactForm(),
    }


def newsletter_form(request):
    mailchimp_settings = MailchimpSettings.for_site(request.site)
    return {
        'show_newsletter_form': bool(mailchimp_settings.newsletter_list),
        'newsletter_form': NewsletterSubscribeForm(),
    }
