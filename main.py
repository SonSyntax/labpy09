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