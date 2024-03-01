from datetime import datetime



datainicial = datafinal = data = email = senha = email1 = senha1 = email2 = senha2 = 0
print("""\n-=-=-=-=-=-=-=-=-=-=-= EVENTOS EM NATAL -=-=-=-=-=-=-=-=-=-=-=-=
            faça seu cadastro aqui mesmo:
            [ 1 ] GGcon games e cosplay
            [ 2 ] djavan teatro riachuelo
            [ 3 ] thiago ventura teatro riachuelo
            [ 4 ] orquestra petrobras sinfonica
            [ 5 ] sair do programa""")
user = int(input("\nquais desses eventos voce quer participar ?"))
if user == 1 :
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("esse evento ocorrerá dia 5 de novembro")
    user = str(input("\ndeseja efetuar seu cadastro ? [S/N]: ")).strip().upper()[0]
    while user not in "SN":
        user = str(input("por favor digite S ou N:")).strip().upper()[0]
    if user == "S":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\ninsira seu email e senha")
        email = str(input("\nemail:")).strip()
        senha = str(input("senha:")).strip()
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("confirme seu email e senha")
        email1 = str(input("\nemail:")).strip()
        senha1 = str(input("senha:")).strip()
        while email1 not in email or senha1 not in senha:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("\nemail ou senha incorretos, por favor insira novamente")
            email1 = str(input("\nemail:")).strip()
            senha1 = str(input("senha:")).strip()
        if email1 == email and senha1 == senha:
            datainicial = datetime(2024, 2, 1)
            datafinal = datetime(2024, 11, 5)
            data = datafinal - datainicial
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\nseu email foi cadastrado com sucesso")
            print(f"\nfaltam {data}")
            print("\naproveite ;)")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user == 'N':
        print("\nokay ! programa encerrado...")
if user == 2:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("esse evento ocorrerá dia 21 de março")
    user = str(input("\ndeseja efetuar seu cadastro ? [S/N]: ")).strip().upper()[0]
    while user not in "SN":
        user = str(input("por favor digite S ou N:")).strip().upper()[0]
    if user == "S":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\ninsira seu email e senha")
        email = str(input("\nemail:")).strip()
        senha = str(input("senha:")).strip()
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("confirme seu email e senha")
        email1 = str(input("\nemail:")).strip()
        senha1 = str(input("senha:")).strip()
        while email1 not in email or senha1 not in senha:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("\nemail ou senha incorretos, por favor insira novamente")
            email1 = str(input("\nemail:")).strip()
            senha1 = str(input("senha:")).strip()
        if email1 == email and senha1 == senha:
            datainicial = datetime(2024, 2, 1)
            datafinal = datetime(2024, 3, 21)
            data = datafinal - datainicial
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\nseu email foi cadastrado com sucesso")
            print(f"\nfaltam {data}")
            print("\naproveite ;)")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user == 'N':
        print("\nokay programa encerrado")
if user == 3:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("esse evento ocorrerá dia 18 de maio")
    user = str(input("\ndeseja efetuar seu cadastro ? [S/N]: ")).strip().upper()[0]
    while user not in "SN":
        user = str(input("por favor digite S ou N:")).strip().upper()[0]
    if user == "S":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\ninsira seu email e senha")
        email = str(input("\nemail:")).strip()
        senha = str(input("senha:")).strip()
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("confirme seu email e senha")
        email1 = str(input("\nemail:")).strip()
        senha1 = str(input("senha:")).strip()
        while email1 not in email or senha1 not in senha:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("\nemail ou senha incorretos, por favor insira novamente")
            email1 = str(input("\nemail:")).strip()
            senha1 = str(input("senha:")).strip()
        if email1 == email and senha1 == senha:
            datainicial = datetime(2024, 2, 1)
            datafinal = datetime(2024, 5, 18)
            data = datafinal - datainicial
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\nseu email foi cadastrado com sucesso")
            print(f"\nfaltam {data}")
            print("\naproveite ;)")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user == 'N':
        print("\nokay programa encerrado")
if user == 4:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("esse evento ocorrerá dia 5 de maio")
    user = str(input("\ndeseja efetuar seu cadastro ? [S/N]: ")).strip().upper()[0]
    while user not in "SN":
        user = str(input("por favor digite S ou N:")).strip().upper()[0]
    if user == "S":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\ninsira seu email e senha")
        email = str(input("\nemail:")).strip()
        senha = str(input("senha:")).strip()
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("confirme seu email e senha")
        email1 = str(input("\nemail:")).strip()
        senha1 = str(input("senha:")).strip()
        while email1 not in email or senha1 not in senha:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("\nemail ou senha incorretos, por favor insira novamente")
            email1 = str(input("\nemail:")).strip()
            senha1 = str(input("senha:")).strip()
        if email1 == email and senha1 == senha:
            datainicial = datetime(2024, 2, 1)
            datafinal = datetime(2024, 5, 5)
            data = datafinal - datainicial
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\nseu email foi cadastrado com sucesso")
            print(f"\nfaltam {data}")
            print("\naproveite ;)")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user == 'N':
        print("\nokay programa encerrado")
if user == 5:
    print("okay, programa encerrado")




            

        




    