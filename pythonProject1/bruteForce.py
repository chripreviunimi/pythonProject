def bruteforce(password):
    lun = len(password)  # per sapere quale ciclo for applicare

    pin = 0
    chiave = False
    conta = 0
    # start_time = time.time()  # lo devo mettere dopo l'input o calcola anche il tempo nel quale io inserisco la cifra
    if lun == 1:
        # 1 cifra
        while not chiave:
            for i in range(10):
                if not chiave:
                    pin = i
                    conta = conta + 1
                    print("Contaaaaa: " + str(conta))
                    print(pin)
                    if pin == int(password):
                        chiave = True
            break

    elif lun == 2:
        # 2 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    if (chiave == False):
                        pin = str(i) + str(j)
                        conta = conta + 1
                        print("Contaaaaa: " + str(conta))
                        print(pin)
                        if int(pin) == int(password):
                            chiave = True
            break

    elif lun == 3:
        # 3 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    for z in range(10):
                        if (chiave == False):
                            pin = str(i) + str(j) + str(z)
                            conta = conta + 1
                            print("Contaaaaa: " + str(conta))
                            print(pin)
                            if int(pin) == int(password):
                                chiave = True
            break

    elif lun == 4:
        # 4 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    for z in range(10):
                        for a in range(10):
                            if (chiave == False):
                                pin = str(i) + str(j) + str(z) + str(a)
                                conta = conta + 1
                                print("Contaaaaa: " + str(conta))
                                print(pin)
                                if int(pin) == int(password):
                                    chiave = True
            break

    elif lun == 5:
        # 5 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    for z in range(10):
                        for a in range(10):
                            for b in range(10):
                                if (chiave == False):
                                    pin = str(i) + str(j) + str(z) + str(a) + str(b)
                                    conta = conta + 1
                                    print("Contaaaaa: " + str(conta))
                                    print(pin)
                                    if int(pin) == int(password):
                                        chiave = True
            break

    elif lun == 6:
        # 6 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    for z in range(10):
                        for a in range(10):
                            for b in range(10):
                                for c in range(10):
                                    if (chiave == False):
                                        pin = str(i) + str(j) + str(z) + str(a) + str(b) + str(c)
                                        conta = conta + 1
                                        print("Contaaaaa: " + str(conta))
                                        print(pin)
                                        if int(pin) == int(password):
                                            chiave = True
            break

    elif lun == 7:
        # 7 cifre
        while chiave == False:
            for i in range(10):
                for j in range(10):
                    for z in range(10):
                        for a in range(10):
                            for b in range(10):
                                for c in range(10):
                                    for d in range(10):
                                        if (chiave == False):
                                            pin = str(i) + str(j) + str(z) + str(a) + str(b) + str(c) + str(d)
                                            conta = conta + 1
                                            print("Contaaaaa: " + str(conta))
                                            print(pin)
                                            if int(pin) == int(password):
                                                chiave = True
            break
    else:
        print("Password troppo lunga per essere decifrata in un tempo accettabile con un bruteforce di questa portata")

    return pin
