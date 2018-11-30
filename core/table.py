from core.table_lib.column import CharCol
from core.table_lib.table import Table


class PegawaiTable(Table):
    nama = CharCol(label="Nama")
    alamat = CharCol(label="Alamat")
    jabatan = CharCol(label="Jabatan")

    class Meta:
        action = True
        view_action = "pegawai_detail"
        edit_action = "pegawai_edit"
        delete_action = "pegawai_delete"

class BarangTable(Table):
    nama = CharCol(label="Nama")
    stok = CharCol(label='Stok')

    class Meta:
        action = True
        view_action = "barang_detail"
        edit_action = "barang_edit"
        delete_action = "barang_delete"

class SupplierTable(Table):
    nama = CharCol(label="Nama")
    alamat = CharCol(label="Alamat")
    telp = CharCol(label='Telp')

    class Meta:
        action = True
        view_action = "supplier_detail"
        edit_action = "supplier_edit"
        delete_action = "supplier_delete"

class SparepartTable(Table):
    nama = CharCol(label="Nama")
    stok = CharCol(label="Stok")

    class Meta:
        action = True
        view_action = "sparepart_detail"
        edit_action = "sparepart_edit"
        delete_action = "sparepart_delete"

class OrderSparepartTable(Table):
    nama = CharCol(label="Nama")
    jumlah = CharCol(label="Jumlah")
    status = CharCol(label="Status")
    supplier = CharCol(label="Supplier")

    class Meta:
        action = True
        view_action = "order_sparepart_detail"
        edit_action = "order_sparepart_edit"
        delete_action = "order_sparepart_delete"
