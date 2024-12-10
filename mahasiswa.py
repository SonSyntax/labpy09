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