from core.crud_builder_lib.crud_class import CrudBuilder
from core.crud_builder_lib.detail import SimpleModelDetail
from core.forms import PegawaiForm, PegawaiChangeForm, BarangForm, SupplierForm, SparepartForm, OrderSparepartForm
from core.models import Pegawai, Barang, Supplier, Sparepart, OrderSparepart
from core.table import PegawaiTable, BarangTable, SupplierTable, SparepartTable, OrderSparepartTable


class PegawaiCrud(CrudBuilder):
    name_prefix = "pegawai"
    title = "Pegawai"
    table = PegawaiTable(queryset=Pegawai.objects)
    form = PegawaiForm
    change_form = PegawaiChangeForm
    detail = SimpleModelDetail(Pegawai, ['nama|Nama', 'alamat|Alamat', 'jabatan|Jabatan'])
    instance = Pegawai


class BarangCrud(CrudBuilder):
    name_prefix = "barang"
    title = "Barang"
    table = BarangTable(queryset=Barang.objects)
    form = BarangForm
    detail = SimpleModelDetail(Barang, ["nama|Nama", "stok|Stok"])
    instance = Barang


class SupplierCrud(CrudBuilder):
    name_prefix = "supplier"
    title = "Supplier"
    table = SupplierTable(queryset=Supplier.objects)
    form = SupplierForm
    detail = SimpleModelDetail(Supplier, ["nama|Nama", "alamat|Alamat", "telp|Telp"])
    instance = Supplier


class SparepartCrud(CrudBuilder):
    name_prefix = "sparepart"
    title = "Sparepart"
    table = SparepartTable(queryset=Sparepart.objects)
    form = SparepartForm
    detail = SimpleModelDetail(Sparepart, ["nama|Nama", "stok|Stok"])
    instance = Sparepart


class OrderSparepartCrud(CrudBuilder):
    name_prefix = "order_sparepart"
    title = "Order Sparepart"
    table = OrderSparepartTable(data=lambda: [
        {
            "id": s.id,
            "nama": s.nama,
            "jumlah": s.jumlah,
            "status": s.status,
            "supplier": s.supplier.nama
        } for s in OrderSparepart.objects.all()
    ])
    form = OrderSparepartForm
    detail = SimpleModelDetail(OrderSparepart, ["nama|Nama", "jumlah|Jumlah", "status|Status", "supplier|Supplier"])
    instance = OrderSparepart


pegawai = PegawaiCrud()
barang = BarangCrud()
supplier = SupplierCrud()
sparepart = SparepartCrud()
order_sparepart = OrderSparepartCrud()

crud_url = pegawai.get_url("pegawai") + barang.get_url("barang") + supplier.get_url("supplier") + sparepart.get_url(
    "sparepart") + order_sparepart.get_url("order_sparepart")
