# Context Processors

To use any context processor, you need to add the function signature name to
your `TEMPLATES[0]["OPTIONS"]["CONTEXT_PROCESSORS"]`

- site_name:
    site_name relies on `django.contrib.sites`, so add it to your `INSTALLED_APPS` on your `settings.py`
    Also read the [official documentation](https://docs.djangoproject.com/en/2.2/ref/contrib/sites/)
     