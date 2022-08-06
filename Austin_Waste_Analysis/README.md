_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Statistics._

---

## Dataset Description

* Pada graded challenge ini, data diakses menggunakan `bigquery-public-data` pada Google Cloud Big Query.
* Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=austin_waste&t=waste_and_diversion&page=table) untuk langsung menuju ke tabel.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan tabel `waste_and_diversion` pada dataset `austin_waste`.
2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `load_time`, `load_type`, `load_weight`, `dropoff_site`.

   - Ambil jumlah data maksimal 150.000 data.

3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P0GC3_<nama-students>.csv`.
4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!
5. Tampilkan `head` dan `tail` dari dataset pada notebook!


## Assignment Problems

Kamu adalah anggota tim Data Science di Austin Smart City dan sedang mengerjakan projek analisa sistem pembuangan dan pengelolaan sampah di kota tersebut. Sebagai anggota tim, berdasarkan data yang tersedia, coba analisa data tersebut menggunakan statistik deskriptif dan inferensial, serta berikan insight kepada pemerintah kota Austin mengenai kondisi sistem pembuangan dan pengelolaan sampah. Gunakan guideline/langkah berikut untuk mempermudah kamu dalam menganalisa.

1. Sebelum melakukan perhitungan dan analisa statistik, lakukan pembersihan data terlebih dahulu. Pastikan tidak ada missing value, dsb.

2. Selanjutnya, lakukan eksplorasi data sederhana guna mengetahui dan mengenali data yang kamu punya. Kamu bisa lakukan hal-hal berikut untuk mengeksplorasi data kamu.
  - Melihat rentang waktu pengambilan data
  - Ada apa saja tipe load sampah di kota Austin berdasarkan data
  - Mengetahui tempat pembuangan sampah ada dimana saja
  - dsb.

3. Berdasarkan central tendency (mean, median, dan modus) untuk masing-masing site, insight/informasi apa yang bisa kamu sampaikan kepada pemerintah kota? (**Caution:** Jangan gunakan pd.DataFrame.describe())

4. Pilih site yang paling menarik perhatian kamu, dan berikan alasannya.

5. Gunakan site yang kamu pilih untuk dicek apakah data `load_weight` ada outlier atau tidak. *Gunakan teknik yang tepat sesuai dengan distribusi dari datanya!*. Jika iya, berapa persen jumlah outliernya? dan bandingkan central tendency data yang telah dikeluarkan outliernya dengan yang belum (hasil dari perhitungan nomor 3).

6. Gunakan site yang telah kamu pilih untuk dihitung range, variance, dan standar deviasi untuk data `load_weight`. Berikan insight dari hasil perhitunganmu kepada pemerintah kota (`Pastikan data yang digunakan adalah data yang sudah dibersihkan dari outlier`).

7. Pemerintah kota berencana menambah site baru. Berikan analisa dan saran terkait berapa kapasitas penampungan di site baru berdasarkan perhitungan `confidence interval`. Data apa yang kamu gunakan, apakah hanya dari satu site saja atau dari keseluruhan site?

8. Buatlah `analisa uji hipotesis` dari data tersebut dari data yang tersedia (kasusnya dibebaskan). Definisikan H0 dan H1 nya serta lakukan perhitungan menggunakan t-test yang sesuai dengan hipotesis kamu. Tulis kesimpulan dari hasil perhitunganmu kepada pemerintah kota (**Ingat!** pemerintah kota tidak mengerti p-value, hipotesis diterima/tidak diterima).

9. Tarik benang merah dan kesimpulan dari perhitungan dan analisa yang kamu telah lakukan di langkah-langkah sebelumnya. Ceritakan kesimpulanmu kepada pemerintah kota dan **hindari** bahasa teknis yang tidak dimengerti oleh orang yang bukan data scientist!


**Jawab pertanyaan berikut untuk mengasah pemahaman konsepmu!**

1. Apa perbedaan statistik deskriptif dan inferensial?
2. Metrik pada central tendency apa yang tepat digunakan untuk menyimpulkan data yang terdistribusi normal dan tidak? Apakah sama atau berbeda?
3. Teknik apa yang kamu pilih untuk handling outlier? jelaskan alasannya!
4. Apa konsep dibalik central tendency sehingga kita dapat menggunakannya untuk menyelesaikan langkah pada nomor 7?
5. Jelaskan jenis uji hipotesis apa yang kamu terapkan dan mengapa?


## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P0W3_<nama-student>.ipynb`, misal `h8dsft_P0W3_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke akun Github masing-masing student.

## Assignment Objectives

*Graded Challenge 3* ini dibuat guna mengevaluasi Statistics Descriptive dan Inferential sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu melakukan pemrosesan data sebelum melakukan perhitungan
- Mampu menerapkan konsep statistics descriptive dan inferential pada suatu permasalahan
- Mampu memahami konsep statistics descriptive dan inferential

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Data Retrieve | Mampu memperoleh data menggunakan SQL BigQuery, melingkupi kesesuaian kode dengan tabel yang dihasilkan | 5 pts |
| Data Preprocessing | Mampu memroses data sampai siap digunakan dalam perhitungan | 4 pts |
| Data Exploratory | Mampu melakukan eksplorasi data sederhana | 4 pts |
| Central Tendency | Mampu menerapkan perhitungan mean, median, modus di kode (2 pts each). `Jika menggunakan .describe(), tidak akan mendapat nilai` | 6 pts |
| Outlier Handling | Mampu menerapkan pendeteksian dan handling outlier di kode | 3 pts |
| Measure of Variance | Mampu menerapkan perhitungan range, variance, dan standar deviasi di kode (2 pts each) | 6 pts |
| Confidence Interval | Mampu menerapkan perhitungan confidence interval pada kode | 3 pts |
| Hypothesis Testing | Mampu mendefinisikan H0 dan H1 serta menerapkan perhitungan uji hipotesis di kode| 4 pts |


### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Statistics | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada (5 each) | 25 pts |


### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Central Tendency | Mampu memberikan kesimpulan/insight dari hasil perhitungan central tendency | 5 pts |
| Outlier Analysis | Mampu memberikan kesimpulan/insight dari hasil pendeteksian/handling outlier | 5 pts |
| Variance | Mampu memberikan kesimpulan/insight dari hasil perhitungan range, variance, dan standar deviasi | 5 pts |
| Confidence Interval | Mampu memberikan kesimpulan/insight/saran dari hasil perhitungan confidence interval | 5 pts |
| Hypothesis Testing | Mampu memberikan kesimpulan/insight/saran dari hasil perhitungan hypothesis testing | 5 pts |
| Overall Analysis | Mampu menarik kesimpulan dari seluruh perhitungan dan analisa yang dilakukan serta menggunakan bahasa yang dipahami orang awam| 10 pts |


### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan menggunakan Markdown untuk penjelasan kode. | 5 pts |

---

```
Total Points : 100
```

## Score Reduction

Pengurangan poin akan diberlakukan jika Student terlambat mengumpulkan tugas yang telah diberikan. Adapun besarnya pengurangan adalah :

| Criteria | Max Points GC2 |
| --- | --- |
| Keterlambatan kurang dari 1 jam setelah deadline | 75 pts (75 %) |
| Keterlambatan lebih dari 1 jam - 1 hari setelah deadline | 50 pts (50 %) |
| Keterlambatan lebih dari 1 hari setelah deadline | 0 pts (0 %) |
