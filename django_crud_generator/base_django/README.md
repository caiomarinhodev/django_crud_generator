# base-django

Base Django is a base application to build fastest django application.

Base provides a boilerplate to create Class Based Views and a set of useful models to use in a ready to go app.

We recommend use base with [Django CRUD generator](https://git.contraslash.com/ma0/django-crud-generator) 
(also mirrored on [github](https://github.com/contraslash/django-crud-generator)), to create CRUD segments in
minutes.
  
Try:

```bash
pip install django-crud-generator
cd your/django/project/folder
git submodule add https://github.com/contraslash/base-django base
django-crud-generator.py --django_application_folder your/application/folder --model_name YourModelName 
```

## Templating

We assume you have a `base.html` file with this a main block content, example:

```html
<html>
    <head>
    
    </head>
    <body>
        {% block content %}
        
        {% endblock %}
    </body>
</html>
```

We support these CSS Frameworks:

- [Bootstrap](templates/base/bootstrap)
- [Materialize](templates/base/bootstrap)


But if you prefer use your own styles, specify the template folder to use in your `settings.py` file

```python
BASE_TEMPLATES_FOLDER = "my_template_folder"
```

This folder must be discoverable for your `TEMPLATE_ENGINE`

To check full documentation see [Templating](docs/templating.md)

Base uses [messages](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/) Framework, with bootstrap you can use like:

```html
<html>
    ...
    <body>
        ...
        {% for message in messages %}
            <div class="alert alert-{{ message.level_tag }} alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                {{ message }}
            </div>
        {% endfor %}
        {% block content %}
        
        {% endblock %}
    </body>
</html>
```

We also provide an [authentication package](https://git.contraslash.com/ma0/authentication-django), (also mirrored in
[github](https://github.com/ma0c/authentication-django)) to speed up authentication

## Permissions

To use the permissions and groups configuration, you need to specify
two dicts one with permissions name and other with groups schema

```python
PERMISSIONS = {
    'manage_orders': {
        'app_label': 'application_name',
        'model': 'model_name',
        'codename': 'code_name_for_permissions',
    }
}

GROUPS = {
    'group_name': {
        "name": _("Verbose name"),
        'permissions': [
            "permission_attached_to",
            "this_group"

        ]
    },
}
```

Then use `base.setup`.


## Context processors

To use any context processor, you need to add the function signature name to
your `TEMPLATES[0]["OPTIONS"]["CONTEXT_PROCESSORS"]`

- site_name:
    site_name relies on `django.contrib.sites`, so add it to your `INSTALLED_APPS` on your `settings.py`
    Also read the [official documentation](https://docs.djangoproject.com/en/2.2/ref/contrib/sites/)
     
     
Check the full documentation for [context_processors](docs/context_processors.md)


