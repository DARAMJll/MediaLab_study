import random

rint = random.randint(1, 20)
count = 4
try_ = 0

input_number = int(input(f"기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요 : "))
try_ += 1

while rint != input_number: 

    if input_number < rint:
        print("Up")
        count -= 1
        input_number = int(input(f"기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요 : "))
        try_ += 1
        if count == 1: break
        if rint == input_number: break
    
    if input_number > rint:
        print("Down")
        count -= 1
        input_number = int(input(f"기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요 : "))
        try_ += 1
        if count == 1: break
        if rint == input_number: break
    
    
if rint == input_number:
    print(f"축하합니다. {try_}번 만에 숫자를 맞히셨습니다.")
if count == 0:
    print(f"아쉽습니다. 정답은 {rint}입니다.")
