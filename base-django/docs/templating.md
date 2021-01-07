# Templating

To use your custom templates in base configuration add `BASE_TEMPLATES_FOLDER` to your `settings.py`

This folder must have a file for each view class:

- BaseCreateView: create.html
- BaseDeleteView: delete.html
- BaseDetailView: detail.html
- BaseGridView: grid.html
- BaseListView: list.html
- BasePaginationGridView: pagination_grid.html
- BasePaginationListView: pagination_list.html
- BaseUpdateView: update.html

You can copy [bootstrap template folder](../templates/base/bootstrap) to use as a base
 

