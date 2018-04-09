from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from wagtail.core import hooks

hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        '<script defer src="{}"></script>',
        'https://use.fontawesome.com/releases/v5.0.6/js/all.js')


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/admin.css')
    )
