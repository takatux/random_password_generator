import random
import string
import csv

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

data=[]

while True:

    print("\n-------------- MENU ----------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Delete Data")
    print("[5] Exit")

    pilihan = input("Select (1,2,3,4,5) : ")
    if pilihan == "1" :
        try:
            if len(data) == 0:
                no = 0
                #for daftar in data:
                #    print("\n",no,daftar)
                #    no += 1
                with open('data.csv', 'r') as f:
                    reader = csv.reader(f)
                    for daftar in reader:
                        print("\n",no,daftar)
                        no += 1
                        data.append(daftar)
            else:
                no = 0
                for daftar in data:
                    print("\n",no,daftar)
                    no += 1
        except FileNotFoundError:
            print("\nBELUM ADA DATA")
    
    elif pilihan == "2" :
        nama = ""
        while nama != "CUKUP":
            print("ketik CUKUP (menggunakan kapital) untuk selesai input")
            nama = input("Masukkan Nama Anda : ")
            if nama == "CUKUP" :
                print("\n\n================== Input selesai =================")
            else:
                password = randomString(11)
                data.append((nama,password))
        print("========= pilih 5 pada menu untuk simpan dan keluar ========")

    elif pilihan == "3" :
        no = 0
        print("----- LIST DATA ------")
        for daftar in data:
            print(no,daftar)
            no += 1
        indx = input("Index data yang akan di hapus : ")
        indx = int(indx)
        data.pop(indx)
        print(data)

    elif pilihan == "5" :
        with open('data.csv','w') as f:
            w = csv.writer(f)
            for d in data:
                w.writerow(d)
        exit()