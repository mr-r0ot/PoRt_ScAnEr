try:
    import os, time, socket, sys
except:
    if os.name == 'nt':
        os.system('pip install socket')
        print("\t\t Instaling...")
        time.sleep(1.5)
        os.system('cls')
    else:
        os.system('pip3 install socket')
        print("\t\t Instaling...")
        time.sleep(1.5)
        os.system('clear')
    
    import os, time, socket, sys
# ===================================================================================================


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



clear_screen()
def scan_port(ip, ranw, until):
    rang = int(ranw)
    rang_untile = int(until)
    print("\n\nIP  IS: " + ip)
    print("\n\n\n\n")
    list_open = []
    for port in range(rang , rang_untile):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            save = sock.connect_ex((ip, port))
            if save == 0:
                print("\n\t     port {}: open\n\n".format(port))
                list_open.append(port)
            if save != 0:
                print("\t port {}: close\n".format(port))   
        except:
            print("\t port {}: error".format(port))
        
        sock.close()

    if list_open != 0:
        print("\n\n\n\n\n\n\n")
        print("\t\t O P E N   P O R T S")
        for ss in list_open:
            print("\n\t port {}: open\n\n".format(ss))
    print("\n\n\n\n\n\t  my github  :  mr-r0ot")
    input("\n\t  Enter for close ")
    sys.exit()



print("\n\t       P O R T   S C A N E R")
ip = input("\n\n\t  [ Enter Ip ] $_ ")
clear_screen()
print("\n\t       Enter range")
ranw = input("\n\n\t    [ Enter range ] $_ ")
until = input("\n\n\t    [ Enter until range ] $_ ")
clear_screen()
print("\n\t       P O R T   S C A N E R")
scan_port(ip, ranw, until)
