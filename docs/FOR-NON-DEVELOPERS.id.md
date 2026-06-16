# Cara memakai rule walau kamu bukan developer

**Bahasa:** [English](FOR-NON-DEVELOPERS.md) · Bahasa Indonesia

Kamu **tidak** perlu bisa coding untuk mendapat banyak manfaat dari rule ini. Rule ini
adalah sekumpulan instruksi yang membuat AI di Cursor bekerja lebih seperti *engineer*
senior yang teliti, bukan AI yang asal menebak dan terlalu percaya diri. Halaman ini
menjelaskan, dengan bahasa sederhana, apa manfaatnya dan cara memakainya.

Kalau ada istilah yang asing, lihat [kamus kecil](#kamus-kecil) di bagian bawah.

---

## Apa yang sebenarnya dilakukan rule ini untukmu

Tanpa rule seperti ini, AI coding assistant sering menebak-nebak, menulis banyak kode
dengan cepat, lalu bilang "sudah selesai" meskipun belum tentu benar-benar jalan. Di
situlah pengguna non-teknis sering dirugikan.

Dengan rule ini aktif, AI didorong untuk:

- **Melihat dulu sebelum bertindak.** Dia membaca proyekmu yang sebenarnya, bukan langsung
  menebak.
- **Memperbaiki seperlunya.** Dia diarahkan untuk membuat perubahan sekecil mungkin yang
  menyelesaikan masalah, bukan melakukan rewrite besar tanpa alasan.
- **Membuktikan hasil kerjanya.** Untuk bug, dia mencoba memunculkan masalahnya dulu,
  memperbaikinya, lalu mengecek ulang bahwa masalahnya benar-benar hilang. Untuk perubahan
  tampilan, dia melihat hasilnya lagi.
- **Jujur soal yang dia tahu dan tidak tahu.** Kalau dia tidak yakin, atau tidak bisa
  menguji sesuatu, dia harus mengatakannya. Dia tidak boleh mengarang fakta supaya
  terdengar yakin.
- **Bertanya hanya kalau benar-benar perlu.** Dia tidak akan menghujanimu dengan pertanyaan
  teknis yang sebenarnya bisa dia cari sendiri di proyekmu.
- **Tidak mengutak-atik rahasiamu.** Dia diperintahkan untuk tidak membuka atau menampilkan
  file berisi password, API key, atau kredensial lain.

Singkatnya: rule ini membuat AI lebih jujur, lebih berhati-hati, dan lebih rajin mengecek
hasil kerjanya. Itu penting, terutama kalau kamu sendiri tidak bisa membaca kode secara
detail.

---

## Cara memasangnya dalam tiga langkah

Kamu butuh aplikasi **Cursor** (gratis, unduh di [cursor.com](https://cursor.com)) dan
folder berisi rule dari proyek ini.

1. **Unduh proyek ini.** Di halaman GitHub proyek, klik tombol hijau **Code**, lalu
   **Download ZIP**, dan ekstrak. (Atau, kalau ada yang sudah menyiapkan proyeknya untukmu,
   mungkin sudah ada di sana.)
2. **Salin folder `.cursor` ke dalam proyekmu.** Cari folder bernama `.cursor` dari hasil
   unduhan, lalu salin ke bagian paling atas folder proyekmu. Titik di depan namanya memang
   disengaja; folder ini bisa jadi tersembunyi secara default
   (di Mac, tekan `Cmd+Shift+.` untuk menampilkan file tersembunyi).
3. **Buka proyekmu di Cursor.** Selesai. Dua rule inti langsung aktif otomatis. Rule dan
   skill lain akan dipakai hanya saat tugasnya memang membutuhkan.

Kamu tidak akan melihat popup konfirmasi. Rule bekerja diam-diam di latar belakang. Untuk
mengecek apakah efeknya terasa, coba minta sesuatu ke AI dan perhatikan apakah dia membaca
file proyekmu sebelum mengubah apa pun.

---

## Cara berbicara dengan AI-nya

Kebiasaan paling penting: **jelaskan hasil yang kamu inginkan dengan bahasa sederhana.
Jangan memaksakan solusi teknis kalau kamu tidak yakin.** Kamulah yang paling tahu seperti
apa hasil yang kamu mau; biarkan AI memikirkan caranya.

Contoh permintaan yang natural dan bagus (ini nyata, dan AI menanganinya dengan baik):

| Yang kamu ketik | Yang dia lakukan |
|---|---|
| "website saya lemot banget, tolong bikin lebih cepat" | Membuka proyekmu, mencari bagian yang lambat, memperbaikinya, lalu menjelaskan peningkatannya. |
| "total di halaman penjualan beda dengan spreadsheet saya, tolong perbaiki" | Menemukan perhitungannya, memunculkan angka yang salah, memperbaiki bug-nya, lalu memastikan totalnya sudah cocok. |
| "buat situs saya nyaman dibuka di iPhone" | Membuat layout muat di layar HP, memastikan menu bisa di-tap, lalu mengeceknya. |
| "saya mau orang bisa booking jadwal dengan saya" | Menyarankan opsi paling sederhana lebih dulu, sering kali tool tanpa kode, lalu bertanya beberapa hal singkat sebelum membangun apa pun. |

Perhatikan polanya: kamu menyebut *tujuan*, bukan "ubah CSS flexbox" atau "refactor
controller". Kalau kamu tahu istilah itu, mungkin kamu tidak butuh halaman ini.

Kamu juga bisa **menempelkan screenshot** dari sesuatu yang terlihat salah. AI bisa membaca
gambar, jadi screenshot halaman yang bermasalah sering kali menjadi cara tercepat untuk
menjelaskan situasinya.

---

## Cara menulis prompt yang baik

Kamu tidak butuh istilah teknis. Prompt yang bagus biasanya menjawab tiga hal sederhana:

1. **Apa yang kamu mau?** — hasil akhirnya, dengan bahasa sederhana.
2. **Di mana / apa yang terpengaruh?** — halaman, layar, atau fitur (kalau kamu tahu).
3. **Seperti apa "berhasil" itu?** — bagaimana kamu tahu perubahannya sudah benar.

Anggap saja rumusnya: **Tujuan + Lokasi + Tanda berhasil.** Tidak harus selalu lengkap,
tapi makin jelas konteksnya, makin bagus hasilnya.

Lihat bedanya:

| Prompt lemah | Prompt kuat |
|---|---|
| "perbaiki formnya" | "Di form kontak, orang masih bisa kirim tanpa mengisi email. Seharusnya wajib isi email valid dulu sebelum bisa dikirim." |
| "bikin lebih bagus" | "Halaman harga terasa terlalu sempit di HP. Tolong beri jarak antar kartu supaya lebih enak dibaca di layar ponsel." |
| "rusak nih" | "Saat saya klik **Tambah ke keranjang**, tidak terjadi apa-apa dan keranjang tetap kosong. Seharusnya barang masuk dan jumlahnya bertambah." |
| "bikin fitur booking" | "Saya mau klien bisa booking telepon 30 menit dengan saya. Mulai dari opsi paling sederhana karena saya belum punya website." |

Beberapa kebiasaan yang membuat prompt lebih ampuh:

- **Jelaskan apa yang kamu lihat, bukan dugaan penyebabnya.** "Totalnya tertulis 12,
  harusnya 12.500" sudah cukup. Kamu tidak perlu menebak *kenapa*.
- **Satu tujuan per pesan.** Selesaikan satu hal dulu, lalu bilang "sekarang lakukan hal
  yang sama untuk halaman pendaftaran."
- **Tempel screenshot** untuk apa pun yang berkaitan dengan tampilan. Gambar lebih cepat
  daripada satu paragraf.
- **Kalau ragu, minta dia menjelaskan rencana dulu:** *"Sebelum mengubah apa pun, beri
  tahu saya rencanamu."* Setelah cocok, kamu bisa bilang "lanjut."
- **Kalimat lanjutan yang berguna:** *"Bagaimana kamu mengecek ini sudah jalan?"*,
  *"Tunjukkan apa yang kamu ubah"*, *"Batalkan itu"*, *"Jelaskan ke saya seperti saya
  bukan programmer."*

> **Templat siap-tempel:**
> *"Saya mau [tujuanmu]. Ini ada di [halaman/fitur]. Saat ini [yang terjadi]; seharusnya
> [yang kamu inginkan]. Tolong ubah dan beri tahu saya bagaimana kamu memastikan hasilnya
> sudah benar."*

---

## Apa yang seharusnya kamu terima sebagai balasan

Jawaban yang baik biasanya menjelaskan, terutama di bagian akhir:

- **apa yang diubah** (file mana, dengan bahasa sederhana),
- **apa yang dicek** untuk memastikan hasilnya berjalan, dan
- **apa yang belum bisa dipastikan**, supaya kamu tahu apa yang perlu dicoba
  sendiri.

Kamu mungkin melihat kata-kata status seperti ini. Berikut artinya untukmu:

| Kalau dia bilang | Artinya |
|---|---|
| **verified** (terverifikasi) | Dia benar-benar mengujinya dan melihatnya jalan. |
| **unverified** / **implemented but unverified** | Perubahannya sudah dibuat, tapi belum bisa diuji sepenuhnya — kamu perlu mencobanya sendiri. |
| **blocked** (terhambat) | Dia menemui sesuatu yang tidak bisa dilewati dan butuh masukan atau akses darimu. |
| **assumption** (asumsi) | Dia membuat dugaan yang masuk akal; cek ulang kalau bagian ini penting. |

Kalau kamu hanya melihat "Selesai!" tanpa keterangan apa yang dicek, tanyakan:
*"Bagaimana kamu mengecek ini sudah jalan?"* Rule ini menyuruhnya menjawab dengan jujur.

---

## Beberapa tips kecil yang berdampak besar

- **Spesifik soal tujuan, fleksibel soal cara.** "Buat form pendaftaran juga meminta nomor
  HP" lebih baik daripada "edit komponen form-nya."
- **Satu hal dalam satu waktu.** Permintaan kecil memberi hasil lebih andal daripada satu
  permintaan raksasa.
- **Kalau dia bertanya, jawab singkat saja.** Biasanya dia bertanya saat ada pilihan yang
  benar-benar penting (misalnya, "mau pelanggan bayar sekarang atau nanti?").
- **Saat ada yang salah, jelaskan yang kamu lihat**, bukan dugaan penyebabnya: "harganya
  tampil 12 padahal harusnya 12.500" itu sudah sangat membantu.
- **Biarkan dia menguji.** Kalau dia ingin menjalankan proyekmu untuk mengecek hasil
  kerjanya, itu tanda rule ini bekerja. Menjawab "ya" biasanya pilihan tepat.
- **Dia tidak akan menyentuh password atau kunci-mu.** Rule melarangnya membaca atau
  menampilkan file rahasia, jadi kamu tidak perlu khawatir isinya bocor ke dalam obrolan.

---

## Kapan sebaiknya melibatkan developer

Rule ini membuat AI lebih aman dan lebih jujur, tapi bukan sihir. Libatkan developer
sungguhan ketika:

- perubahannya menyangkut **uang, akun, atau data pribadi** dan harus benar-benar tepat,
- kamu akan **mempublikasikan / deploy** sesuatu ke pelanggan sungguhan untuk pertama
  kali, atau
- AI bilang dia **blocked** pada sesuatu yang tidak bisa dia akses (server, akun,
  perizinan).

Cara sehat memandangnya: AI ini seperti *engineer* junior yang cukup cakap dan sekarang
dipaksa untuk *menunjukkan cara kerjanya*. Itu peningkatan besar, tapi untuk perubahan
berisiko tinggi, kamu tetap butuh mata seorang senior.

---

## Kamus kecil

- **Cursor** — aplikasi tempat kamu mengetik permintaanmu; ini editor kode dengan AI di
  dalamnya.
- **Proyek / repo** — folder yang berisi file-file website atau aplikasimu.
- **Folder `.cursor`** — folder rule yang kamu salin tadi; inilah yang membuat AI
  berperilaku lebih hati-hati.
- **Terminal** — jendela teks untuk mengetik perintah komputer. Umumnya kamu **tidak**
  membutuhkannya untuk ini; AI yang menjalankan perintahnya untukmu.
- **Deploy / push** — mempublikasikan perubahanmu supaya orang lain bisa melihatnya. Layak
  ditinjau developer untuk pertama kalinya.

---

Mau versi singkat untuk developer, atau ingin melihat bagaimana semua ini diuji ke model
AI-nya? Lihat [README](../README.md) utama dan [harness](../harness/README.md).
