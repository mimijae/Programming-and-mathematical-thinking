# 2000
# 7500

coffee_dic = {'아메리카노':2000, '카페라떼':4000, '에스프레소':1500}
price_1 = coffee_dic['아메리카노']
print(price_1)

total_price = 0
for price in coffee_dic.values():
    total_price += price
    
print(total_price)