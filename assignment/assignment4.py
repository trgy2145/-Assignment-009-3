sayı = int(input("Please enter you number :"))
asalmi = True
if sayı <= 1:
    asalmi = False
for i in range (2, sayı):
    if (sayı % i == 0) :
        asalmi = False
        break
if asalmi:
    print("girilen sayı asaldır..")
else :
    print("sayı asal değildir...")

