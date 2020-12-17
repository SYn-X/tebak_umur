x = int(input('pilih 1 angka 1 - 9: '))
lahir = int(input('masukan tahun lahirmu: '))

def go_main():
  a = x * 2
  hasil_a = (a)
  b = hasil_a + 5
  hasil_b = (b)
  c = hasil_b * 50 
  hasil_c = (c)
  d = hasil_c + 1770
  hasil_akhir = (d)
  hasil = hasil_akhir - lahir
  print("nah digit pertama adalah angka yang kamu pilih, yaitu:",x,"lalu 2 digit terakhir adalah umurmu",hasil)  

if x == 1:
  go_main()
elif x == 2:
  go_main()
elif x == 3:
  go_main()
elif x == 4:
  go_main()
elif x == 5:
  go_main()
elif x == 6:
  go_main()
elif x == 7:
  go_main()
elif x == 8:
  go_main()
elif x == 9:
  go_main()
elif x < 9:
  print('angka salah coba lagi')

  
  
  
  
  
  
  
  
