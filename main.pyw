import os
import sys
import csv
from random import randint
from PIL import Image
import yfinance
import customtkinter
from validos import ativos_validos

# versão
vers = 'v0.2.1'


# dividend yield (%) - retorno esperado:
dy = 0.06 #6%
# período consultado - histórico de dividendos pagos:
anos = 5


class Ativo: # referente aos ativos e consulta (yfinance)

    def __init__(self, ticker):
        self.ticker = ticker.upper().strip()

        if self.ticker in ativos_validos:
            self.conectar()

        elif len(ativos_validos) == 0:
            if len(self.ticker) in [5, 6]:
                self.conectar()

    def conectar(self):
        self.conexao = yfinance.Ticker(f'{self.ticker}.SA')
        self.calculo()

    def calculo(self):
        try:
            self.conexao.history(period=f'{anos}y')
            self.avg = sum(self.conexao.dividends) / anos
            self.pt = self.avg / dy
            self.pa = self.conexao.info["currentPrice"]
            self.pt = f'{self.pt:.2f}'
        except KeyError:
            pass
        except ArithmeticError:
            pass

    def retorno(self, janela_nome='Carteira'):
        if janela_nome == 'Carteira':
            try:
                info_lista = [self.pt, self.pa]

                return info_lista

            except AttributeError:
                pass

        if janela_nome == 'Consulta':
            try:
                tk = self.conexao.info['symbol']
                nm = self.conexao.info["longName"]
                info_lista = [self.pt, self.pa, nm, tk[:-3]]

                return info_lista

            except AttributeError:
                pass
            except LookupError:
                pass


class Interface: # referente a estrutura gráfica (executável) do customtkinter

    def __init__(self):
        self.root = customtkinter.CTk()

    def criarDimensao(self):
        self.root.title(f'Ticker6 -- {vers}')
        self.root.geometry('700x400+150+150')
        self.root._set_appearance_mode('dark')
        self.root.resizable(width=False, height=False)

    def criarJanela(self, j1='Carteira', j2='Consulta', j3='...'):
        self.j1, self.j2, self.j3 = j1, j2, j3

        self.janela = customtkinter.CTkTabview(self.root, width=670, height=370, corner_radius=5, fg_color='gray17',
            segmented_button_fg_color='gray17', segmented_button_selected_color='gray17', bg_color='gray14',
                segmented_button_unselected_color='gray20', segmented_button_selected_hover_color='gray17',
                    segmented_button_unselected_hover_color='gray23', border_width=1, border_color='gray')

        self.janela.pack()
        self.janela.add(f'{j1}')
        self.janela.add(f'{j2}')
        self.janela.add(f'{j3}')

        return self.janela

    def criarTitulo(self):
        titulo = customtkinter.CTkLabel(self.janela.tab(self.j1), text='Carteira', font=("arial bold", 16),
            text_color='gray')

        titulo.place(x=20, y=20)

        customtkinter.CTkLabel(self.janela.tab(self.j2), text='Consulta', font=("arial bold", 16),
            text_color='gray').place(x=20, y=20)

        return titulo

    def criarEntrada(self):
        entrada = customtkinter.CTkEntry(self.janela.tab(f'{self.j2}'),
            width=100, placeholder_text=' ...', placeholder_text_color='white', fg_color='gray10', text_color='white',
                font=("Calibri", 14), border_color='gray', border_width=2)

        entrada.place(x=90, y=20)

        return entrada

    def criarBotao(self):
        customtkinter.CTkButton(self.janela.tab(f'{self.j2}'), text='>', width=1, command=InterfaceConsulta,
            corner_radius=10, text_color='light blue', fg_color='gray28', hover_color='dark sea green',
                anchor='center', border_color='gray', border_width=2).place(x=195, y=20)

        botao_adicionar = customtkinter.CTkButton(self.janela.tab(f'{self.j2}'), text='+', width=1, corner_radius=10,
            text_color='gray17', fg_color='gray28', hover_color='red', anchor='center',
                border_color='gray25', border_width=2)

        botao_adicionar.place(x=230, y=20)

        return botao_adicionar

    def criarBotaoRe(self):
        botao_remover = customtkinter.CTkButton(self.janela.tab('Consulta'), text='Remover da Carteira', width=1,
            corner_radius=10, text_color='white', fg_color='gray28', hover_color='dark sea green',
                anchor='center', border_color='gray25', border_width=2)

        botao_remover.place(x=270, y=20)

        return botao_remover

    def gerarInterface(self):
        self.atualizarInterface()
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            exit()

    def atualizarInterface(self):
        if len(carteira) > 0:
            for rotulo in carteira_corrente:
                ticker = rotulo[0]
                l1 = rotulo[1]
                l0 = rotulo[2]

                info = Ativo(ticker).retorno()

                l1.configure(text=status(1, info, ticker))
                l0.configure(text=status(0, info), text_color=statusCor(info))

        if len(consulta_corrente) > 0:
            for rotulo in consulta_corrente:
                ticker = rotulo[0]
                l1 = rotulo[1]
                l0 = rotulo[2]
                l3 = rotulo[3]

                info = Ativo(ticker).retorno('Consulta')

                l1.configure(text=status(1, info, ticker))
                l0.configure(text=status(0, info), text_color=statusCor(info))
                l3.configure(text='{}\n{}\n\n{}'.format(info[2], '> Preço Teto (Bazin)', '> Cotação'))

        self.root.after(600000, self.atualizarInterface) # 10min para atualização dos rótulos


