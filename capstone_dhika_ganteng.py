# import os

# define a dictionary to hold data
stock_gudang = {'KODE BARANG' : ['KK001', 'MK001', 'KB001'],
                'NAMA BARANG' : ['KURSI KAYU', 'MEJA KAYU', 'KURSI BESI'],
                'TOTAL STOK' : [5, 6, 4],
                'HARGA POKOK' : [75000, 95000, 80000],
                'HARGA JUAL' : [125000, 145000, 130000]
}

nama_kolom = []
value_kode_barang = []
value_nama_barang = []
value_total_stok = []
value_harga_pokok = []
value_harga_jual = []
list_semua_value = value_kode_barang + value_nama_barang + value_total_stok + value_harga_pokok + value_harga_jual
index = len(stock_gudang["NAMA BARANG"])

for i in stock_gudang.keys():
    nama_kolom.append(i)

def input_value_in_list(nama_kolom, nama_list):
    for i in range(len(stock_gudang[nama_kolom])):
        nama_list.append(stock_gudang[nama_kolom][i])

input_value_in_list("KODE BARANG", value_kode_barang)
input_value_in_list("NAMA BARANG", value_nama_barang)
input_value_in_list("TOTAL STOK", value_total_stok)
input_value_in_list("HARGA POKOK", value_harga_pokok)
input_value_in_list("HARGA JUAL", value_harga_jual)



# main function to display menu
def main():
    
    print("|======================================================================================================|")
    print("|--------------------------------------- BETA SYSTEM STOCK OPNAME -------------------------------------|")
    print("|=========================================== GUDANG KAYU CERIA ========================================|")
    print("|______________________________________________________________________________________________________|")
    print("\t\t\t\t      |1.| Lihat Stok Data Barang|")
    print("\t\t\t\t      |2.| Tambah Stok Data Baru |")
    print("\t\t\t\t      |3.| Perbarui Stok Data    |")
    print("\t\t\t\t      |4.| Hapus Stok Data       |")
    print("\t\t\t\t      |5.| Keluar                |")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        menu_1()
    elif choice == '2':
        menu_2()
    elif choice == '3':
        menu_3()
    elif choice == '4':
        menu_4()
    elif choice == '5':
        exit_programme()
    else:
        print("Input yang anda masukkan salah.")
        main()

# MENU 1
def menu_1():
    
    print('''
    |------------------------- SILAHKAN PILIH SALAH SATU OPSI YANG TERSEDIA --------------------------|

    \tPilih Opsi :
    \t1. Tampilkan Seluruh Stok
    \t2. Tampilkan Stok Yang Diinginkan
    \t3. Kembali
    ''')

    tampilan_menu_baca = input('Enter Your Choice:')

    if tampilan_menu_baca == '1' :
        create_table()
        input("\n\n\n|Enter| to continue.")
        menu_1()
    elif tampilan_menu_baca == '2' :
        sub_menu1()
        input("\n\n\n\n|ENTER| to continue.")
        menu_1()
    elif tampilan_menu_baca == '3':
        main()
    else :
        print('Pilihan Tidak Tersedia, silahkan pilih opsi yang ada.')
        menu_1()

def create_table():
    global nama_kolom
    a_space = " "
    print('''
    |======================================= AVAILABLE STOCK =======================================|
    |====================================== GUDANG KAYU CERIA ======================================|
    |_______________________________________________________________________________________________|
          ''')
    print(f"{a_space: <5}{nama_kolom[0]: <20}|{nama_kolom[1]: <20}|{nama_kolom[2]: <20}|{nama_kolom[3]: <20}|{nama_kolom[4]: <20}")

    for i in range(len(stock_gudang[nama_kolom[0]])) :
        print(f'{a_space: <5}{(stock_gudang[nama_kolom[0]][i]): <20}|{(stock_gudang[nama_kolom[1]][i]): <20}|{(stock_gudang[nama_kolom[2]][i]): <20}|{(stock_gudang[nama_kolom[3]][i]): <20}|{(stock_gudang[nama_kolom[4]][i]): <20}')

