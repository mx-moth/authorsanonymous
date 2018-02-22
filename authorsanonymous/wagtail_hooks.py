from django.utils.html import format_html
from wagtail.wagtailcore import hooks

hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        '<script defer src="{}"></script>',
        'https://use.fontawesome.com/releases/v5.0.6/js/all.js')