class InterfaceCarteira: # referente a janela carteira no programa

    def __init__(self, lista):
        global titulo_j1, msg, carteira_corrente, carteira

        titulo_j1.configure(text=f'Carteira ({len(lista)})')

        x = 20  # posição X inicia em 20
        if len(lista) <= 4:

            for ticker in lista:
                info = Ativo(ticker).retorno()

                l1, l0, rotulo_img = criarRotulo(info, ticker)
                l1.place(x=x, y=80)
                l0.place(x=x-2, y=125)

                if rotulo_img.cget("text") == '':
                    rotulo_img.place(x=x+80, y=79)

                carteira_corrente.append([ticker, l1, l0, rotulo_img])
                x = x + 170

        elif len(lista) in [5, 6, 7, 8]:
            x = 20  # posição X inicia em 20

            for ticker in lista[:4]:
                info = Ativo(ticker).retorno()

                l1, l0, rotulo_img = criarRotulo(info, ticker)
                l1.place(x=x, y=80)
                l0.place(x=x-2, y=125)

                if rotulo_img.cget("text") == '':
                    rotulo_img.place(x=x+80, y=79)

                carteira_corrente.append([ticker, l1, l0, rotulo_img])
                x = x + 170

            x = 20  # posição X retorna para 20
            for ticker in lista[4:]:

                info = Ativo(ticker).retorno()

                l1, l0, rotulo_img = criarRotulo(info, ticker)
                l1.place(x=x, y=200)
                l0.place(x=x-2, y=245)

                if rotulo_img.cget("text") == '':
                    rotulo_img.place(x=x+80, y=199)

                carteira_corrente.append([ticker, l1, l0, rotulo_img])
                x = x + 170
        else:
            carteira = lista[:8]
            Arquivo().reescrever(conteudo=carteira)
            InterfaceCarteira(carteira)

        if len(lista) == 0:
            aleatorio = randint(1,3)
            if aleatorio == 1:
                msg = aviso('Voçê pode adicionar até 8 ativos à carteira...', 'Carteira')
            if aleatorio == 2:
                msg = aviso('Faça uma consulta e adicione seus ativos favoritos à carteira...', 'Carteira')
            if aleatorio == 3:
                msg = aviso('', 'Carteira')
        else:
            apagarMsg()


class InterfaceConsulta: # referente a janela de consulta no programa

    def __init__(self):
        global consulta_corrente
        try:
            if len(consulta_corrente) > 0:
                if len(entrada.get()) in [5, 6]:
                    self.atualizarRotulo('Consulta')

            info = Ativo(entrada.get()).retorno('Consulta')

            l1, l0, rotulo_img = criarRotulo(info, ticker=info[3], local='Consulta')
            l1.place(x=20, y=80)
            l0.place(x=18, y=125)

            if rotulo_img.cget("text") == '':
                rotulo_img.place(x=20+80, y=79)

            l3 = customtkinter.CTkLabel(janela.tab('Consulta'), text='{}\n{}\n\n{}'
                .format(info[2], '> Preço Teto (Bazin)', '> Cotação'), font=("Consolas", 13),
                    text_color='light green', fg_color='transparent', corner_radius=5, justify='left')
            l3.place(x=140, y=85)

            consulta_corrente = [[info[3], l1, l0, l3, rotulo_img]]

            self.alterarBotoes()

            entrada.delete(0, last_index='end')
        except TypeError:
            pass

    def alterarBotoes(self):
        global botao_adicionar, botao_remover
        try:
            self.ticker = consulta_corrente[0][0]
        except IndexError:
            self.ticker = ['']

        if self.ticker in carteira:
            botao_adicionar.configure(hover_color='red', command=None)
            botao_remover = root.criarBotaoRe()
            botao_remover.configure(command=self.removerAtivo)
        else:
            botao_adicionar.configure(hover_color='dark sea green', command=self.adicionarAtivo)
            apagarBotaoRe()

            if len(consulta_corrente) == 0:
                botao_adicionar.configure(hover_color='red', command=None)

    def adicionarAtivo(self):
        if len(carteira_corrente) < 8:
            Arquivo().escrever()
            self.atualizarRotulo()
            self.atualizarRotulo('Consulta')
            self.alterarBotoes()

    def atualizarRotulo(self, janela_nome='Carteira'):
        global carteira, carteira_corrente, consulta_corrente

        if janela_nome == 'Consulta':
            for rotulo in consulta_corrente:
                rotulo[1].destroy()
                rotulo[2].destroy()
                rotulo[3].destroy()
                rotulo[4].destroy()
            consulta_corrente.clear()

        if janela_nome == 'Carteira':
            for rotulo in carteira_corrente:
                rotulo[1].destroy()
                rotulo[2].destroy()
                rotulo[3].destroy()
            carteira_corrente.clear()
            carteira = Arquivo().ler()
            InterfaceCarteira(carteira)

    def removerAtivo(self):
        global carteira

        ticker = consulta_corrente[0][0]
        carteira.remove(f'{ticker}')
        Arquivo().reescrever(conteudo=carteira)

        self.atualizarRotulo()
        self.atualizarRotulo('Consulta')
        self.alterarBotoes()
        apagarBotaoRe()


