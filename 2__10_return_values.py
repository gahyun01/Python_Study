def tax_cal(money):
  # print(money * 0.35)
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

# to_pay = tax_cal(150000000)
# pay_tax(to_pay)
pay_tax(tax_cal(150000000))
