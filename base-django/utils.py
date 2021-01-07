from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    FloatField,
    EmailField,
    ForeignKey,
    FileField,
    DateTimeField,
    DateField,
    AutoField,
    BooleanField,
    ManyToManyField
)
from django.forms.widgets import (
    Textarea,
    NumberInput,
    EmailInput,
    Input,
    Select,
    TextInput,
    FileInput,
    DateTimeInput,
    DateInput,
    HiddenInput,
    CheckboxInput,
    CheckboxSelectMultiple,
)

import random
import string
import csv


def generate_random_string(n):
    """
    Generates a random string of length n
    :param n: Length of string
    :return: Random string
    """
    return ''.join(random.choices(string.ascii_lowercase, k=n))


def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    """
    CSV reader for UTF-8 documents
    :param unicode_csv_data: Data of CSV
    :param dialect: Dialect of CSV
    :param kwargs: Other args
    :return:
    """
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [str(cell, 'utf-8') for cell in row]


def utf_8_encoder(unicode_csv_data):
    """
    UTF-8 Encoder
    :param unicode_csv_data:
    :return: Generator of UTF-8 encoding
    """
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def field_to_widget(field):
    if type(field) is CharField:
        if field.choices:
            return Select(attrs={"class": "form-control"})
        return TextInput(attrs={"class": "form-control", "rows": 1})
    if type(field) is TextField:
        return Textarea(attrs={"class": "form-control", "rows": 1})
    if type(field) is AutoField:
        return HiddenInput(attrs={"class": "form-control", "rows": 1})
    if type(field) is IntegerField or type(field) is FloatField:
        return NumberInput(attrs={"class": "form-control"})
    if type(field) is EmailField:
        return EmailInput(attrs={"class": "form-control"})
    if type(field) is ForeignKey:
        return Select(attrs={"class": "form-control"})
    if type(field) is ManyToManyField:
        return CheckboxSelectMultiple(attrs={"class": ""})
    if type(field) is BooleanField:
        return CheckboxInput(attrs={"class": "form-control"})
    if type(field) is FileField:
        return FileInput(attrs={"class": "form-control"})
    if type(field) is DateField:
        return DateInput(attrs={
            "class": "form-control date",
            "type": "date"
        })
    if type(field) is DateTimeField:
        return DateTimeInput(attrs={"class": "form-control datetimepicker"})

    return Input(attrs={"class": "form-control"})


def generate_bootstrap_widgets_for_all_fields(model):
    return {x.name: field_to_widget(x) for x in model._meta.get_fields()}
