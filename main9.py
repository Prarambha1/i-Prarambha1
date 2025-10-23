# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := place sign in frontmost position
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12000.45

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:,.2f}")
print(f"Price 3 is {price3:+,.2f}")

print(f"Price 1 is {price1:<10.2f}")
print(f"Price 2 is {price2:>10.2f}")
print(f"Price 3 is {price3:^10.2f}")