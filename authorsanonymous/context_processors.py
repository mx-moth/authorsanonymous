from .forms import ContactForm


def contact_form(request):
    return {
        'show_contact_form': True,
        'contact_form': ContactForm(),
    }
