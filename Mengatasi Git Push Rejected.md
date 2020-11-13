### Mengatasi Git Push Rejected

![snapshoot](https://i.ibb.co/7j3j8kJ/Mengatasi-Git-Push-Rejected.jpg)


Saya ingin melakukan Push ke repository GitHub dari repository lokal saya tapi mendapatkan pesan seperti berikut: 😱

```git
To https://github.com/A2xxxxxxxx/xxxx.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/A2.xxxxx/xxxx.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
### Solusi

kita hanya cukup menambahkan parameter `--force` atau `-f` keduanya sama saja, sehingga menjadi `git push origin master --force`.


### Referensi

- `git push --help` for details.