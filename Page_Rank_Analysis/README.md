[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8147189&assignment_repo_type=AssignmentRepo)
# Graded Challenge 2

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Linear Algebra dan Calculus._

---

## Dataset Description

* Pada graded challenge ini, data diakses menggunakan `bigquery-public-data` pada Google Cloud Big Query.
* Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=san_francisco_bikeshare&page=dataset&project=rock-wonder-317907) untuk langsung menuju ke dataset.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan database `san_francisco_bikeshare`.
2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `trip_id`, `start_date`, `start_station_name`, `end_station_name`, `start_station_latitude`, `start_station_longitude`, `end_station_latitude`, `end_station_longitude` pada tabel `san_francisco_bikeshare.bikeshare_trips`, dan `region_id` pada tabel `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info`.

   - Nilai `start_station_name` tidak boleh sama dengan `end_station_name`

   - Kolom `start_station_latitude`, `start_station_longitude`, `end_station_latitude`, dan `end_station_longitude` tidak boleh ada nilai `null`

   - Pilih `start_date` dengan rentang tanggal lahir kamu di tahun 2017 sampai 5 bulan berikutnya. **Contoh: kamu lahir di tanggal 14 Februari maka rentang start_date dari 2017-02-14 sampai 2017-07-14**.
3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P0GC2_Set_1_<nama-students>.csv`.
4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!
5. Tampilkan `head` dan `tail` dari dataset pada notebook!


## Assignment Problems

### Problem 1
Kamu adalah seorang data scientist di San Francisco Smart City. Kamu sedang mengerjakan proyek untuk menganalisa dan mengoptimasi sistem pesepedaan. Tugas pertamamu, kamu harus mencari stasiun awal mana yang paling favorit di antara stasiun-stasiun lainnya dengan menghitung **PageRank** menggunakan *Eigendecomposition*.

Dalam mencapai tujuan ini, ikuti langkah-langkah berikut:

1. Buatlah dua variable baru yang bernama `start_stations` dan `end_stations` yang masing-masing berisikan list nama stasiun awal dan stasiun akhir. `Pastikan tidak ada nama stasiun yang duplikat di masing-masing variable`.
2. Deteksi stasiun-stasiun yang hanya terdapat di salah satu variable dan tidak di keduanya (exclusive-or/xor) menggunakan `np.setxor1d(array1,array2)`. Outputnya akan berupa numpy array dan masukkan output tersebut ke dalam variable bernama `exclusive_stations`. Agar mudah membayangkan, ilustrasi xor dapat dilihat pada [gambar ini](https://www.mathworks.com/help/examples/map/win64/SetOperationsOnTwoOverlappingCircularRegionsExample_01.png).
3. Buat dataframe yang berisikan cross-tabulation antara `start_stations` dan `end_stations` menggunakan `pd.crosstab(pd.Series1,pd.Series2)`. Hasil dari langkah ini akan menghasilkan dataframe yang menginfokan berapa jumlah/frekuensi perjalanan dari start station tertentu ke end station tertentu. Hasil dari langkah ini dimasukkan ke dalam variable bernama `df_matrix`. Ilustrasi cross-tabulation dapat dilihat pada link [berikut](http://www.dartistics.com/cross-tab-w-chi-square_files/figure-html/cross-tab-1.png).
4. Buatlah salinan dari data yang di-load ke dalam variable bernama `df_copy`.
5. Filter `df_copy` dimana tidak ada `start_station_name` dan `end_station_name` yang termasuk dalam list `exclusive_stations`.
6. Lakukan **langkah 3** untuk variable `df_copy` dan simpan ke dalam variable bernama `df_matrix_square`. **Pastikan jumlah rows dan columns sama, kalau tidak ulangi dari langkah 4**.
7. Jumlahkan nilai kolom masing-masing rows pada `df_matrix_square` menggunakan method `sum(axis=1)` dan simpan ke dalam variable bernama `total_trips`.
8. Bagi setiap kolom `df_matrix_square` dengan menggunakan method `.div()`, dengan inputan parameter `total_trips` dan `axis='rows'`. Masukkan hasilnya ke variable `weighted_matrix_df`.
9. Konversikan `weighted_matrix_df` ke `numpy array`.
10. Hitung `eigen value` dan `eigen vector`menggunakan library `numpy`.
11. Score `PageRank` terdapat pada `eigen vector` yang `eigen value`nya paling tinggi. Simpan eigen vector tersebut ke dalam variable bernama `PR_Scores`.
12. Buat dataframe baru bernama `PageRank_df` dengan kolom 'start_station' yang berisikan value variable `start_stations` dan kolom `score` yang berisikan value variable `PR_Scores`.
13. Tampilkan `head` dari dataframe `PageRank_df`!

**Jawab Pertanyaan Berikut:**

a. Mengapa dalam kasus ini kita menerapkan konsep *Eigendecomposition*?

b. Dari pengamatanmu, mengapa pada akhirnya kita menggunakan dataframe `df_matrix_square` dibandingkan `df_matrix` untuk dilakukan proses *Eigendecomposition*? Berikan alasan yang logis sesuai dengan konsep *Eigendecomposition*.

c. Jika dilihat dari PageRanknya, dimana nilai PageRank paling besar merupakan stasiun yang paling favorit. Apa insight yang akan kamu berikan?

******

### Problem 2
Masih dengan proyek yang sama, menggunakan integral, hitung luas area lingkup stasiun awal sepeda di kota San Francisco. Ikuti langkah berikut:

1. Buat variable baru bernama `df_coor_stations` yang berisikan data yang sudah di-load dimana kolom `region_id = 3`. Pastikan tidak ada data yang duplikat dan hanya menyertakan kolom `start_station_name`,`start_station_latitude`, dan `start_station_longitude`. Urutkan pula dataframe tersebut berdasarkan `start_station_longitude` dari nilai terkecil hingga terbesar.
2. Plot grafik area stasiun-stasiun di San Fransisco menggunakan method `.plot()`. **Catatan**: Gunakan arahan berikut dalam penggunaan method `.plot()`, `.plot(x='nama kolom untuk sumbu x',y='nama kolom untuk sumbu y',figsize=(20,8))`. *Longitude merupakan sumbu x dan Latitude merupakan sumbu y*.
3. Hitung luas area yang dilingkup stasiun awal menggunakan library `Scipy`. Hasilnya bersatuan square degree.

**Jawab Pertanyaan Berikut:**

a. Terdapat 2 jenis integral yaitu definite dan indefinite. Jenis integral apa yang kamu gunakan untuk kasus ini? Berikan alasanmu!

b. Terdapat dua metode dalam perhitungan integral yaitu simbolik dan numerik. Mana yang kamu gunakan untuk kasus ini dan mengapa?

c. Apakah diperlukan mendefinisikan fungsi matematis ( seperti `f(x) = x^2+2` ) pada kasus ini? Berikan penjelasan dan alasanmu!


## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P0W2_<nama-student>.ipynb`, misal `h8dsft_P0W2_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke akun Github masing-masing student.

## Assignment Objectives

*Graded Challenge 2* ini dibuat guna mengevaluasi Linear Algebra dan Calculus sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu melakukan pemrosesan data sebelum melakukan perhitungan
- Mampu menerapkan konsep kalkulus dan linear algebra pada suatu permasalahan
- Mampu memahami konsep kalkulus dan linear algebra

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Data Retrieve | Mampu memperoleh data menggunakan SQL BigQuery, melingkupi kesesuaian kode dengan tabel yang dihasilkan | 5 pts |
| Data Preprocessing | Mampu memroses data sampai siap digunakan dalam perhitungan linear algebra (4 pts) dan Kalkulus (3 pts) | 7 pts |
| Linear Algebra Implementation | Mampu menerapkan perhitungan Eigendecomposition kode | 3 pts |
| Calculus Implementation | Mampu menerapkan perhitungan Integral dengan kode | 3 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Linear Algebra | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Problem 1 (5 each number) | 15 pts |
| Calculus | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Problem 2 (5 each number) | 15 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan menggunakan Markdown untuk penjelasan kode. | 12 pts |

---

```
Total Points : 60
```

---

## Score Reduction

Pengurangan poin akan diberlakukan jika Student terlambat mengumpulkan tugas yang telah diberikan. Adapun besarnya pengurangan adalah :

| Criteria | Max Points GC2 |
| --- | --- |
| Keterlambatan kurang dari 1 jam setelah deadline | 45 pts (75 %) |
| Keterlambatan lebih dari 1 jam - 1 hari setelah deadline | 30 pts (50 %) |
| Keterlambatan lebih dari 1 hari setelah deadline | 0 pts (0 %) |
