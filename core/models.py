from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Pegawai(AbstractUser):
    nama = models.CharField(max_length=255, null=True, default=None)
    alamat = models.CharField(max_length=255, null=True, default=None)
    JABATAN = (
        ("Marketing", "Marketing"),
        ("Produksi", "Produksi"),
        ("Gudang", "Gudang"),
        ("Pimpinan", "Pimpinan")
    )
    jabatan = models.CharField(max_length=255, null=True, default=None, choices=JABATAN)


class Penjualan(models.Model):
    creator = models.ForeignKey('core.Pegawai', on_delete=models.CASCADE)


class PenjualanDetail(models.Model):
    master = models.ForeignKey('core.Penjualan', on_delete=models.CASCADE, related_name="details")
    barang = models.ForeignKey('core.Barang', on_delete=models.CASCADE)


class Barang(models.Model):
    nama = models.CharField(max_length=255)
    stok = models.IntegerField()


class Supplier(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    telp = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class OrderSparepart(models.Model):
    nama = models.CharField(max_length=255)
    jumlah = models.CharField(max_length=255)
    STATUS = (
        ("Disetujui", "Disetujui"),
        ("Tidak Disetujui", "Tidak Disetujui"),
        ("Belum Disetujui", "Belum Disetujui"),
        ("Diproses", "Diproses"),
        ("Selesai", "Selesai"),
    )
    status = models.CharField(max_length=255, choices=STATUS)
    supplier = models.ForeignKey('core.Supplier', on_delete=models.CASCADE, related_name='orders')


# Transaksi Sparepart ?

class Sparepart(models.Model):
    nama = models.CharField(max_length=255)
    stok = models.IntegerField()
