from django.contrib.contenttypes import models as contenttypes_models
from django.contrib.auth import models as auth_models

from . import conf


def get_or_create_permission_from_dict(action_meta_data):
    contenttype = contenttypes_models.ContentType.objects.get(
        app_label=action_meta_data['app_label'],
        model=action_meta_data['model']
    )
    permissions = auth_models.Permission.objects.filter(
        content_type=contenttype,
        codename=action_meta_data['codename']
    )

    if permissions.count() > 0:
        permission = permissions[0]
    else:
        print(conf.CREATING_PERMISSION_WITH_NAME.format(action_meta_data['codename']))
        permission = auth_models.Permission.objects.create(
            content_type=contenttype,
            codename=action_meta_data['codename'],
            name=action_meta_data['codename']
        )

    return permission


def transform_descriptive_dict_in_permission_dict(permission_dict):
    assert isinstance(permission_dict, dict)
    return_dict = dict()
    for permission_name, description_dict in permission_dict.items():
        assert description_dict.get("app_label", "")
        assert description_dict.get("model", "")
        assert description_dict.get("codename", "")

        return_dict[permission_name] = get_or_create_permission_from_dict(description_dict)

    return return_dict


def get_all_permissions_in_dict_form():
    return {x.codename: x for x in auth_models.Permission.objects.all()}


def configure_groups_and_permissions(groups_dict, permissions_dict):
    assert isinstance(permissions_dict, dict)
    transformed_permission_dict = transform_descriptive_dict_in_permission_dict(permissions_dict)
    # Now we merge all permissions with new permission_dict
    all_permissions_in_dict_form = {
        **get_all_permissions_in_dict_form(),
        **transformed_permission_dict
    }
    assert isinstance(groups_dict, dict)
    for group_id, group_description in groups_dict.items():
        assert group_description.get("name", "")
        assert group_description.get("permissions", "")
        group_name = group_description.get("name", "")
        groups = auth_models.Group.objects.filter(name=group_name)
        if groups.count() == 0:
            print(conf.CREATING_GROUP_WITH_NAME.format(group_name))
            group = auth_models.Group.objects.create(
                name=group_name
            )
        else:
            group = groups[0]
        for permission in group_description.get("permissions", ""):
            group.permissions.add(all_permissions_in_dict_form[permission])
