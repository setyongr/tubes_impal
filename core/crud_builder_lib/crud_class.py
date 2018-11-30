from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, path
from django.utils.decorators import available_attrs


def login_required(function=None):
    @wraps(function, assigned=available_attrs(function))
    def _wrapped_view(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(self, request, *args, **kwargs)
        return redirect(reverse("login"))
    return _wrapped_view


class CrudBuilder:
    name_prefix = None
    title = None
    table = None
    form = None
    detail = None
    instance = None
    change_form = None

    def __init__(self):
        if self.change_form is None:
            self.change_form = self.form

    @login_required
    def index(self, request):
        context = {
            'title': self.title,
            'table': self.table,
            'add_url': reverse(self.name_prefix + '_add')
        }
        return render(request, 'table.html', context)

    @login_required
    def route_add(self, request):
        form = self.form(request.POST or None)

        form.handle_user(request.user)
        if form.is_valid():
            form.save()
            return redirect(self.name_prefix + '_index')

        context = {
            'title': "Tambah " + self.title,
            'form': form
        }

        return render(request, 'form.html', context=context)

    @login_required
    def route_detail(self, request, id):
        instance = self.detail.get_object(id)

        context = {
            'title': "Detail " + self.title,
            'sections': self.detail.get_schema(instance)
        }

        return render(request, 'detail.html', context=context)

    @login_required
    def route_edit(self, request, id):
        instance = get_object_or_404(self.instance, id=id)
        form = self.change_form(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()
            return redirect(self.name_prefix+'_index')

        context = {
            'title': "Edit " + self.title,
            'form': form
        }

        return render(request, 'form.html', context=context)


    @login_required
    def route_delete(self, request, id):
        instance = get_object_or_404(self.instance, id=id)
        instance.delete()
        return redirect(self.name_prefix+'_index')


    def get_url(self, base_path):
        # Adding default url
        url = [
            path(base_path + '/', self.index, name=self.name_prefix + '_index'),
            path(base_path + '/add', self.route_add, name=self.name_prefix + '_add'),
            path(base_path + '/detail/<id>', self.route_detail, name=self.name_prefix + '_detail'),
            path(base_path + '/edit/<id>', self.route_edit, name=self.name_prefix + '_edit'),
            path(base_path + '/delete/<id>', self.route_delete, name=self.name_prefix + '_delete')
        ]

        return url