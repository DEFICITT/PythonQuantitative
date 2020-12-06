#
# a = 12.9566
# c = round(a, 2)
# print(c)

hello = 'hello world'
# print(hello[0])
# print(hello * 3)

# a = hello.split(' ')
# print(a)
#
# for value in a:
#     print(value)

# a = hello.upper()
# print(a)

symbol1 = "BTC/USDT"
symbol2 = "btc_usdt"
symbol3 = symbol2.upper()

symbol4 = symbol3.replace('_', '/')
print(symbol1 == symbol4)
