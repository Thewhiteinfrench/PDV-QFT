from PDV_func import *
from Janelas import *
produtos_passados = {}
events = ["cancelar", "saida", "fim", "Sair", "Fechar", "k", sg.WIN_CLOSED]
janelas = {0: login(), 1: None, 2: None,
           3: None, 4: None, 5: None}
compras = []
contador = 0
produtos = [{'Nome': 'Leite', 'Cb': '1111111111111', 'Valor': '4.56'}]
soma = 0
cache = ""
#  INICIANDO PROGRAMA
while True:
    window, event, values = sg.read_all_windows()
    # FiINALIZANDO JANELAS
    if event in events:
        if window == janelas[0]:
            break
        elif window == janelas[1]:
            janelas[1].close()
            janelas[0] = login()
        elif window == janelas[2]:
            janelas[2].close()
            janelas[2] = None
        elif window == janelas[3]:
            janelas[3].close()
            janelas[3] = None
        elif window == janelas[4]:
            janelas[4].close()
            janelas[4] = None
        elif window == janelas[5]:
            janelas[5].close()
            janelas[5] = None
    # EVENTOS DE INICIALIZAÇÃO DE JANELAS
    if event == "avancar":
        janelas[1] = pdv()
        janelas[0].close()
    # INICIANDO CADASTRO DE CLIENTES
    if event == "cc" and janelas[2] is None:
        janelas[2] = cadastro_clientes()
    # INICIANDO JANELA DE FECHAR COMPRA
    if event == "end" and janelas[3] is None:
        janelas[3] = fecha(str(f'''{soma:.2f}''').replace('.', ','))
        soma = 0
        contador = 0
        tot = str(f'{soma:.2f}').replace('.', ',')
        janelas[1]['tot'].update(f'{tot:>140}')
        compras = []
        janelas[1]["op"].update(values=compras)
    # INICIANDO CADASTRO DE PRODUTOS
    if event == "add" and janelas[4] is None:
        janelas[4] = cadastro()
    if event == 'add1':
        janelas[5].close()
        janelas[4] = cadastro(cache)
    # EVENTOS DO PDV
    # BUSCANDO PRODUTOS
    if event == "busca" and values["produto"].strip() != "":
        window.refresh()
        a = busca(values["produto"], produtos)
        if a:
            print(a["Cb"])
            contador += 1
            if values["qua"].strip() == "":
                values["qua"] = "1"
            soma += float(a["Valor"]) * float(values["qua"].replace(",", "."))
            tot = str(f'{soma:.2f}').replace('.', ',')
            janelas[1]['tot'].update(f'{tot:>140}')
            compras.append([contador, a["Nome"], a["Valor"],
                            values["qua"].replace(",", ".")])
            janelas[1]["op"].update(values=compras)
        else:
            cache = values["produto"]
            janelas[5] = non()
    # CADASTRANDO PRODUTOS !!!ALTERAR EM BREVE!!! DB EM XLSX
    if event == 'pronto' and values['nome'] != '' and values['cb'] != '' and values['valor'] != '':
        values['valor'] = values['valor'].replace(',', '.')
        # FORMATANDO
        janelas[4]['nome'].update('')
        janelas[4]['cb'].update('')
        janelas[4]['valor'].update('')
        produtos.insert(0, {})
        produtos[0]['Nome'] = values['nome']
        produtos[0]['Cb'] = values['cb']
        produtos[0]['Valor'] = values['valor']
        for k, v in produtos[0].items():
            print(f"{k, v}", end="")
    # FECHANDO A COMPRA
    quant = [[]]
    if event == 'Calcular' and values['pago'] != '' and values['compra'] != '0,00':
        # FACILITADOR DE TROCO
        compra = float(f"{values['compra']}".replace(",", "."))
        pago = float(f"{values['pago']}".replace(",", "."))
        janelas[3]["troco"].update(f"R${pago - compra:.2f}".replace(".", ","))
        a = troco(compra, pago)
        janelas[3]["tb"].update(values=a)
        continue
