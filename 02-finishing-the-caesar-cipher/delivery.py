
#Part 3 Lab
#Problem

price: int = 1500
if price > 1000:
 price -= 100
print(price)

price: int = 499
if price >= 500:
 band: str = "high"
else:
 band = "low"
print(band)
print()


#Delivery Day Drill
DAYS_IN_WEEK :int =7

day:int = int(input("Day:"))   # 1 - 7 days
days_to_wait:int = int(input("Days to Wait:" ))   #days_to_wait   # 0 -7 days

delivery_day = day + days_to_wait

#print(delivery_day)

if delivery_day > DAYS_IN_WEEK :
   Delivery_Day:int = delivery_day - DAYS_IN_WEEK
   print("Delivery Day:", Delivery_Day)

else:
   print("delivery_day:", delivery_day)

#delivery_day is from 1 to DAYS_IN_WEEK  
assert 1 <= Delivery_Day <= DAYS_IN_WEEK

print()




item_code: str = "TEA-250G"
letters: int = 0

for character in item_code:
 if "A" < character < "Z":
  letters += 1
print("Letters:", letters)