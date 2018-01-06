from django.core.mail import send_mail

from .forms import ContactForm


def contact_form(request):
    did_send = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send(request)
            did_send = True
    else:
        form = ContactForm()

    return render(request, 'layouts/contact.html', {
        'form': form,
        'did_send': did_send,
    })
