from PySimpleGUI import SetOptions, rgb
import PySimpleGUI as sg
from datetime import datetime
op = ""
data = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"


def login():
    sg.theme("SystemDefault")
    SetOptions(background_color="#252525", text_color="#feb403", scrollbar_color=rgb(255, 255, 255),
               input_text_color="#FFFAFA", input_elements_background_color="#3A3B3C")
    layout = [[sg.Text("Usuário:", font="Verdana 9 bold", background_color="#3A3B3C", size=(12, 0)),
               sg.Input(size=(11, 0), key="log", font="Verdana 10 bold")],
              [sg.Text("Senha:", font="Verdana 9 bold", background_color="#3A3B3C", size=(12, 0)),
               sg.Input(size=(11, 0), key="password", font="Verdana 10 bold")],
              [sg.Push(background_color="#252525"), sg.Button("Avançar", key="avancar", button_color="#feb403",
                                                              bind_return_key=True, size=(9, 0)),
               sg.Exit("Cancelar", key="cancelar", button_color="#252525", size=(9, 0)),
               sg.Push(background_color="#252525")],
              ]
    layout1 = [[sg.Image("logo1.png", size=(200, 125))]]
    layout2 = [
        [sg.Column(layout), sg.VSeparator(), sg.Column(layout1)]
    ]
    return sg.Window(font="Verdana", layout=layout2, title="--PDV-- Login", finalize=True, return_keyboard_events=True)


def pdv():  # PDV interface principal
    compras = []
    head = ["  Item  ", "  Descrição  ", "   Valor   ", " Quantidade ", "  Total  "]
    sg.theme("SystemDefault")
    SetOptions(background_color="#252525", scrollbar_color=rgb(255, 255, 255), text_color=rgb(255, 255, 255), )
    layout = [[sg.Text("Descrição", size=(35, 0), key="descricao", background_color="#3A3B3C", expand_x=True, font="Verdana 25 bold",
                       text_color=rgb(255, 255, 255), justification="center")],
              [sg.Text('Código:', text_color="#feb403", font="Verdana 15 bold", background_color="#252525",
                       size=(7, 0)), sg.Input(key='produto', size=(14, 0), background_color="#FFFFFF", text_color=rgb(0, 0, 0),
                                              font="Verdana 13 bold")],
              [sg.Button('Adcionar', key='busca', button_color="#feb403", size=(15, 0), bind_return_key=True),
              sg.Text('', key='vazio', size=(23, 0), background_color="#252525")],
              [sg.Table(size=(125, 27), key='op', values=compras, headings=head, justification="center"), sg.Image("logo0.png", size=(450, 450))],
              [sg.Input(size=(10, 0), font="Verdana 15 bold", key="qua", default_text="1,000"),
               sg.Text(size=(10, 0), text_color=rgb(0, 0, 0), background_color="#FFFAFA", font="Verdana 15 bold", key="pu", text="0,00"),
               sg.Text(size=(10, 0), text_color=rgb(0, 0, 0), background_color="#FFFAFA", font="Verdana 15 bold", key="des", text="0,00"),
               sg.Text(size=(10, 0), text_color=rgb(0, 0, 0), background_color="#FFFAFA", font="Verdana 15 bold", key="tt", text="0,00")],
              [sg.Text("    Quantidade    ", font="Verdana 12 bold", background_color="#252525"),
               sg.Text("  Valor Unitário    ", font="Verdana 12 bold", background_color="#252525"),
               sg.Text("   Desconto       ", font="Verdana 12 bold", background_color="#252525"),
               sg.Text("  Preço Total", font="Verdana 12 bold", background_color="#252525"), sg.Push(background_color="#252525"),
               sg.Text("Total:", font="Verdana 14 bold", background_color="#252525"),
               sg.Text(size=(10, 0), text_color=rgb(0, 0, 0), background_color="#FFFAFA",
                                         font="Verdana 15 bold", key="tot", text="0,00")],
              [sg.Text("Caixa 001", font="Verdana 14 bold", background_color="#252525"), sg.Push(background_color="#252525"),
               sg.Text("IP: 000.000.0.000", background_color="#252525")],
              [sg.Text(f"Operador: {op}", background_color="#252525"), sg.Push(background_color="#252525"),
               sg.Text(f"Data: {data}", background_color="#252525")]
              ]
    return sg.Window('Caixa', layout=layout, finalize=True, size=(1100, 714), return_keyboard_events=True)


