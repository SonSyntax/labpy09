# labpy09

![baru3](https://github.com/user-attachments/assets/e30d09a8-c619-4645-818c-d0cc3eb509e0)


## __init__.py
```Python
#di package file init di isi opsional
````

## data.mahasiswa.py
```Python
class Mahasiswa:
    def __init__(self, nama, nim, nilai, data):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
        self.data = data
        
    def tambah_data(data):
        nim = input("masukan nim anda: ")
        nama = input("masukan nama anda: ")
        nilai = float(input("masukan nilai tugas: "))
        
        data[nim] = {
        'nama' : nama,
        'nilai' : nilai
       }

    def lihat_data(data):
        print("\nDaftar Nilai: ")
        print("="*61)
        print("| NO | NAMA                           | NIM       | NILAI |")
        print("="*61)
        
        for i, (nim, info) in enumerate (data.items(), start=1):
            print(f"| {i:<2} | {info['nama']:<30} | {nim:<9} | {info['nilai']:<5} |")
        
        print("="*61)
        
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
````

File ini berisi kelas-kelas yang mendefinisikan model data mahasiswa, serta operasi dasar yang bisa dilakukan pada data mahasiswa (tambah, ubah, hapus, cari, dan tampilkan data).

Kelas:
Mahasiswa:
Bertanggung jawab untuk menyimpan data mahasiswa seperti NIM, nama, jurusan, dan tahun masuk.
Memiliki metode __str__ untuk mempermudah pencetakan objek mahasiswa dalam format yang mudah dibaca.
DataMahasiswa:
Berfungsi untuk mengelola kumpulan data mahasiswa.
Memiliki beberapa metode untuk memanipulasi data mahasiswa, seperti menambah mahasiswa (tambah_mahasiswa), menghapus mahasiswa berdasarkan NIM (hapus_mahasiswa), memperbarui data mahasiswa (ubah_mahasiswa), mencari mahasiswa berdasarkan NIM (cari_mahasiswa), dan menampilkan seluruh mahasiswa (tampilkan_semua).

## view.input_form.py
```Python
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
            

````

File ini berisi form input untuk memasukkan data mahasiswa baru ke dalam sistem. Ketika dijalankan, file ini akan meminta input dari pengguna seperti NIM, nama, jurusan, dan tahun masuk mahasiswa.

Kelas:
InputForm:
Menyediakan metode tampilkan_form() yang meminta inputan dari pengguna dan mengembalikan data yang dimasukkan sebagai tuple.

## view.mahasiswa.py
```Python
from data.mahasiswa import Mahasiswa
from view.input_form import tambah_data
import time

    
def lihat_data(data):
        print("\nDaftar Nilai: ")
        print("="*61)
        print("| NO | NAMA                           | NIM       | NILAI |")
        print("="*61)
        
        for i, (nim, info) in enumerate (data.items(), start=1):
            print(f"| {i:<2} | {info['nama']:<30} | {nim:<9} | {info['nilai']:<5} |")
        
        print("="*61)
        
def keluar_program():
        print("program akan dihentikan")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Program berhasil dihentikan")
        exit()
````
File ini bertugas untuk menampilkan data mahasiswa, baik dalam bentuk list seluruh mahasiswa maupun detail dari seorang mahasiswa.

Kelas:
MahasiswaView:
Menyediakan dua metode utama:
tampilkan_list(): Menampilkan seluruh daftar mahasiswa yang ada di dalam mahasiswa_list.
tampilkan_detail(): Menampilkan detail dari seorang mahasiswa berdasarkan data yang diberikan. Jika mahasiswa tidak ditemukan, maka akan menampilkan pesan kesalahan.

## main.py
```Python
import time
from view.input_form import tambah_data, ubah_data, hapus_data, cari_data
from data.mahasiswa import Mahasiswa
from view.mahasiswa import lihat_data, keluar_program

def main():
    data = dict()
    
    while True:
        print("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar")
        pilihan = input("\nPilih menu: ").lower()
            
        if pilihan == "t":
            tambah_data(data)
        elif pilihan == "l":
            lihat_data(data)
        elif pilihan == "u":
            ubah_data(data)
        elif pilihan == "h":
            hapus_data(data)
        elif pilihan == "c":
            cari_data(data)
        elif pilihan == "k":
            keluar_program()
        else:
            print("pilihan tidak valid")
    
    
if __name__ == "__main__":
    main()
````

File ini merupakan program utama yang menjalankan menu interaktif untuk pengguna. Pengguna dapat memilih berbagai opsi untuk mengelola data mahasiswa, seperti menambah, mengubah, menghapus, mencari, dan menampilkan daftar mahasiswa.

Fungsi:
Menampilkan menu utama yang memungkinkan pengguna untuk memilih tindakan (menambah, menghapus, mengubah, mencari, menampilkan).
Menggunakan kelas-kelas di file mahasiswa.py, input_form.py, dan mahasiswa_view.py untuk menjalankan fungsi-fungsi tersebut.
