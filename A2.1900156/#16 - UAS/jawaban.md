### 1. class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan. Ini berisi data serta metode yang digunakan untuk memproses data tersebut.
### 2. Apa itu instance?
### Instance adalah salinan class dengan nilai sebenarnya , secara harfiah merupakan objek class tertentu.
## 3. Apa hubungan antara class dan instance?
### Sementara class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut.
## 4. Apa sintaks Python yang digunakan untuk menentukan class baru?
class PythonclassName:
## 5. Apa konvensi ejaan untuk nama class?
### CamelCase notasi, dimulai dengan huruf kapital — yaitu
PythonclassName()
## 6. Bagaimana Anda memberi instantiate, atau membuat instance dari, sebuah class?
### Anda menggunakan nama class, diikuti dengan tanda kurung. Jadi jika nama classnya Dog(), contoh Dognya adalah - my_class = Dog().
## 7. Bagaimana Anda mengakses atribut dan perilaku instance class?
### Dengan notasi titik — misalnya, instance_name.attribute_name
## 8. Apa itu metode?
### Sebuah fungsi yang didefinisikan di dalam class.
## 9. Apa tujuannya self?
### Argumen pertama dari setiap metode merujuk pada instance class saat ini, yang menurut konvensi, diberi nama self. Dalam __init__metode ini, selfmengacu pada objek yang baru dibuat; sementara dalam metode lain, selfmengacu pada contoh yang metode namanya disebut.
## 10. Apa tujuan dari __init__metode ini?
### __init__Metode menginisialisasi sebuah instance dari class.