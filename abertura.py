from PDV_func import *
from Janelas import *

produtos_passados = {}
events = ["cancelar", "Escape:27", "fim", "Fechar"'', sg.WIN_CLOSED]
janelas = {0: login(), 1: None, 2: None,
           3: None, 4: None, 5: None}
compras = []
contador_itens = 0
produtos = [{'Nome': 'Leite', 'Cb': '1212', 'Valor': '4.56', "Quantidade": 0}]
soma = 0
pgmt = None
cache = ""
user_auth = False
#  INICIANDO PROGRAMA
while True:
    # LEITURA DE EVENTOS E JANELAS
    window, event, values = sg.read_all_windows()
    print(event)
    # FiINALIZANDO JANELAS
    if event in events:
        if window == janelas[0] or window == janelas[1]:
            break
        elif window == janelas[2]:
            janelas[2].close()
            janelas[2] = None
        elif window == janelas[3]:
            if values["troco"] == "0,00":
                validacao = sg.PopupYesNo("Quer mesmo cancelar a ação?\n"
                                          "A compra não foi finalizada.",
                                          font="Verdana 8 bold", button_color="#feb403",
                                          background_color="#252525")
                if validacao == "Yes":
                    janelas[3].close()
                    janelas[3] = None
                else:
                    pass
            else:
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
        with open("auth.txt", "r") as autenticar:
            data = autenticar.read()
            if values["log"] == data.split(" - ")[0] and values["password"] == data.split(" - ")[1]:
                user_auth = True
                janelas[1] = pdv()
                janelas[0].close()
            else:
                janelas[0]["vf"].update("Informação inválida")
    if window == janelas[1] and user_auth:
        # INICIANDO CADASTRO DE CLIENTES
        if event == "F2:113" and janelas[2] is None:
            janelas[2] = cadastro_clientes()

        # INICIANDO JANELA DE FECHAR COMPRA
        if event == "F3:114" and janelas[3] is None and len(compras) > 0:
            janelas[1]["qua"].update("1,000")
            janelas[1]["pu"].update("0,00")
            janelas[1]["tt"].update("0,00")
            janelas[1]["descricao"].update("Descrição")
            janelas[3] = fecha(str(f'{soma:.2f}').replace('.', ','))
            soma = 0
            contador_itens = 0
            tot = str(f'{soma:.2f}').replace('.', ',')
            janelas[1]['tot'].update(f'{tot}')
            compras = []
            janelas[1]["op"].update(values=compras)

<<<<<<< Updated upstream
        # INICIANDO CADASTRO DE PRODUTOS
        if event == "F4:115" and janelas[4] is None:
            janelas[4] = cadastro()
=======
<<<<<<< HEAD
        # INICIANDO CADASTRO DE PRODUTOS
        if event == "F4:115" and janelas[4] is None:
            janelas[4] = cadastro()
=======
    # INICIANDO JANELA DE FECHAR COMPRA
    if event == "F3:114" and janelas[3] is None and len(compras) > 0:
        janelas[1]["qua"].update("1,000")
        janelas[1]["pu"].update("0,00")
        janelas[1]["tt"].update("0,00")
        janelas[1]["descricao"].update("Descrição")
        janelas[3] = fecha(str(f'{soma:.2f}').replace('.', ','))
        soma = 0
        contador = 0
        contador_itens = 0
        tot = str(f'{soma:.2f}').replace('.', ',')
        janelas[1]['tot'].update(f'{tot}')
        compras = []
        janelas[1]["op"].update(values=compras)

    # INICIANDO CADASTRO DE PRODUTOS
    if event == "F4:115" and janelas[4] is None:
        janelas[4] = cadastro()
>>>>>>> cc437e0ddf62ca040c26a1d482aafefffeee519c
>>>>>>> Stashed changes
    if event == 'add1':
        janelas[5].close()
        janelas[4] = cadastro(cache)
    # EVENTOS DO PDV
    # BUSCANDO PRODUTOS
    if event == "busca" and len(values["produto"].strip()) > 2:
        a = busca(values["produto"], produtos)
        # PRODUTO ENCONTRADO
        if a:
            janelas[1]["descricao"].update(a["Nome"])
            contador_itens += 1
            # EVITANDO ERRO QUANTIDADE VAZIA
            if values["qua"].strip() == "":
                values["qua"] = "1,000"
            values["qua"] = float(values["qua"].replace(",", "."))
            # DEFININDO SOMA À SER EXIBIDA
            soma += float(a["Valor"]) * values["qua"]
            # FORMATANDO VALOR (SOMA)
            tot = str(f'{soma:.2f}').replace('.', ',')
            # ATUALIZANDO JANELA PARA O VALOR FORMATADO
            janelas[1]['tot'].update(f'{tot}')
            # DEFININDO VALRORES DA TABELA
            janelas[1]["produto"].update("")
            compras.append([contador_itens, a["Nome"], str(f"{float(a['Valor']):.2f}").replace('.', ','),
                            str(f"{values['qua']:.3f}").replace('.', ','),
                            str(f"{float(a['Valor']) * float(values['qua']):.2f}").replace('.', ',')])
            janelas[1]["pu"].update(str(f"{float(a['Valor']):.2f}").replace('.', ','))
            janelas[1]["tt"].update(str(f"{float(a['Valor']) * float(values['qua']):.2f}").replace('.', ','))
            # ATUALIZANDO TABELA
            janelas[1]["op"].update(values=compras)
        # PRODUTO NÃO ENCONTRADO
        else:
            # DEFININDO VARIÁVEL COM CÓDIGO NÃO CADASTRADO
            cache = values["produto"]
            # INICIANDO JANELA DE ERRO
            janelas[5] = non()
    elif event == "busca" and len(values["produto"].strip()) > 0:
        janelas[1]["qua"].update(values["produto"].strip())
        janelas[1]["produto"].update("")
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
    # FECHANDO A COMPRA
    quant = [[]]
    if window == janelas[3]:
        if event == "Dinheiro":
            janelas[3]["Dinheiro"].update(button_color="#feb403")
            janelas[3]["Cartão"].update(button_color="#252525")
            janelas[3]["Outros"].update(button_color="#252525")
            pgmt = 0
        if event == "Cartão":
            janelas[3]["Dinheiro"].update(button_color="#252525")
            janelas[3]["Cartão"].update(button_color="#feb403")
            janelas[3]["Outros"].update(button_color="#252525")
            pgmt = 1
        if event == "Outros":
            janelas[3]["Dinheiro"].update(button_color="#252525")
            janelas[3]["Cartão"].update(button_color="#252525")
            janelas[3]["Outros"].update(button_color="#feb403")
            pgmt = 2

        if pgmt == 0 and event == 'Calcular' and values['pago'].strip() != '':
            # FACILITADOR DE TROCO
            compra = float(f"{values['compra']}".replace(",", "."))
            pago = float(f"{values['pago']}".replace(",", "."))
            janelas[3]["troco"].update(f"{pago - compra:.2f}".replace(".", ","))
            a = troco(compra, pago)
            janelas[3]["tb"].update(values=a)
            continue
