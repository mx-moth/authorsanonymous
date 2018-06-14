from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from mailchimp3.mailchimpclient import MailChimpError
from requests.exceptions import RequestException

from .forms import ContactForm, NewsletterSubscribeForm
from .models import MailchimpSettings


def contact_form(request):
    return render(request, 'layouts/contact.html', {
        'form': ContactForm(),
        'show_contact_form': False,
    })


@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return JsonResponse(
            {'errors': form.errors.get_json_data()}, status=422)

    form.send(request)

    return JsonResponse({}, status=204)


@require_POST
def newsletter_submit(request):
    mailchimp_settings = MailchimpSettings.for_site(request.site)
    if not mailchimp_settings.newsletter_list:
        raise Http404

    form = NewsletterSubscribeForm(request.POST)

    if not form.is_valid():
        return JsonResponse(
            {'errors': form.errors.get_json_data()}, status=422)

    try:
        form.save(request)
    except RequestException:
        return JsonResponse(
            {'error': 'Error subscribing to list'}, status=500)
    except MailChimpError as error:
        response = error.args[0]
        return JsonResponse(
            {'errors': {'email': [{'message': response['detail']}]}},
            status=422)

    return JsonResponse({}, status=204)
