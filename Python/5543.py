hambuger, beverage = 0, 0

up = int(input())
mid = int(input())
low = int(input())

if (up > mid):
    if (up > low): hambuger = min(mid, low)
    else: hambuger = mid
else:
    if (mid > low): hambuger = min(up, low)
    else: hambuger = up

coke = int(input())
sprite = int(input())

if (coke > sprite): beverage = sprite
else: beverage = coke

print(hambuger + beverage - 50)
