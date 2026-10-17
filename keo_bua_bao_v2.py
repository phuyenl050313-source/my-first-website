import random
diem_nguoi = 0
diem_may = 0

while (diem_nguoi < 20 and diem_may < 20):
    print("1 Kéo")
    print("2 Búa")
    print("3 Bao")
    nguoi = int(input("Chọn(1-3):"))
    may = random.randint(1,3)
    if may == 1:
        print("Kéo")
    elif may == 2:
        print("Búa")
    else:
        print("Bao")
    if nguoi == may:
        print("Hòa")
    elif(nguoi == 1 and may == 3):
        print("Bạn thắng") 
        diem_nguoi += 5
    elif(nguoi == 2 and may == 1):
        print("Bạn thắng")
        diem_nguoi += 5
    elif(nguoi == 3 and may == 2):
        print("Bạn thắng")
        diem_nguoi += 5
    else:
        print("Bạn thua")
        diem_may += 5
    print("Điểm bạn là:",diem_nguoi)
    print("Điểm máy là:",diem_may)
if diem_nguoi >= 20:
    print("Bạn là người thắng chung cuộc🎉")
else:
    print("Máy thắng chung cuộc")