def sub_menu1() :
    global stock_gudang
    global nama_kolom
    a_space = " "

    input_value = input('Masukan Nama barang Yang ingin di cari :').upper()

    while input_value not in stock_gudang['NAMA BARANG'] :
        print("Input yang anda masukkan salah, coba lagi.")
        input_value = input('Masukan Informasi Yang Diinginkan :').upper()
    else :
        global nama_kolom
        a_space = " "
        
        print('''
    ======================================= AVAILABLE STOCK =======================================
    ====================================== GUDANG KAYU CERIA ======================================
            ''')
        print(f"{a_space: <5}{nama_kolom[0]: <20}|{nama_kolom[1]: <20}|{nama_kolom[2]: <20}|{nama_kolom[3]: <20}|{nama_kolom[4]: <20}")
        print(f'{a_space: <5}{(stock_gudang[nama_kolom[0]][stock_gudang["NAMA BARANG"].index(input_value)]): <20}|{(stock_gudang[nama_kolom[1]][stock_gudang["NAMA BARANG"].index(input_value)]): <20}|{(stock_gudang[nama_kolom[2]][stock_gudang["NAMA BARANG"].index(input_value)]): <20}|{(stock_gudang[nama_kolom[3]][stock_gudang["NAMA BARANG"].index(input_value)]): <20}|{(stock_gudang[nama_kolom[4]][stock_gudang["NAMA BARANG"].index(input_value)]): <20}')

def search_index(temp_index, input_value):
    global stock_gudang
    global nama_kolom

    an_index = stock_gudang[nama_kolom[temp_index].index(input_value)]
    return an_index


# MENU 2
def menu_2():
    print('''
    |-------------------------------------- TAMBAH STOCK BARU --------------------------------------|

    \tPilih Opsi :
    \t1. Buat item
    \t2. Kembali
    ''')

    tampilan_menu_buat = input('Enter Your Choice:')

    if tampilan_menu_buat == '1' :
        menu2_sub1()
        create_table()
        menu_2()
    elif tampilan_menu_buat == '2':
        main()
    else :
        print('Pilihan Tidak Tersedia, silahkan pilih opsi yang ada.')
        menu_2()
    
def menu2_sub1():
    global stock_gudang

    # Cek input kode barang
    input_kode_barang = input("Input kode barang dengan format 'XXYYY'\n\n'XX' adalah Inisial Nama Barang.\n\n'YYY' adalah Kode barang. \n\nXXYYY =").upper()

    while input_kode_barang.isalnum() == False and input_kode_barang not in stock_gudang["KODE BARANG"]:
        print("Input yang anda masukkan salah, silahkan input kembali.\n")
        input_kode_barang = input("Input kode barang dengan format 'XXYYY'\n\n'XX' adalah Inisial Nama Barang.\n\n'YYY' adalah Kode barang: ").upper()

        if input_kode_barang[0:2].isalpha() and input_kode_barang[2:].isnumeric() and input_total_stok in stock_gudang["KODE BARANG"]:
            break
        else:
            pass
    else:
        pass

    input_nama_barang = input("\nInput nama barang : ").upper()

    while input_nama_barang.isnumeric() and input_nama_barang not in stock_gudang["NAMA BARANG"]:
        print("Input yang anda masukkan salah, silahkan input kembali.\n")
        input_nama_barang = input("\nInput nama barang: ").upper()

        if input_nama_barang.isalpha() and input_nama_barang in stock_gudang["NAMA BARANG"]:
            break
        else:
            pass
    else:
        pass

    input_total_stok = input("\nInput total stock: ")

    while input_total_stok.isalpha():
        print("Input yang anda masukkan salah, silahkan input kembali.\n")
        input_total_stok = input("\nInput kembali total stock: ")

        if input_total_stok.isnumeric():
            input_total_stok = int(input_total_stok)
            break
        else:
            pass
    else:
        input_total_stok = int(input_total_stok)

    input_harga_pokok = input("\nInput harga pokok: ")

    while input_harga_pokok.isalpha():
        print("Input yang anda masukkan salah, silahkan input kembali.\n")
        input_harga_pokok = input("\nInput kembali harga pokok: ")

        if input_harga_pokok.isnumeric():
            input_harga_pokok = int(input_harga_pokok)
            break
        else:
            pass
    else:
        input_harga_pokok = int(input_harga_pokok)

    input_harga_jual = input("\nInput harga jual: ")

    while input_harga_jual.isalpha():
        print("Input yang anda masukkan salah, silahkan input kembali.\n")
        input_harga_jual = input("\nInput kembali harga jual: ")

        if input_harga_jual.isnumeric():
            input_harga_jual = int(input_harga_jual)
            break
        else:
            pass
    else:
        input_harga_jual = int(input_harga_jual)

    apakah_anda_yakin_insert(input_kode_barang, input_nama_barang, input_total_stok, input_harga_pokok, input_harga_jual)

