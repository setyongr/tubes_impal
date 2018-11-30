import json

from django.template.loader import render_to_string


class Column:
    key = ''

    def __init__(self, label):
        self.label = label

    @property
    def render(self):
        pass


class CharCol(Column):
    @property
    def render(self):
        return json.dumps({
            'data': self.key
        })


class ImageCol(Column):
    @property
    def render(self):
        return render_to_string('table/column/image_column', {
            'key': self.key
        })
