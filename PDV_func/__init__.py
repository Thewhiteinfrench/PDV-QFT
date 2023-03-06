diccedulas = {'R$100,00': 100, 'R$50,00': 50, 'R$20,00': 20, 'R$10,00': 10, 'R$5,00': 5, 'R$2,00': 2,
              'R$1,00': 1, 'R$0,50': 0.5, 'R$0,25': 0.25, 'R$0,10': 0.1, 'R$0,05': 0.05}


def busca(cb, produtos):
    for c in produtos:
        if cb == c["Cb"]:
            return c


def cad():
    pass


def troco(compra, pago):
    quant = [[]]
    acm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    troco = pago - compra
    print(f'''O troco foi de R${str(f'{troco:.2f}').replace('.', ',')}''')
    for i, k, v in zip(range(len(diccedulas) + 1), diccedulas.keys(), diccedulas.values()):
        if troco >= 1:
            while True:
                if troco >= v:
                    troco -= v
                    acm[i] += 1
                else:
                    break
        else:
            str_troco = str(f"{troco:.2f}")
            if str_troco[3] == "1":
                troco -= 0.01
            if str_troco[3] == "2":
                troco -= 0.02
            if str_troco[3] == "3":
                troco += 0.02
            if str_troco[3] == "4":
                troco += 0.01
            if str_troco[3] == "6":
                troco -= 0.01
            if str_troco[3] == "7":
                troco -= 0.02
            if str_troco[3] == "8":
                troco += 0.02
            if str_troco[3] == "9":
                troco += 0.01
            while True:
                troco = float(f"{troco:.2f}")
                if troco >= v:
                    troco -= v
                    acm[i] += 1
                else:
                    break
    for c in acm:
        if c > 0:
            quant[0].append(f"[{c}]")
        else:
            quant[0].append("")
    return quant