def apakah_anda_yakin_insert(input_kode_barang, input_nama_barang, input_total_stok, input_harga_pokok, input_harga_jual):
    user_input = input("\nApakah anda yakin ingin memasukkan data ke dalam tabel (y/n)?")

    if user_input == 'y':
        stock_gudang[nama_kolom[0]].append(input_kode_barang)
        stock_gudang[nama_kolom[1]].append(input_nama_barang)
        stock_gudang[nama_kolom[2]].append(input_total_stok)
        stock_gudang[nama_kolom[3]].append(input_harga_pokok)
        stock_gudang[nama_kolom[4]].append(input_harga_jual)
        create_table()
        input(" \nData berhasil ditambah. \n\n\n|ENTER| to continue.")
        menu_2()
    elif user_input == 'n':
        create_table()
        input(" \nData tidak berhasil ditambah. \n\n\n|ENTER| to continue.")
        menu_2()
    else:
        print("Input yang anda masukkan salah, silahkan input ulang")
        apakah_anda_yakin_insert(input_kode_barang, input_nama_barang, input_total_stok, input_harga_pokok, input_harga_jual)


# MENU 3
def menu_3():
    print('''
    |---------------------- UBAH ITEM DALAM SYSTEM GUDANG ----------------------|

    \tPilih Opsi :
    \t1. Ubah item
    \t2. Kembali
    ''')

    tampilan_menu_ubah = input('Enter Your Choice:')

    if tampilan_menu_ubah == '1' :
        create_table()
        input("\n\n|ENTER TO CONTINUE|")
        menu3_sub1()
        menu_3()
    elif tampilan_menu_ubah == '2':
        main()
    else :
        print('Pilihan Tidak Tersedia, silahkan pilih opsi yang ada.')
        menu_3()

def menu3_sub1():
    global nama_kolom
    global value_kode_barang
    global value_nama_barang
    global value_total_stok
    global value_harga_pokok
    global value_harga_jual
    global list_semua_value

    input_nama_kolom = input("\nInput nama kolom: ")

    while input_nama_kolom.upper() not in nama_kolom:
        print("Nama kolom tidak ada, silahkan input ulang")
        input_nama_kolom = input("Input nama kolom: ")

        if input_nama_kolom.upper() in nama_kolom:
            input_nama_kolom = input_nama_kolom.upper()
            break
        else:
            pass
    else:
        input_nama_kolom = input_nama_kolom.upper()

    if input_nama_kolom == nama_kolom[0]:
        input_value_lama = input("Input value lama: ")

        while input_value_lama.upper() not in value_kode_barang:
            print("Input yang anda masukkan salah, silahkan input ulang")
            input_value_lama = input("Input value lama")

            if input_value_lama.upper() in value_kode_barang:
                input_value_lama = input_value_lama.upper()
                break
            else:
                pass
        else:
            input_value_lama = input_value_lama.upper()

    elif input_nama_kolom == nama_kolom[1]:
        input_value_lama = input("Input value lama: ")

        while input_value_lama.upper() not in value_nama_barang:
            print("Input yang anda masukkan salah, silahkan input ulang")
            input_value_lama = input("Input value lama: ")

            if input_value_lama.upper() in value_nama_barang:
                input_value_lama = input_value_lama.upper()
                break
            else:
                pass
        else:
            input_value_lama = input_value_lama.upper()

    elif input_nama_kolom == nama_kolom[2]:
        input_value_lama = input("Input value lama: ")

        while int(input_value_lama) not in value_total_stok and input_value_lama.isalpha():
            print("Input yang anda masukkan salah, silahkan input ulang")
            input_value_lama = input("Input value lama: ")

            if input_value_lama.isnumeric() and int(input_value_lama) in value_total_stok:
                input_value_lama = int(input_value_lama)
                break
            else:
                pass
        else:
            input_value_lama = int(input_value_lama)

    elif input_nama_kolom == nama_kolom[3]:
        input_value_lama = input("Input value lama: ")

        while int(input_value_lama) not in value_harga_pokok and input_value_lama.isalpha():
            print("Input yang anda masukkan salah, silahkan input ulang")
            input_value_lama = input("Input value lama: ")

            if input_value_lama.isnumeric() and int(input_value_lama) in value_harga_pokok:
                input_value_lama = int(input_value_lama)
                break
            else:
                pass
        else:
            input_value_lama = int(input_value_lama)
    
    elif input_nama_kolom == nama_kolom[4]:
        input_value_lama = input("Input value lama: ")

        while int(input_value_lama) not in value_harga_jual and input_value_lama.isalpha():
            print("Input yang anda masukkan salah, silahkan input ulang")
            input_value_lama = input("Input value lama: ")

            if input_value_lama.isnumeric() and int(input_value_lama) in value_harga_jual:
                input_value_lama = int(input_value_lama)
                break
            else:
                pass
        else:
            input_value_lama = int(input_value_lama)


    input_value_baru = input("Input value baru: ")

    if input_value_baru.isnumeric():
        while int(input_value_baru) in list_semua_value:
            print("Input yang anda masukkan sudah ada, silahkan input value baru")
            input_value_baru = input("Input value baru: ")
            input_value_baru = int(input_value_baru)

            if input_value_baru not in list_semua_value:
                break
            else:
                pass
        else:
            input_value_baru = int(input_value_baru)

    else:
        while input_value_baru in list_semua_value:
            print("Input yang anda masukkan sudah ada, silahkan input value baru")
            input_value_baru = input("Input value baru: ").upper()

            if input_value_baru not in list_semua_value:
                break
            else:
                pass
        else:
            input_value_baru = input_value_baru.upper()


    update_atau_tidak = input("Apakah anda ingin memperbaharui informasi tersebut (y/n)?")

    while update_atau_tidak != "y" and update_atau_tidak != 'n':
        print("Input yang anda masukkan salah, silahkan input ulang")
        update_atau_tidak = input("Apakah anda ingin memperbaharui informasi tersebut (y/n)?")
    else:
        if update_atau_tidak == "y":

            an_index = stock_gudang[input_nama_kolom].index(input_value_lama)
            stock_gudang[input_nama_kolom][an_index] = input_value_baru
            create_table()
            input('\nData berhasil diperbarui.\n\n\t\t\t\t\t -|ENTER TO CONTINUE|-')
            menu_3()
    
        elif update_atau_tidak == 'n':
            create_table()
            print('\nData gagal diperbarui.')
            input('\n|ENTER TO CONTINUE|')
            menu_3()

