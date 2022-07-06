print("ປີ້ເຂົ້າຊົມຫໍພິພິຕະພັນສຳລັບຄົນລາວລາຄາ 10,000 ກີບ/ຄົນ ຊື້ 10 ປີ້ຂຶ້ນໄປຫຼຸດທັນທີ 50%")
print("Museum tickets for Foreigner 20,000 kip/person. Buy 10 or more tickets, get 20% off immediately.")

while(1):
    print()
    print("*******************************************************************************************************************************")
    a = int(input("ຄົນລາວກົດ 1 Press 2 for Foreigner: \n"))

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print()

    if a == 1:
        print("***ຍິນດີຕ້ອນຮັບສູ່ຫໍພິພິຕະພັນ***")
        print()
        b = int(input("ເຈົ້າຕ້ອງການຊື້ປີ້ເຂົ້າຊົມຫໍພິພິຕະພັນຈັກໃບ: "))
        if b >= 10:
            e = (b*10000)-(b*10000)*(0.5)
            e = int(e)
            print("ລາຄາພິເສດສຳລັບປີ້ %d ໃບແມ່ນ:" %b, e, "ກີບ")
           
        else:
            print("ລາຄາປີ້ %d ໃບແມ່ນ:"%b, b*10000, "ກີບ")

    elif a == 2:
        print("***Wellcome to Musuem***")
        print()
        c = int(input("How many tickets do you want: "))
        if c >= 10:
            g = (c*20000)-(c*20000)*(0.2)
            g = int(g)
            print("special price for %d tickets :" %c, g, "KIP")
        else:
            print("total for %d tickets"%c, c*20000, "KIP")

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print()
    print("ທ່ານຕ້ອງການຊີ້ປີ້ອີກບໍ ຖ້າຕ້ອງການກົດ Yes, ບໍ່ຕ້ອງການກົດ No")
    print("Do you want to buy more Tickets: Yes or No")
    s = str(input())
    s = s.lower()
    if s == "yes":
        continue    
    elif s == "y":
        continue
    elif s == "no":
        print()
        print("Thank you for using our service")
        break   
    elif s == "n":
        print()
        print("Thank you for using our service")
        break
    else:
        print()
        print("Thank you for using our service")
        break
