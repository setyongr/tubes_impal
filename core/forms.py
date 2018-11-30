from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from core.models import Pegawai, Barang, Supplier, Sparepart, OrderSparepart


class UserHandleMixin:
    def handle_user(self, user):
        pass

    def user_clean(self, user):
        pass


class PegawaiForm(UserCreationForm, UserHandleMixin):
    nama = forms.CharField()
    alamat = forms.CharField()
    jabatan = forms.ChoiceField(label="Jabatan", choices=Pegawai.JABATAN)

    class Meta:
        model = Pegawai
        fields = ("username", "nama", "alamat", "jabatan")


class PegawaiChangeForm(UserChangeForm, UserHandleMixin):
    nama = forms.CharField
    alamat = forms.CharField()
    jabatan = forms.ChoiceField(label="Jabatan", choices=Pegawai.JABATAN)

    class Meta:
        model = Pegawai
        fields = ("username", "nama", "alamat", "jabatan")


class BarangForm(forms.ModelForm, UserHandleMixin):
    class Meta:
        model = Barang
        fields = ("nama", "stok")


class SupplierForm(forms.ModelForm, UserHandleMixin):
    class Meta:
        model = Supplier
        fields = ("nama", "alamat", "telp")


class SparepartForm(forms.ModelForm, UserHandleMixin):
    class Meta:
        model = Sparepart
        fields = ("nama", "stok")


class OrderSparepartForm(forms.ModelForm, UserHandleMixin):
    status = forms.ChoiceField(label="Status", choices=OrderSparepart.STATUS)
    def handle_user(self, user):
        if user.jabatan != "Pimpinan":
            self.fields["status"].choices = [('Belum Disetujui', 'Belum Disetujui')]
            if self.instance.status:
                self.fields["status"].choices = [(self.instance.status, self.instance.status)]

                if user.jabatan == "Gudang" and self.instance.status == "Disetujui":
                    self.fields["status"].choices = [("Diproses", "Diproses"), (self.instance.status, self.instance.status)]

                if user.jabatan == "Gudang" and self.instance.status == "Diproses":
                    self.fields["status"].choices = [("Selesai", "Selesai"), (self.instance.status, self.instance.status)]


    class Meta:
        model = OrderSparepart
        fields = ("nama", "jumlah", "status", "supplier")