# MENU 4 (DELETE)
def menu_4():
    print('''
    |------------------------ HAPUS ITEM DALAM GUDANG ---------------------|

    \tPilih Opsi :
    \t1. Hapus item
    \t2. Kembali
    ''')

    tampilan_menu_hapus = input('Enter Your Choice:')

    if tampilan_menu_hapus == '1' :
        create_table()
        menu4_sub1()
        menu_4()
    elif tampilan_menu_hapus == '2':
        main()
    else :
        print('Pilihan Tidak Tersedia, silahkan pilih opsi yang ada.')
        menu_4()

def menu4_sub1():
    global value_nama_barang

    print('''\n
    | ADA BARANG.
    ''')

    nama_barang = input('Masukkan "NAMA BARANG" yang ingin dihapus: ')

    
    while nama_barang.upper() not in value_nama_barang :
        print("\n\n\tBarang tidak ditemukan dalam system, silahkan input ulang.")
        nama_barang = input('\n\n\t\tMasukan nama barang yang ingin dihapus:')
    
        if nama_barang.upper() in value_nama_barang :
            index = stock_gudang['NAMA BARANG'].index(nama_barang.upper())
            confirm = input('Anda yakin ingin menghapus data tersebut? \n(y/n) :\n\n\t\t\t|PRESS "ENTER" TO CANCEL| ')
            if confirm == 'y':
                nama_barang = nama_barang.upper()
                break
            else:
                create_table()
                print('\n\nData gagal dihapus.')
                input('\n|ENTER TO CONTINUE -->')
                menu_4()
    else:
        nama_barang = nama_barang.upper()
        index = stock_gudang['NAMA BARANG'].index(nama_barang)
        confirm = input('\nAnda yakin ingin menghapus data tersebut? \n(y/n) :\n\n\t\t\t|PRESS "ENTER" TO CANCEL| ')
        if confirm == 'y' :
            nama_barang = nama_barang.upper()
        else :
            create_table()
            print('\n\nData gagal dihapus.')
            input('\n|ENTER TO CONTINUE -->')
            menu_4()
    

    del stock_gudang['KODE BARANG'][index]
    del stock_gudang['NAMA BARANG'][index]
    del stock_gudang['TOTAL STOK'][index]
    del stock_gudang['HARGA POKOK'][index]
    del stock_gudang['HARGA JUAL'][index]
    create_table()
    print('\n\nData berhasil dihapus.')
    input('\n|ENTER TO CONTINUE -->')



def exit_programme() :

    keluar_var = input('Apakah anda yakin untuk keluar dari system (y/n) ?')

    if keluar_var == 'y' :
         print('''
            --------------T e R i M a ==== K a S i H----------------
            ====== telah menggunakan system beta gudang kayu =======
            ''')
         exit()
    else :
        main()


      
        
    
    
        
        
        




main()
        
        




