import csv
import os
import datetime
import time

tanggal= datetime.datetime.now()

def tampilan():
    print(" WELCOME TO SMARTAPOTEK ".center(85))
    print("Kepuasan Anda adalah Tujuan Kami".center(90))
    print("="*85)
tampilan()

def balik_user():
    print("\n")
    input("Tekan ENTER untuk kembali ke Menu User")
    tampilan()
    user_menu2()

def balik_admin():
    print("\n")
    input("Tekan ENTER untuk kembali ke Menu Admin")
    tampilan()
    admin_menu2()

def menu_awal():
    os.system('cls')
    tampilan()
    print("Apakah kamu User atau Admin :".center(85))
    print("1. User")
    print("2. Admin")
    print("-"*50)
    print("Pilih siapa Anda :")
    pilihan = input("")
    if pilihan == "1":
       user_menu()
    elif pilihan == "2":
        admin_menu()
    else:
        print('input tidak valid!!!')
        menu_awal()

def user_menu():
    os.system("cls")
    print('-'*50)
    print("1. Register")
    print("2. Login")
    print('-'*50)
    print("Pilih menu yang ingin digunakan:".center(50))
    print('-'*50)
    user_choice= (input(""))
    if user_choice== "1":
        user_register()
    elif user_choice == "2":
        user_login()
    else:
        print('input tidak valid!!!')
        menu_awal()

def admin_menu():
    os.system("cls")
    print('-'*50)
    print("1. Register")
    print("2. Login")
    print('-'*50)
    print("Pilih menu yang ingin digunakan:".center(50))
    print('='*50)
    user_choice= (input(""))
    if user_choice== "1":
        admin_register()
    elif user_choice == "2":
        admin_login()
    else:
        print('input tidak valid!!!')
        menu_awal()


def user_register():
    os.system('cls')
    print('-'*50)
    print("Silahkan melakukan registrasi".center(50))
    print('-'*50)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    with open('datalogin.csv', mode='a',newline='') as file:
    
        writer = csv.writer(file,delimiter=",")
        
        writer.writerow([username,password])
     

    print("Registrasi berhasil!")
    input("Tekan enter untuk kembali ke menu")
    os.system("cls")
    user_menu()

def admin_register():
    os.system('cls')
    print('-'*50)
    print("Silahkan melakukan registrasi".center(50))
    print('-'*50)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    with open('admin.csv', mode='a',newline='') as file:
    
        writer = csv.writer(file,delimiter=",")
        
        writer.writerow([username,password])
     

    print("Registrasi berhasil!")
    input("Tekan enter untuk kembali ke menu")
    os.system("cls")
    admin_menu()