class Arquivo: # manipulação de arquivos

    def ler(self, nome_arquivo='.ativos.csv'):
        lista = []
        try:
            with open(dir, 'r', newline='', encoding='UTF-8') as self.arquivo:
                conteudo = csv.reader(self.arquivo)
                lista = [ticker.upper() for linha in conteudo for ticker in linha]
            self.fechar()

        except FileNotFoundError:
            if nome_arquivo == '.ativos.csv':
                self.criar()
            else:
                pass
        finally:
            return lista

    def escrever(self):
        with open(dir, 'a', newline='', encoding='UTF-8') as self.arquivo:
            ticker = consulta_corrente[0][0]
            escritor = csv.writer(self.arquivo)
            escritor.writerow([ticker])
        self.fechar()

    def reescrever(self, conteudo):
        with open(dir, 'w+', newline='', encoding='UTF-8') as self.arquivo:
            escritor = csv.writer(self.arquivo)
            for ticker in conteudo:
                escritor.writerow([ticker])
        self.fechar()

    def criar(self):
        with open(dir, 'x', encoding='UTF-8') as self.arquivo:
            pass
        self.fechar()

    def fechar(self):
        self.arquivo.close()


# funções gerais
def status(local, info, nome_ticker=None):
    """
    tratamento da informação a ser retornada no rótulo
    local: 1 (superior), 0 (inferior)
    info: retorno de uma consulta (uma lista)
    """
    if local == 1:
        nome_ticker = nome_ticker.upper().strip()
        info = '{:^8} \nR$ {:<8} \n\n'.format(nome_ticker, info[0])

        return info

    if local == 0:
        info = 'R$ {:<8} '.format(info[1])

        return info

def statusCor(info): # tratamento de cor da informação a ser retornada
    if float(info[1]) <= float(info[0]):
        cor = 'light green'
    else:
        cor = 'salmon3'

    return cor

def aviso(mensagem, local='Carteira'): # definição de rótulo de mensagem
    aviso_ = customtkinter.CTkLabel(janela.tab(f'{local}'), text=f'{mensagem}', font=("arial bold", 13),
        text_color='gray', fg_color='transparent')
    aviso_.pack(pady=100)

    return aviso_

def apagarMsg(): # excluir rótulo de mensagem
    global msg
    try:
        msg.destroy()
    except AttributeError:
        pass

def apagarBotaoRe(): # excluir rótulo botão remover
    global botao_remover
    try:
        botao_remover.destroy()
    except NameError:
        pass

def criarRotulo(info, ticker, local='Carteira'): # criação de rótulo (com textos e imagem)
    caminho = diretorio(ticker)
    imagem = None

    l1 = customtkinter.CTkButton(janela.tab(local), text=status(1, info, ticker),
                                font=("Consolas", 14), text_color='white', fg_color='gray26', corner_radius=7,
                                width=70,
                                anchor='w', height=10)

    l0 = customtkinter.CTkLabel(janela.tab(local), text=status(0, info), font=("Consolas", 14),
                                text_color=statusCor(info), fg_color='transparent', corner_radius=7, width=110,
                                anchor='w')

    if os.path.exists(caminho):
        imagem = customtkinter.CTkImage(dark_image=Image.open(caminho), size=(30, 30))

        rotulo_img = customtkinter.CTkLabel(janela.tab(local), text='', fg_color='transparent', corner_radius=4,
                                            image=imagem,
                                            width=5, height=33)
    else:
        rotulo_img = customtkinter.CTkLabel(janela.tab(local), text='N', fg_color='transparent', corner_radius=0,
                                            image=imagem,
                                            width=0, height=0)

    return l1, l0, rotulo_img


def diretorio(ticker):
    if hasattr(sys, '_MEIPASS'):
        caminho = os.path.join(sys._MEIPASS, 'img', f'{ticker[:4]}.jpg')
    else:
        caminho = os.path.join('img', f'{ticker[:4]}.jpg')
    return caminho


if __name__ == '__main__':

    # ativos e rótulos que estão em 'carteira' em execução
    carteira_corrente = []
    # ativos e rótulos que estão em 'consulta' em execução
    consulta_corrente = []
    # mensagem, avisos
    msg = None

    # diretório
    dir_padrao = os.path.expanduser("~")
    dir = os.path.join(dir_padrao, '.ativos.csv')

    ##
    root = Interface()

    root.criarDimensao()
    janela = root.criarJanela()

    titulo_j1 = root.criarTitulo()
    entrada = root.criarEntrada()
    botao_adicionar = root.criarBotao()

    carteira = Arquivo().ler()

    InterfaceCarteira(lista=carteira)

    ###
    root.gerarInterface()
    