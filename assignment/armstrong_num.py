num = input("Enter a number: ")

if "." in num or "," in num:
   print("float blr sayı giremezsiniz..")
elif num.startswith("-"):
   print("sıfırdan küçük bir değer girdiniz.")
elif not num.isdigit():
   print("karakter dizisi giremezsiniz..")
else:

   power = len(num)
   sum = 0
   temp = int(num)
   while temp > 0:
      digit = temp % 10
      sum += digit ** power
      temp //= 10
   if int(num) == sum:
      print(num, "bir Armstrong sayısıdır..")
   else:
      print(num, "bir Armstrong sayısı değildir...")