def user_login():
    os.system('cls')
    print('-'*50)
    print('Silahkan melakukan login'.center(50))
    print('-'*50)
    valid = True
    while(valid):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
      
        with open('datalogin.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    global user
                    user = username
                    os.system('cls')
                    print("Login berhasil!")
                    user_menu2()
                    os.system("cls")
                  
        print("username / password salah !!")
        print("Apakah Anda ingin login kembali [y/n]?")
        cek= input("")
        if cek == "n":
            valid = False
        elif cek == "y":
            valid = True
        else:
            print("input salah!")
            valid = False
        os.system("cls")
            

def admin_login():
    os.system('cls')
    print('-'*50)
    print('Silahkan melakukan login'.center(50))
    print('-'*50)
    valid = True
    while(valid):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
      
        with open('admin.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login berhasil!")
                    admin_menu2()
                    os.system("cls")
                  
        print("username / password salah !!")
        print("Apakah Anda ingin login kembali [y/n]?")
        cek= input("")
        if cek == "n":
            valid = False
        elif cek == "y":
            valid = True
        else:
            print("input salah!")
            valid = False
            os.system("cls")

def baca_data_obat():
    data_masalah_kesehatan = []

    with open('obat.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_masalah_kesehatan.append(row)

    return data_masalah_kesehatan

def tampilkan_daftar_masalah_kesehatan(data_masalah):
    masalah_kesehatan = set()
    for item in data_masalah:
        masalah_kesehatan.add(item['masalah_kesehatan'])

    print("  Daftar Masalah Kesehatan   ".center(78,"-"))
    for idx, masalah in enumerate(masalah_kesehatan, start=1):
        print(f"{idx}. {masalah}")

    
def beli_obat(data_masalah): 
    tampilkan_daftar_masalah_kesehatan(data_masalah)
    pilihan_masalah = int(input("Pilih nomor masalah kesehatan Anda: "))
    data = list(set(i["masalah_kesehatan"] for i in data_masalah))
    
    if 1 <= pilihan_masalah <= len(data):
        masalah_terpilih = data[pilihan_masalah - 1]

        obat_masalah = [item for item in data_masalah if item['masalah_kesehatan'] == masalah_terpilih]
        
        print(f"Anda memilih masalah kesehatan: {masalah_terpilih}")
        print("  Daftar Obat   ".center(78,"-"))
        for idx, obat in enumerate(obat_masalah, start=1):
            obat['kegunaan'] = obat['kegunaan'].replace(";", ",")
            print(f"{idx}. Nama: {obat['nama_obat']}")
            print(f"\t Harga\t : Rp. {obat['harga']}")
            print(f"\t Kegunaan: {obat['kegunaan']}")
 

        pilihan_obat = int(input("Pilih nomor obat yang ingin Anda beli: "))
        if 1 <= pilihan_obat <= len(obat_masalah):
            obat_terpilih = obat_masalah[pilihan_obat - 1]
            print(f"Anda telah memilih obat {obat_terpilih['nama_obat']} untuk {masalah_terpilih}.")
           
            jumlah = int(input("Masukkan jumlah obat yang ingin Anda beli: "))
            os.system('cls')
            if jumlah > 0:
                stok_obat = int(obat_terpilih['stok'])
                total_harga = int(obat_terpilih['harga']) * jumlah
                
                obat_terpilih['stok'] = str(int(obat_terpilih['stok']) - jumlah)
                if jumlah <= stok_obat:
                    obat_terpilih['stok'] = str(stok_obat - jumlah)
                    cetak_nota(user, tanggal, masalah_terpilih, obat_terpilih['nama_obat'], obat_terpilih['harga'], jumlah, total_harga)
                    data = []
                    with open('obat.csv', 'r') as csvfile:
                        csvreader = csv.DictReader(csvfile)
                        for row in csvreader:
                            data.append(row)
                    
                    for row in data:
                        if row['masalah_kesehatan'] == masalah_terpilih and row['nama_obat'] == obat_terpilih['nama_obat']:
                            row['stok'] = int(row['stok']) - jumlah
                            
                    with open('obat.csv', 'w', newline='') as csvfile:
                        fieldnames = ['masalah_kesehatan', 'nama_obat', 'harga', 'kegunaan', 'stok']
                        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        csvwriter.writeheader()
                        csvwriter.writerows(data)

                    history = []
                    with open('history_transaksi.csv', 'r') as csvfile:
                        csvreader = csv.DictReader(csvfile)
                        for row in csvreader:
                            history.append(row)
                    used_reference_numbers = set(int(row['no_referensi']) for row in history)

                    new_reference_number = 1
                    while new_reference_number in used_reference_numbers:
                        new_reference_number += 1
                    
                    history.append({'no_referensi' : new_reference_number,
                                    'user' : user,
                                    'tanggal' : tanggal,
                                    'nama_masalah' : masalah_terpilih,
                                    'nama_barang' : obat_terpilih['nama_obat'],
                                    'harga' : obat_terpilih['harga'],
                                    'quantity' : jumlah
                                    })
                    
                    with open('history_transaksi.csv', 'w', newline='') as csvfile:
                        fieldnames = ['no_referensi', 'user','tanggal', 'nama_masalah', 'nama_barang', 'harga', 'quantity']
                        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        csvwriter.writeheader()
                        csvwriter.writerows(history)

                else:
                    print("Stok obat tidak mencukupi.")
        else: 
            print("Pilihan obat tidak valid.")
    else:
        print("Pilihan masalah kesehatan tidak valid.")


def cetak_nota(user, tanggal, nama_masalah, nama_obat, harga_obat, jumlah, total_harga):
    print("  NOTA PEMBELIAN  ".center(78,"="))
    print(f"Tanggal \t\t: {tanggal}")
    print(f"Nama Pembeli\t\t: {user}")
    print(f"Masalah Kesehatan\t: {nama_masalah}")
    print(f"Obat yang dibeli\t: {nama_obat}")
    print(f"Jumlah\t\t\t: {jumlah}")
    print(f"Harga per unit\t\t: Rp. {harga_obat} ")
    print(f"Total harga\t\t: Rp. {total_harga} ")
    print("  TERIMA KASIH ATAS KUNJUNGANNYA  ".center(78,"="))

def update_data():
    print("  UPDATE HARGA DAN STOK  ".center(78,"="))
    input_file = 'obat.csv'
    output_file = 'obat.csv'
    data = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    data_masalah = baca_data_obat()
    tampilkan_daftar_masalah_kesehatan(data_masalah)
    update_masalah  = int(input("Masukkan nama masalah kesehatan yang ingin diperbarui: "))
    data = list(set(i["masalah_kesehatan"] for i in data_masalah))
    
    if 1 <= update_masalah <= len(data):
        masalah_terpilih = data[update_masalah - 1]

        obat_masalah = [item for item in data_masalah if item['masalah_kesehatan'] == masalah_terpilih]
        print("Daftar Obat:")
        for idx, obat in enumerate(obat_masalah, start=1):
            print(f"{idx}. {obat['nama_obat']}")
        update_obat = int(input("Masukkan nama obat yang ingin diperbarui\t: "))
        update_harga = input("Masukkan harga yang baru\t\t\t: ")
        update_stok = input("Masukkan stok yang baru\t\t\t\t: ")
        obat_terpilih = obat_masalah[update_obat - 1]

    data_ditemukan = False

    for row in data_masalah:
        if row['masalah_kesehatan'] == masalah_terpilih and row['nama_obat'] == obat_terpilih['nama_obat']:
            row['masalah_kesehatan'] = masalah_terpilih
            row['nama_obat'] = obat_terpilih['nama_obat']
            if update_harga != "":
                row['harga'] = update_harga
            if update_stok != "":
                row['stok'] = update_stok
            data_ditemukan = True

    if not data_ditemukan:
        print("Data tidak ditemukan. Tidak ada pembaruan yang dilakukan.")

    else:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['masalah_kesehatan', 'nama_obat', 'harga', 'kegunaan', 'stok']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(data_masalah)

        print(f"Data telah diubah dan disimpan dalam file {output_file}")

def tambah_data():
    print("  SILAHKAN TAMBAH DATA OBAT  ".center(78,"="))
    input_file = 'obat.csv'
    output_file = 'obat.csv'

    data = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    
    masalah_kesehatan = input("Masukkan masalah kesehatan baru: ")
    nama_obat = input("Masukkan nama obat baru : ")
    harga = input("Masukkan harga\t\t: ")
    kegunaan = input("Masukkan kegunaan\t: ")
    stok = input("Masukkan stok\t\t : ")

    data_baru = {
        'masalah_kesehatan': masalah_kesehatan,
        'nama_obat': nama_obat,
        'harga': harga,
        'kegunaan': kegunaan,
        'stok': stok
    }

    data.append(data_baru)


    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['masalah_kesehatan', 'nama_obat', 'harga', 'kegunaan', 'stok']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)

    print(f"Data baru telah ditambahkan dan disimpan dalam file {output_file}")

def tulis_data_obat(nama_file, data_obat_list):
    with open(nama_file, 'w', newline='', encoding='utf-8') as file_csv:
        fieldnames = ["masalah_kesehatan", "nama_obat", "harga", "kegunaan", "stok"]
        writer_csv = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer_csv.writeheader()
        writer_csv.writerows(data_obat_list)


def hapus_data(nama_file, masalah_kesehatan_hapus):
    print("  HAPUS DATA OBAT ".center(78,"="))
    data_obat_list = baca_data_obat()
    try:
        masalah_kesehatan_hapus = int(masalah_kesehatan_hapus)
        
        if 1 <= masalah_kesehatan_hapus <= len(data_obat_list):
            del data_obat_list[masalah_kesehatan_hapus - 1]
            print(f"Data dengan nomor masalah kesehatan {masalah_kesehatan_hapus} berhasil dihapus.")
            print('Data berhasil di Hapus !!')
        else:
            print("Nomor yang dimasukkan tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

    tulis_data_obat(nama_file, data_obat_list)

def pickone_line(data):
    found_data = []  
    with open("history_transaksi.csv", 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row["no_referensi"] == data:
                found_data.append(row) 
    return found_data

def admin_menu2():
    print("  Pilihan Menu  ".center(78, "=",))
    print("1. Cetak Nota")
    print("2. Update Data")
    print("3. Tambah Data")
    print("4. Hapus Data")
    print("5. Kembali ke menu awal")
    print("6. Log Out")
    print('='*81)
    pilih = input('Pilih Menu Yang Ingin Digunakan: ')
    print("Permintaan anda kami proses".center(81))
    print("="*81)
    time.sleep(1)
    if pilih == '1':
        os.system('cls')
        loop = True
        while loop:
            try:
                no_referensi = input("Masukkan Nomor Referensi : ").lower()
                data = pickone_line(no_referensi)
                cetak_nota(data[0]["user"],data[0]["tanggal"],data[0]["nama_masalah"], data[0]["nama_barang"], data[0]["harga"], data[0]["quantity"], int(data[0]["harga"]) * int(data[0]["quantity"]))
                loop = False
            except:
                print("Masukkan No Referensi Yang Benar")
                input("Tekan Enter ")
        balik_admin()
    elif pilih == '2':
        os.system('cls')
        baca_data_obat()
        update_data()
        balik_admin()
    elif pilih == '3':
        os.system('cls')
        tambah_data()
        balik_admin()
    elif pilih == '4':
        os.system('cls')
        print("  HAPUS DATA OBAT ".center(78,"="))
        data_obat_sebelum = baca_data_obat()
        print("Data Obat Sebelum Dihapus:")
        for idx, obat in enumerate(data_obat_sebelum, start=1):
            print(f"{idx}. {obat['masalah_kesehatan']}: {obat['nama_obat']}")
        masalah_kesehatan_hapus = input("Masukkan nomor yang ingin anda hapus :" )
        hapus_data('obat.csv', masalah_kesehatan_hapus)
        data_obat_setelah = baca_data_obat()
        print("\nData Obat Setelah Dihapus:")
        for idx, obat in enumerate(data_obat_setelah, start=1):
            print(f"{idx}. {obat['masalah_kesehatan']}: {obat['nama_obat']}")
        balik_admin()
    elif pilih == '5':
        os.system('cls')
        menu_awal()
    elif pilih == "6":
        os.system('cls')
        print('Terimakasih telah menggunkan aplikasi SmartApotek!!'.center(81))
        exit()  
    else:
        print('pilihan tidak valid!!!')


def user_menu2():
    print("  Pilihan Menu  ".center(78, "=",))
    print("1. Beli Obat")
    print("2. Kembali ke menu awal")
    print("3. Log Out")
    print('-'*81)
    pilih = input('Pilih Menu Yang Ingin Digunakan : ')
    print("Permintaan anda kami proses".center(81))
    print("="*81)
    time.sleep(1)
    print('-'*81)
    if pilih == '1':
        os.system('cls')
        data_masalah_kesehatan = baca_data_obat()
        beli_obat(data_masalah_kesehatan)
        balik_user()
    elif pilih == '2':
        os.system('cls')
        menu_awal()
    elif pilih == "3":
        os.system('cls')
        print('Terimakasih telah menggunkan aplikasi SmartApotek!!'.center(81))
        exit() 
    else:
        print('pilihan tidak valid!!!')

menu_awal()
