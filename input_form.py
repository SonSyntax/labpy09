import time
from data.mahasiswa import Mahasiswa

def tambah_data(data):
        nim = input("masukan nim anda: ")
        nama = input("masukan nama anda: ")
        nilai = float(input("masukan nilai tugas: "))
        
        data[nim] = {
        'nama' : nama,
        'nilai' : nilai
       }

def cari_data(data):
        nim = input("masukan nim yang ingin dicari: ")
        if nim in data:
            info = data[nim]
            print("\nData ditemukan:")
            print(f'''
              nim           : {nim}
              nama          : {info['nama']}
              nilai         : {info['nilai']}
              ''')
        else:
            print("nim tidak ditemukan ")
        
def hapus_data(data):
        nim = input("temukan data anda dengan memasukan nim jika ingin di hapus: ")
        if nim in data:
            del data[nim]
            print("Data berhasil dihapus")
        else:
            print("Nim tidak ditemukan")
        
def ubah_data(data):
        nim = input("masukan nim yang ingin di ubah: ")
        if nim in data:
            print("Data ditemukan. masukkan data baru")
            nama = input("masukan nama anda: ")
            nilai = float(input("masukan nilai tugas: "))
           
            
            data[nim] = {
                'nama' : nama,
                'nilai' : nilai
                
            }
            print("Data Berhasil diubah")
        else:
            print("Nim tidak ditemukan")
            
