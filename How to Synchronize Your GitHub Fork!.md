## How to Synchronize Your GitHub Fork

<img src="https://cdn.nearsoft.com/uploads/2019/10/syncgithubfork.jpeg" width="600" height="300"/>

Saat kita melakukan kolaborasi dalam sebuah proyek Open Source, kita biasanya diminta untuk melakukan percabangan atau `fork` dari repositori asli (selanjutnya saya singkat menjadi repo). `Fork` adalah aktivitas melakukan salinan proyek kedalam akun Github kita. Hasil salinan ini memungkinkan kita untuk bebas bereksperimen ataupun melakukan perubahan tanpa mempengaruhi repo asli / utamanya.

Saat kita melakukan percabangan `repo` `(fork)`, kita tidak akan mendapatkan update dari `repo` asli. Hal ini menyebabkan apabila repo utama memiliki `update`, `fork` `repo` pada akun Github kita tidak akan otomatis mengikuti repo aslinya. Jadi untuk menghindari masalah saat kita mencoba untuk melakukan sebuah `perubahan / commit`, lebih baik kita menjaga agar `fork` repo tetap `up to date.`

**Berikut cara membuat Fork Repositori kita agar selalu up to date.**

1. Pertama, lakukan `fork` dan `clone` repositori terlebih dahulu.
2. Kedua, masuk kedalam direktori repositori tersebut. 
3. Lihat list remote yang terdapat pada fork repo yang telah kita clone dengan perintah berikut.

```
git remote -v
```
4. Tambahkan remote asli dari repo yang kita fork dengan perintah berikut:

```
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

5. Lakukan ***fetch*** dari repo asli

```
git fetch upstream
```

6. Bila sudah, sekarang kita pindah ke `branch` `master`

```
git checkout master
```
7. Lakukan `merge` dari `upstream/master` kedalam `branch` `master`

```
git merge upstream/master
```

---
>> Sekarang perubahan yang ada pada repo asli sudah dimasukkan ke dalam` lokal branch kita`, `lakukan push` apabila kamu ingin memperbaharui` fork repo` kamu. Hal yang perlu kita ingat bahwa sebelum kita melakukan perubahan, pastikan untuk memperbarui fork repo kita. Hal ini akan menghindari kita menemui `konflik saat melakukan merge`. `Lakukan step 5 sampai 7 secara berkala` agar kita selalu mendapatkan `update terbaru` dari `repo asli`. 



### Referensi:

1. [help.github.com](https://help.github.com/en/articles/configuring-a-remote-for-a-fork)
2. [nearsoft.com](https://nearsoft.com/blog/how-to-synchronize-your-github-fork/)

