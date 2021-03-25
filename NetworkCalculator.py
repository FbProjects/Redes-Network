while True:
    import os
    os.system("cls" if os.name == 'nt' else 'clear')

    def print1():
        print("\t----------------------------------------")
        print("\t|||                                  |||")
        print("\t||| Network Calculator, By: LeagueBR |||")
        print("\t|||                                  |||")
        print("\t----------------------------------------\n")
    print1()
    # -----------------------------------------------
    vRede1 = input("1º Network octet: ")
    if int(vRede1) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vRede1 = input("\n1º Network octet: ")
        if int(vRede1) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vRede2 = input("2nd Network octet: ")
    if int(vRede2) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vRede2 = input("\n2nd Network octet: ")
        if int(vRede2) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vRede3 = input("3rd Network octet: ")
    if int(vRede3) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vRede3 = input("\n3rd Network octet: ")
        if int(vRede3) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vRede4 = input("4th Network octet: ")
    if int(vRede4) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vRede4 = input("\n4th Network octet: ")
        if int(vRede4) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # -------------------- MASK ----------------------
    vMask1 = input("\n\n\n1st mask octet: ")
    if int(vMask1) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vMask1 = input("\n1st mask octet: ")
        if int(vMask1) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vMask2 = input("2nd mask octet: ")
    if int(vMask2) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vMask2 = input("\n2nd mask octet: ")
        if int(vMask2) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vMask3 = input("3rd mask octet: ")
    if int(vMask3) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vMask3 = input("\n3rd mask octet: ")
        if int(vMask3) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    vMask4 = input("4th mask octet: ")
    if int(vMask4) >= 256:
        print("Type a valid number! (Between 0 e 255)")
        vMask4 = input("\n4th mask octet: ")
        if int(vMask4) <= 255:
            pass
        else:
            print("Type a valid number (Between 0 e 255), closing...")
            os.system("pause")
            exit()
    else:
        pass
    # ------------------------------------------------
    endIP = vRede1+"."+vRede2+"."+vRede3+"."+vRede4     # 192.168.0.1
    endMask = vMask1+"."+vMask2+"."+vMask3+"."+vMask4   # 255.255.255.0
    # ------------------------------------------------
    # n1R = 1st octet IP solved.
    # FAZER IF ELSE DE MASK == 0: EXIT()
    # -------------- SEGUNDO OCTETO --------------------
    if int(vMask2) == 255:
        broad2 = vRede2
        last2 = vRede2
        host2 = vRede2
        rede2 = vRede2
    else:
        sub2 = 256 - int(vMask2)  # 16
        calc2 = int(sub2)  # 16
        while int(sub2) <= int(vRede2):
            sub2 = int(sub2) + calc2
        broad2 = int(sub2) - 1
        last2 = int(broad2)
        host2 = int(broad2) - int(calc2) + 1
        rede2 = int(broad2) - int(calc2) + 1
    # print()
    # -------------- TERCEIRO OCTETO --------------------
    if int(vMask3) == 255:
        broad3 = vRede3
        last3 = vRede3
        host3 = vRede3
        rede3 = vRede3
    else:
        sub3 = 256 - int(vMask3)
        calc3 = int(sub3)
        while int(sub3) <= int(vRede3):
            sub3 = int(sub3) + calc3
        broad3 = int(sub3) - 1  # 15
        last3 = int(broad3)  # 15
        host3 = int(broad3) - int(calc3) + 1
        rede3 = int(broad3) - int(calc3) + 1
    # -------------- QUARTO OCTETO --------------------
    if int(vMask4) == 0:
        broad4 = 255
        last4 = 254
        host4 = 1
        rede4 = 0
    else:
        sub4 = 256 - int(vMask4)  # 256 - 248
        calc4 = int(sub4)  # 8
        while int(sub4) <= int(vRede4):  # while 8 <= 180
            sub4 = int(sub4) + calc4  # sub4 = 16 + 16
        broad4 = int(sub4) - 1  # 184 - 1 (183)
        last4 = int(broad4) - 1  # 182
        rede4 = int(broad4) - int(calc4) + 1  # 176
        host4 = int(rede4) + 1
    # -------------------------------------------------

    # N1 = REDE, N2 = 1ST HOST, N3 = LAST HOST, N4 = BROADCAST.
    os.system("cls" if os.name == 'nt' else 'clear')
    print1()
    print("\n>>> Network address  : {}.{}.{}.{}".format(vRede1, rede2, rede3, rede4))
    print(">>> 1st Host address : {}.{}.{}.{}".format(vRede1, host2, host3, host4))
    print(">>> Last Host address: {}.{}.{}.{}".format(vRede1, last2, last3, last4))
    print(">>> Broadcast address: {}.{}.{}.{}\n".format(vRede1, broad2, broad3, broad4))

    os.system("pause")

