from django.shortcuts import get_object_or_404

from core.models import Pegawai


class ViewSection:
    def __init__(self, title, details):
        self.title = title
        self.details = details

    class d:
        def __init__(self, label, value, type=None):
            """
            :param title:
            :param value:
            :param type: (image, None)
            """
            self.label = label
            self.value = value
            self.type = type


class Detail:
    def get_object(self, id):
        raise ValueError("get_object should be implemented")

    def get_schema(self, instance):
        return ValueError("get_schema should be implemented")

    def get_template(self):
        return None


class SimpleModelDetail(Detail):
    def __init__(self, instance, schema):
        self.instance = instance
        self.schema = schema

    def get_object(self, id):
        return get_object_or_404(self.instance, id=id)

    def get_schema(self, instance):
        section = []
        vs = ViewSection("Detail", [])
        for s in self.schema:
            key, title = s.split('|')
            vs.details.append(ViewSection.d(title, getattr(instance, key)))

        section.append(vs)
        return section