def cadastro_clientes():
    sg.theme("SystemDefault")
    SetOptions(text_color="#feb403", scrollbar_color=rgb(255, 255, 255),
               input_text_color="#FFFAFA", input_elements_background_color="#3A3B3C",
               background_color="#252525")
    layout = [
        [sg.Text('Nome:'), sg.Input()],
              [sg.Checkbox('Física'), sg.Checkbox('Jurídica')],
              [sg.Text('CPF:'), sg.Input(size=(11, 0))],
              [sg.Text('Dados gerais')],
              [sg.Text('Dia do Aniversário:'), sg.Input(size=(20, 0)), sg.Text('', size=(11, 0)), sg.Text('Sexo:'),
               sg.Input(size=(20, 0))], [sg. Text('', size=(9, 0)), sg.Text('RG:'), sg.Input(size=(20, 0))],
              [sg.Button('Salvar', key='save'), sg.Exit('Sair', key='fim')]
              ]
    return sg.Window('Cadastro de clientes', layout=layout, finalize=True, size=(800, 440), return_keyboard_events=True)


def fecha(compra):  # Fecha Cupom
    quanti = []
    cedulas = ['R$100,00', 'R$50,00', 'R$20,00', 'R$10,00', 'R$5,00', 'R$2,00', 'R$1,00', 'R$0,50', 'R$0,25', 'R$0,10', 'R$0,05']
    sg.theme("DarkGreen5")
    SetOptions(text_color="#feb403", scrollbar_color=rgb(255, 255, 255),
               input_text_color=rgb(0, 0, 0), input_elements_background_color="#3A3B3C", background_color="#252525")
    # LAYOUT DA JANELA
    layout = [[sg.Button("Dinheiro", button_color="#252525", font="Verdana 13 bold", size=(15, 0)),
               sg.Text("Compra R$:", font="Verdana 13 bold", text_color=rgb(255, 255, 255),
                       background_color="#252525", size=(10, 0)),
               sg.Input(compra, key="compra", font="Verdana 15 bold", size=(12, 0), background_color="#ffffff", text_color=rgb(0, 0, 0))],
              [sg.Button("Cartão", button_color="#252525", font="Verdana 13 bold", size=(15, 0)),
               sg.Text("Pago R$:", font="Verdana 13 bold", text_color=rgb(255, 255, 255),
                       background_color="#252525", size=(10, 0)),
               sg.InputText(background_color="#ffffff", key="pago", font="Verdana 15 bold", size=(12, 0), text_color=rgb(0, 0, 0))],
              [sg.Button("Outros", button_color="#252525", font="Verdana 13 bold", size=(15, 0)),
               sg.Text("Troco R$:", font="Verdana 13 bold", text_color=rgb(255, 255, 255),
                       background_color="#252525", size=(10, 0)),
               sg.Input(default_text="0,00", font="Verdana 15 bold", size=(12, 0), background_color="#ffffff",
                        text_color=rgb(0, 0, 0), key="troco")],
              [sg.Button('Calcular', bind_return_key=True), sg.Exit('Sair', key='Sair')],
              [sg.Table(key="tb", headings=cedulas, values=quanti, justification="center", size=(50, 2))]
    ]
    return sg.Window('Fecha', layout=layout, finalize=True, return_keyboard_events=True)


def cadastro(cache=""):  # Cadastro de produtos
    sg.theme("SystemDefault")
    SetOptions(background_color="#252525", text_color="#feb403", scrollbar_color=rgb(255, 255, 255),
               input_text_color="#FFFAFA", input_elements_background_color="#3A3B3C")
    layout = [[sg.Text('Nome:', size=(10, 0)), sg.Input(size=(15, 0), key='nome')],
              [sg.Text('Valor: R$', size=(10, 0)), sg.Input(size=(15, 0), key='valor')],
              [sg.Text('Código de barras:', size=(10, 0)), sg.Input(default_text=cache, size=(15, 0), key='cb')],
              [sg.Button('Pronto', key='pronto'), sg.Exit('Fechar')],

              ]
    return sg.Window('Cadastro', layout=layout, finalize=True, size=(800, 440), return_keyboard_events=True)


def non():  # Produtos não encontrados
    sg.theme("SystemDefault")
    SetOptions(background_color="#252525", text_color="#feb403", scrollbar_color=rgb(255, 255, 255),
               input_text_color="#FFFAFA", input_elements_background_color="#3A3B3C")
    layout = [[sg.Text('Produto não encontrado')],
              [sg.Text('Quer cadastra-lo?')],
              [sg.Button('Cadastrar', key='add1'), sg.Exit('Sair', key='k')]]
    return sg.Window('Erro...', layout=layout, size=(500, 200), finalize=True, return_keyboard_events=True)


