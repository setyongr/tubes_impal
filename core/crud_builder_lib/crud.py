from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path, reverse


class SimpleCrud:
    def __init__(self, title, table, form, detail, instance, change_form = None):
        self.title = title
        self.table = table
        self.form = form
        self.detail = detail
        self.instance = instance
        if change_form is None:
            change_form = self.form

        self.change_form = change_form

    def route_index(self, name_prefix):
        def function(request):
            context = {
                'title': self.title,
                'table': self.table,
                'add_url': reverse(name_prefix + '_add')
            }
            return render(request, 'table.html', context)

        return function

    def route_add(self, name_prefix):
        def function(request):
            form = self.form(request.POST or None)

            if form.is_valid():
                form.save()
                return redirect(name_prefix+'_index')

            context = {
                'title': "Tambah " + self.title,
                'form': form
            }

            return render(request, 'form.html', context=context)

        return function

    def route_detail(self):
        def function(request, id):

            instance = self.detail.get_object(id)

            context = {
                'title': "Detail " + self.title,
                'sections': self.detail.get_schema(instance)
            }

            return render(request, 'detail.html', context=context)

        return function

    def route_edit(self, name_prefix):
        def function(request, id):
            instance = get_object_or_404(self.instance, id=id)
            form = self.change_form(request.POST or None, instance=instance)

            if form.is_valid():
                form.save()
                return redirect(name_prefix+'_index')

            context = {
                'title': "Edit " + self.title,
                'form': form
            }

            return render(request, 'form.html', context=context)

        return function

    def route_delete(self, name_prefix):
        def function(request, id):
            instance = get_object_or_404(self.instance, id=id)
            instance.delete()
            return redirect(name_prefix+'_index')

        return function

    def get_url(self, name_prefix, base_path=''):
        return [
            path(base_path + '/', self.route_index(name_prefix), name=name_prefix + '_index'),
            path(base_path + '/add', self.route_add(name_prefix), name=name_prefix + '_add'),
            path(base_path + '/detail/<id>', self.route_detail(), name=name_prefix + '_detail'),
            path(base_path + '/edit/<id>', self.route_edit(name_prefix), name=name_prefix + '_edit'),
            path(base_path + '/delete/<id>', self.route_delete(name_prefix), name=name_prefix + '_delete')
        ]
