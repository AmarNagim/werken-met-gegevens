# berekening feestlunch
# info: Je wilt 17 croissantjes van elk 39 eurocent en 2 stokbroden van elk 2,78 euro kopen. 
# je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen? Laat Python dat uitrekenen.


croissant_amount = 17          # croissant
single_croissant_price = 0.39
stokbrood_amount = 2           # stokbrood
single_stokbrood_price = 2.78
coupon_amount = 3              # kortingsbon
single_coupon_price = 0.50

price_croissant = croissant_amount*single_croissant_price       
price_stokbrood = stokbrood_amount*single_stokbrood_price
price_coupon = coupon_amount*single_coupon_price
price_after_coupon = price_croissant + price_stokbrood - price_coupon

price = print(f"De prijs van de feestlunch is €{price_after_coupon},-")

print(price)                   # prijs
