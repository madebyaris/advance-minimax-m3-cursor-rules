# Memakai aturan ini kalau kamu bukan programmer

**Bahasa:** [English](FOR-NON-DEVELOPERS.md) · Bahasa Indonesia

Kamu **tidak** perlu bisa coding untuk mendapat banyak manfaat dari ini. Aturan-aturan ini
adalah sekumpulan instruksi yang membuat AI di dalam Cursor bertindak seperti seorang
*engineer* senior yang teliti — bukan seperti anak magang yang terlalu pede. Halaman ini
menjelaskan, dengan bahasa sederhana, apa yang aturan ini lakukan untukmu dan cara
memakainya.

Kalau ada istilah yang asing, lihat [kamus kecil](#kamus-kecil) di bagian bawah.

---

## Apa yang sebenarnya dilakukan aturan ini untukmu

Tanpa aturan apa pun, asisten AI cenderung menebak-nebak, menulis banyak kode dengan
cepat, lalu bilang "sudah selesai" entah benar-benar jalan atau tidak. Di situlah pengguna
non-teknis sering kena getahnya.

Dengan aturan ini aktif, asisten didorong untuk:

- **Lihat dulu sebelum bertindak.** Dia membaca proyekmu yang sebenarnya, bukan menebak.
- **Melakukan perbaikan sekecil mungkin** yang menyelesaikan masalahmu, bukan menulis ulang
  besar-besaran.
- **Membuktikan hasil kerjanya.** Untuk bug, dia menirukan dulu masalahnya, memperbaikinya,
  lalu mengecek ulang bahwa masalahnya benar-benar hilang. Untuk perubahan tampilan, dia
  melihat hasilnya.
- **Berkata jujur.** Kalau dia tidak yakin, atau tidak bisa menguji sesuatu, dia
  mengatakannya — bukan pura-pura. Dia tidak akan mengarang fakta supaya terdengar pede.
- **Bertanya hanya kalau benar-benar perlu.** Dia tidak akan menghujanimu dengan pertanyaan
  teknis yang sebenarnya bisa dia jawab sendiri dengan melihat proyekmu.
- **Tidak mengutak-atik rahasiamu.** Dia diperintahkan untuk tidak membuka atau menampilkan
  file berisi password dan kunci (*key*).

Singkatnya: dia dirancang untuk jujur dan selalu memverifikasi — hal yang justru sulit kamu
cek sendiri.

---

## Pasang dalam tiga langkah

Kamu butuh aplikasi **Cursor** (gratis, unduh di [cursor.com](https://cursor.com)) dan
folder aturan dari proyek ini.

1. **Unduh proyek ini.** Di halaman GitHub proyek, klik tombol hijau **Code**, lalu
   **Download ZIP**, dan ekstrak. (Atau, kalau ada yang sudah menyiapkan proyeknya untukmu,
   mungkin sudah ada di sana.)
2. **Salin folder `.cursor` ke dalam proyekmu.** Cari folder bernama `.cursor` di dalam
   hasil unduhan, lalu salin ke bagian paling atas folder proyekmu. Titik di depan namanya
   memang disengaja; folder ini bisa jadi tersembunyi secara default
   (di Mac, tekan `Cmd+Shift+.` untuk menampilkan file tersembunyi).
3. **Buka proyekmu di Cursor.** Selesai. Dua aturan inti langsung aktif otomatis. Sisanya
   memuat sendiri hanya saat sebuah tugas membutuhkannya.

Kamu tidak akan melihat popup konfirmasi — aturan bekerja diam-diam di latar belakang.
Untuk memastikan, coba saja minta sesuatu ke asisten dan perhatikan dia memeriksa file-mu
sebelum bertindak.

---

## Cara bicara dengannya

Kebiasaan paling penting: **jelaskan hasil yang kamu inginkan dengan bahasa sederhana.
Jangan mencoba menjelaskan solusi teknisnya.** Kamulah yang paling tahu seperti apa
"bagus" itu; biar dia yang memikirkan caranya.

Contoh permintaan yang natural dan bagus (ini nyata, dan asisten menanganinya dengan baik):

| Yang kamu ketik | Yang dia lakukan |
|---|---|
| "website saya lemot banget tolong bikin cepat" | Membuka proyekmu, menemukan bagian yang lambat, memperbaikinya, lalu menjelaskan peningkatannya. |
| "total di halaman penjualan beda sama spreadsheet saya, perbaiki" | Menemukan perhitungannya, menirukan angka yang salah, memperbaiki bug-nya, lalu memastikan totalnya kini cocok. |
| "buat situs saya jalan di iphone" | Membuat tata letak muat di layar HP dan menu bisa di-tap, lalu mengeceknya. |
| "saya mau orang bisa booking janji temu dengan saya" | Menyarankan opsi paling sederhana lebih dulu (sering kali alat tanpa-kode), dan bertanya beberapa hal singkat sebelum membangun apa pun. |

Perhatikan polanya: kamu menyebut *tujuan*, bukan "ubah CSS flexbox" atau "refactor
controller". Kalau kamu tahu istilah-istilah itu, mungkin kamu tidak butuh halaman ini.

Kamu juga bisa **menempelkan tangkapan layar (screenshot)** dari sesuatu yang terlihat
salah. Asisten bisa membaca gambar, jadi foto halaman yang rusak sering kali adalah cara
tercepat menjelaskan masalah.

---

## Cara menulis prompt yang baik (rumus sederhana)

Kamu tidak butuh istilah teknis. Permintaan yang andal menjawab tiga pertanyaan kecil:

1. **Apa yang kamu mau?** — hasilnya, dengan bahasa sederhana.
2. **Di mana / apa yang terpengaruh?** — halaman, layar, atau fitur (kalau kamu tahu).
3. **Seperti apa "berhasil" itu?** — bagaimana kamu tahu ini sudah jalan.

Anggap saja rumusnya: **Tujuan + Di mana + Tanda-berhasil.** Tidak harus selalu ketiganya,
tapi makin lengkap, makin bagus hasilnya.

Lihat bedanya:

| Prompt lemah | Prompt kuat |
|---|---|
| "perbaiki formnya" | "Di form kontak, orang bisa kirim tanpa isi email. Seharusnya wajib isi email yang valid dulu sebelum bisa dikirim." |
| "bikin lebih bagus" | "Halaman harga terasa sempit di HP. Tambahkan jarak antar kartu supaya enak dibaca di layar ponsel." |
| "rusak nih" | "Waktu saya klik **Tambah ke keranjang**, tidak terjadi apa-apa dan keranjang tetap kosong. Seharusnya barangnya masuk dan jumlahnya bertambah." |
| "bikin fitur booking" | "Saya mau klien bisa booking telepon 30 menit dengan saya. Mulai dari opsi paling sederhana — saya belum punya website." |

Beberapa kebiasaan yang membuat prompt lebih ampuh:

- **Jelaskan apa yang kamu lihat, bukan penyebabnya.** "Totalnya tertulis 12, harusnya
  12.500" sudah sempurna — kamu tidak perlu menebak *kenapa*.
- **Satu tujuan per pesan.** Selesaikan satu hal dulu, lalu bilang "sekarang lakukan hal
  yang sama untuk halaman pendaftaran."
- **Tempel screenshot** untuk apa pun yang berkaitan dengan tampilan. Gambar lebih cepat
  daripada satu paragraf.
- **Gugup? Minta dia menjelaskan dulu:** *"Sebelum mengubah apa pun, beri tahu saya
  rencanamu."* Kamu bisa menyetujui, lalu bilang "lanjut."
- **Lanjutan yang berguna:** *"Bagaimana kamu memverifikasi ini jalan?"*, *"Tunjukkan apa
  yang kamu ubah"*, *"Batalkan itu"*, *"Jelaskan ke saya seperti saya bukan programmer."*

> **Templat siap-tempel:**
> *"Saya mau [tujuanmu]. Ini ada di [halaman/fitur]. Sekarang [yang terjadi]; seharusnya
> [yang kamu inginkan]. Tolong lakukan perubahannya dan beri tahu saya bagaimana kamu
> memastikan ini berhasil."*

---

## Apa yang akan kamu terima sebagai balasan

Jawaban yang baik biasanya memberi tahu kamu, di bagian akhir:

- **apa yang dia ubah** (file mana, dengan bahasa sederhana),
- **apa yang dia cek** untuk memastikan ini jalan, dan
- **apa saja yang belum bisa dia pastikan**, supaya kamu tahu apa yang perlu kamu coba
  sendiri.

Kamu mungkin melihat kata-kata status seperti ini. Berikut artinya untukmu:

| Kalau dia bilang | Artinya |
|---|---|
| **verified** (terverifikasi) | Dia benar-benar mengujinya dan melihatnya jalan. |
| **unverified** / **implemented but unverified** | Dia sudah membuat perubahannya tapi belum bisa menguji sepenuhnya — tolong coba sendiri. |
| **blocked** (terhambat) | Dia menemui sesuatu yang tidak bisa dilewati dan butuh masukan atau akses darimu. |
| **assumption** (asumsi) | Dia membuat dugaan yang masuk akal; cek ulang kalau ini penting. |

Kalau kamu cuma melihat "Selesai!" tanpa keterangan apa yang dicek, tanyakan: *"Bagaimana
kamu memverifikasi ini jalan?"* Aturan ini menyuruhnya menjawab dengan jujur.

---

## Beberapa tips yang berdampak besar

- **Spesifik soal tujuan, longgar soal cara.** "Buat form pendaftaran juga meminta nomor
  HP" lebih baik daripada "edit komponen form-nya."
- **Satu hal dalam satu waktu.** Permintaan kecil memberi hasil lebih andal daripada satu
  permintaan raksasa.
- **Kalau dia bertanya, jawab singkat saja.** Dia hanya bertanya saat sebuah pilihan benar
  penting (misalnya, "mau pelanggan bayar sekarang atau nanti?").
- **Saat ada yang salah, jelaskan yang kamu lihat**, bukan dugaan penyebabnya: "harganya
  tampil 12 padahal harusnya 12.500" itu sempurna.
- **Biarkan dia menguji.** Kalau dia ingin menjalankan proyekmu untuk mengecek hasil
  kerjanya, itu tandanya aturan ini bekerja. Menjawab "ya" biasanya pilihan tepat.
- **Dia tidak akan menyentuh password atau kunci-mu.** Aturan melarangnya membaca atau
  menampilkan file rahasia, jadi kamu tidak perlu khawatir bocor ke dalam obrolan.

---

## Kapan harus melibatkan developer

Aturan ini membuat asisten lebih aman dan lebih jujur, tapi bukan sihir. Libatkan developer
sungguhan ketika:

- perubahannya menyangkut **uang, akun, atau data pribadi** dan harus benar-benar tepat,
- kamu akan **mempublikasikan/men-deploy** sesuatu ke pelanggan sungguhan untuk pertama
  kali, atau
- asisten bilang dia **blocked** pada sesuatu yang tidak bisa dia akses (server, akun,
  perizinan).

Cara sehat memandangnya: asisten ini ibarat *engineer* junior yang cakap dan kini
*menunjukkan cara kerjanya*. Itu peningkatan besar — tapi untuk perubahan berisiko tinggi,
kamu tetap butuh mata seorang senior.

---

## Kamus kecil

- **Cursor** — aplikasi tempat kamu mengetik permintaanmu; ini editor kode dengan AI di
  dalamnya.
- **Proyek / repo** — folder yang berisi file-file website atau aplikasimu.
- **Folder `.cursor`** — folder aturan yang kamu salin tadi; inilah yang membuat asisten
  berperilaku baik.
- **Terminal** — jendela teks untuk mengetik perintah komputer. Umumnya kamu **tidak**
  membutuhkannya untuk ini; asisten yang menjalankan perintahnya untukmu.
- **Deploy / push** — mempublikasikan perubahanmu supaya orang lain bisa melihatnya. Layak
  ditinjau developer untuk pertama kalinya.

---

Mau versi singkat untuk developer, atau ingin melihat bagaimana semua ini diuji terhadap
model-nya? Lihat [README](../README.md) utama dan [harness](../harness/README.md).
