import string

from django.db.models import ManyToOneRel, ManyToManyField, ManyToManyRel, OneToOneRel, OneToOneField, ForeignKey


def get_label_html(attr):
    LABEL_TAG = '<label>{}:</label> \n'
    return LABEL_TAG.format(str(attr).capitalize())


def get_form_html(attr):
    dic = {'attribute': attr}
    form = string.Template('{{ form.${attribute} }} \n').safe_substitute(**dic)
    return form


def get_readonly_form_html(attr):
    dic = {'attribute': attr}
    form = string.Template('\n{{ object.${attribute} }} \n').safe_substitute(**dic)
    return form


def make_group_form_html(attr):
    block = get_label_html(attr) + get_form_html(attr)
    dic = {'block': block}
    group = string.Template('<div class="form-group"> \n ${block} </div>').safe_substitute(**dic)
    return group


def make_group_readonly_form_html(attr):
    block = get_label_html(attr) + get_readonly_form_html(attr)
    dic = {'block': block}
    group = string.Template('<div class="form-group"> \n ${block} </div>').safe_substitute(**dic)
    return group


def make_column_form(attr, length_col=12):
    form_group_attr = make_group_form_html(attr)
    length_col = 'col-xs-' + str(length_col)
    dic = {'block': form_group_attr}
    column = string.Template('<div class="' + length_col + '"> \n ${block} \n </div> \n').safe_substitute(**dic)
    return column


def make_readonly_column_form(attr, length_col=4):
    form_group_attr = make_group_readonly_form_html(attr)
    length_col = 'col-xs-' + str(length_col)
    dic = {'block': form_group_attr}
    column = string.Template('<div class="' + length_col + '"> \n ${block} \n </div> \n').safe_substitute(**dic)
    return column


def get_block_readonly_form(model):
    attributes_model = [make_readonly_column_form(str(f.name)) for f in model._meta.get_fields() if
                        f.editable and str(f.name).lower() != 'id']
    block_form = "".join(map(str, attributes_model))
    return block_form


def get_block_form(model):
    attributes_model = [make_column_form(str(f.name)) for f in model._meta.get_fields() if
                        f.editable and str(f.name).lower() != 'id']
    block_form = "".join(map(str, attributes_model))
    return block_form


def get_attributes_model(model):
    return [f for f in model._meta.get_fields() if
            f.editable and type(f) not in [ManyToOneRel, ManyToManyField, ManyToManyRel]]


def get_attributes_related(model):
    return [get_related_name(str(f.related_model)) for f in model._meta.get_fields() if
            f.editable and type(f) == ForeignKey]


def get_attributes_display(model, format_type='({})'):
    attributes_model = ['"' + str(f.name) + '"' for f in get_attributes_model(model)]
    list_str = ', '.join(map(str, attributes_model))
    format_type = format_type.format(list_str)
    return format_type


def valid_name_field(item):
    return '+' not in str(item.name)


def get_inlines_from_model(model):
    return [get_related_name(str(item.related_model)) for item in
            model._meta.get_fields(include_hidden=True) if
            type(item) == ManyToOneRel and valid_name_field(item)]


def get_list_inlines(model):
    list_attributes_rel = get_inlines_from_model(model)
    list_inlines = ['{}Inline'.format(attribute) for attribute in list_attributes_rel]
    return list_inlines


def get_inline_classes(model):
    list_inlines = get_list_inlines(model)
    list_inlines = ', '.join(map(str, list_inlines))
    list_inlines = '[{}]'.format(list_inlines)
    return list_inlines


def get_related_name(word):
    return word[word.index('app.models.') + len('app.models.'):word.index("'>")]


def get_formsets(model):
    inlines = ["{inline}{model}FormSet".format(model=model.__name__, inline=inline) for inline in
               get_inlines_from_model(model)]
    inlines = ', '.join(map(str, inlines))
    inlines = '[{}]'.format(inlines)
    return inlines


def get_formsets_import(model):
    inlines = ["{inline}{model}FormSet".format(model=model.__name__, inline=inline) for inline in
               get_inlines_from_model(model)]
    inlines = ', '.join(map(str, inlines))
    if len(inlines) >= 1:
        return ', {}'.format(inlines)
    else:
        return ''
