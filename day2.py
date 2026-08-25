# 1 Struktur data soal yang berisi pertanyaan, pilihan jawaban, dan jawaban yang benar
daftar_soal = [
    {
        "pertanyaan": "Apa bahasa internasional yang digunakan untuk komunikasi di seluruh dunia?",
        "pilihan": ["A. Inggris", "B. Spanyol", "C. Mandarin", "D. Arab"],
        "jawaban": "A",
    },
    {
        "pertanyaan": "Apa bahasa resmi yang digunakan di Indonesia?",
        "pilihan": ["A. Inggris", "B. Indonesia", "C. Jepang", "D. Prancis"],
        "jawaban": "B",
    },
    {
        "pertanyaan": "Berapa jumlah provinsi di Indonesia?",
        "pilihan": ["A. 38", "B. 34", "C. 36", "D. 32"],
        "jawaban": "A",                 
    },
    {
        "pertanyaan": "Apa ibukota dari Indonesia?",
        "pilihan": ["A. Jakarta", "B. Surabaya", "C. Bandung", "D. Medan"],
        "jawaban": "A",
    },
    {
        "pertanyaan": "Apa mata uang resmi yang digunakan di Indonesia?",
        "pilihan": ["A. Dollar", "B. Euro", "C. Rupiah", "D. Yen"],
        "jawaban": "C",
    },
]

skor = 0

print("Hallo! Selamat datang di kuis sederhana ini :) Hope you enjoy it!")

# 2 Looping/ perulangan otomatis untuk setiap soal yang ada di daftar_soal
for i, item in enumerate(daftar_soal, 1):
    print(f"\nSoal {i}: {item['pertanyaan']}")
    
    for pilihan in item["pilihan"]:
        print(pilihan)

    jawaban_user = input("Masukkan jawaban Anda (A/B/C/D): ").upper()

    # cek jawaban user dengan jawaban yang benar
    if jawaban_user == item["jawaban"]:
        print("✅Jawaban Anda benar!")
        skor += 10
    else:
        print(f"❌Jawaban Anda salah! Jawaban yang benar adalah: {item['jawaban']}")

# 3 Evaluasi hasil kuis
print("\n" + "="*30)
print(f"HASIL AKHIR: {skor} / {len(daftar_soal) * 10}")

if skor == len(daftar_soal) * 10:
    print("Selamat! Anda mendapatkan skor sempurna!")
elif skor > 0:
    print("Bagus, tingkatkan lagi!.")
else:
    print("Keep trying! Anda bisa lebih baik.")
