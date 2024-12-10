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