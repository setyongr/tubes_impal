import copy
import json

from .column import Column

"""
Simple Table
See sample.py for example
"""


class BaseTable(object):
    def __init__(self, data=None, queryset=None):
        self.data = data
        self.queryset = queryset
        # Make a copy so that modifying this will not touch the class definition.
        self.columns = copy.deepcopy(self.base_columns)

    @property
    def header(self):
        return [column.label for column in self.columns]

    @property
    def get_json_data(self):
        return json.dumps(self.data)

    @property
    def checkbox(self):
        return getattr(self.opts, 'checkbox', False)

    @property
    def action(self):
        return getattr(self.opts, 'action', False)

    @property
    def get_data(self):
        used_data = []
        if self.data:
            used_data = self.data()
        if self.queryset is not None:
            used_data = list(self.queryset.values())
        return used_data

    def parse_action_url(self, url):
        kwargs = {}

        pattern = url.split('|')
        if len(pattern) > 1:
            param = pattern[1]
            param = param.split(',')

            for p in param:
                key, v = p.split("=")
                kwargs[key] = v

        pattern = pattern[0]
        return {
            'url': pattern,
            'kwargs': json.dumps(kwargs)
        }

    @property
    def action_url(self):
        urls = {}

        view_action = getattr(self.opts, 'view_action', None)
        edit_action = getattr(self.opts, 'edit_action', None)
        delete_action = getattr(self.opts, 'delete_action', None)

        if view_action:
            urls["view"] = self.parse_action_url(view_action)

        if edit_action:
            urls["edit"] = self.parse_action_url(edit_action)

        if delete_action:
            urls["delete"] = self.parse_action_url(delete_action)

        return urls

    @property
    def additional_button(self):
        return getattr(self.opts, 'additional_button', None)


class TableMetaClass(type):

    def __new__(cls, name, bases, attrs):
        attrs['opts'] = attrs.get('Meta', None)
        columns = []
        for attr_name, attr in attrs.items():
            if isinstance(attr, Column):
                attr.key = attr_name
                columns.append(attr)

        # If this class is subclassing other tables, add their fields as
        # well. Note that we loop over the bases in reverse - this is
        # necessary to preserve the correct order of columns.
        parent_columns = []
        for base in bases[::-1]:
            if hasattr(base, "columns"):
                parent_columns = base.columns + parent_columns

        base_columns = parent_columns + columns

        attrs['base_columns'] = base_columns

        return super(TableMetaClass, cls).__new__(cls, name, bases, attrs)


Table = TableMetaClass(str('Table'), (BaseTable,), {})
