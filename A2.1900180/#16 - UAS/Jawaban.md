class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan. Ini berisi data serta metode yang digunakan untuk memproses data tersebut.
Instance adalah salinan class dengan nilai sebenarnya , secara harfiah merupakan objek class tertentu.
Sementara class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut.
class PythonclassName:
CamelCase notasi, dimulai dengan huruf kapital — yaitu, PythonclassName()
Anda menggunakan nama class, diikuti dengan tanda kurung. Jadi jika nama classnya Dog(), contoh Dognya adalah - my_class = Dog().
Dengan notasi titik — misalnya, instance_name.attribute_name
Sebuah fungsi yang didefinisikan di dalam class.
Argumen pertama dari setiap metode merujuk pada instance class saat ini, yang menurut konvensi, diberi nama self. Dalam __init__metode ini, selfmengacu pada objek yang baru dibuat; sementara dalam metode lain, selfmengacu pada contoh yang metode namanya disebut. Untuk lebih lanjut tentang __init__vs self, lihat artikel ini .
__init__Metode menginisialisasi sebuah instance dari class.