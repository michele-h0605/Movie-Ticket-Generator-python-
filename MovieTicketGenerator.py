#Print available showtimes
print("Available movies today:")
print("A)12 Strong:    1)2:30  2)4:40  3)7:50  4)10:50")
print("B)Coco:         1)12:40 2)3:45")
print("C)The Post:     1)12:45 2)3:35  3)7:05  4)9:55")

#Prompt User
choice = input("Movie choice:   ")
#Choice A
if choice == "A":
    showtime = int(input("Showtime:       "))
    #Showtimes
    if showtime == 1:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30 and showtime > 2:
            print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
        elif adult_tix + kid_tix <= 30 and showtime < 2:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 5:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30 and showtime > 2:
            print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
        elif adult_tix + kid_tix <= 30 and showtime < 2:
            print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 8:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30 and showtime > 2:
            print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
        elif adult_tix + kid_tix <= 30 and showtime < 2:
            print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 11:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
#Choice B
elif choice == "B":
    showtime = int(input("Showtime:       "))
    #Showtimes
    if showtime == 2:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime >= 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 4:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
#Choice C
elif choice == "C":
    showtime = int(input("Showtime:       "))
    #Showtimes
    if showtime == 1:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 4:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 7:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    elif showtime == 10:
        #Adult + Child Tickets
        adult_tix = float(input("Adult tickets:  "))
        kid_tix = float(input("Kid tickets:    "))
        if adult_tix + kid_tix <= 30:
            if showtime > 2:
                print(f'Total cost:     ${round(adult_tix * 12.45 + kid_tix * 9.68, 2)}')
            else:
                print(f'Total cost:     ${round(adult_tix * 11.17 + kid_tix * 8, 2)}')
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")