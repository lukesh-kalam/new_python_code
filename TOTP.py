import pyotp
totp1 = pyotp.TOTP("IBATPMF2XARJGRSJYONSN2MJCOXCR52WILFKAJWOKWZZJJ6PSWSJVKDKU725ZXBPPZLOJQSDYYSVH2VUPDDCB7V7OSPVZMVB2TOAJOI")
print("New Current OTP : ", totp1.now() )
