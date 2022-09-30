# Kalkulator by Khansa Mahira #

print("List operator: [ + ; - ; * ; / ; ^ ; = ]")

try:
    angka_awal = float(input("Masukkan nilai: "))
    tanda = input("Operator: ")
    angka = angka_awal


    while tanda != "=":
        if tanda == "+":
            angka_berikutnya = float(input("Masukkan nilai: "))
            angka_update = angka_berikutnya
            angka += angka_update
            print("Kalkulasi nilai:", angka)
        elif tanda == "-":
            angka_berikutnya = float(input("Masukkan nilai: "))
            angka_update = angka_berikutnya
            angka -= angka_update
            print("Kalkulasi nilai:", angka)
        elif tanda == "*":
            angka_berikutnya = float(input("Masukkan nilai: "))
            angka_update = angka_berikutnya
            angka *= angka_update
            print("Kalkulasi nilai:", angka)
        elif tanda == "/":
            angka_berikutnya = float(input("Masukkan nilai: "))
            angka_update = angka_berikutnya
            angka /= angka_update
            print("Kalkulasi nilai:", angka)
        elif tanda == "^":
            pangkat = int(input("Masukkan nilai: "))
            angka = angka ** pangkat
            print("Kalkulasi nilai:", angka)
        else:
            print("Maaf anda memasukkan input operator yang tidak sesuai.\nSilahkan masukkan input operator yang sesuai.")
        tanda = input("Operator: ")
    print("Hasil akhir:", angka)

except ValueError:
    print("Maaf anda memasukkan input nilai yang tidak sesuai.\nProgram berhenti.")
    exit()