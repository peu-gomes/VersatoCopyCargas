import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime


def selecionar_arquivo():
    global caminho_unificada_interface
    caminho_unificada_interface = filedialog.askopenfilename()
    btn_baixar_unificada["state"] = tk.NORMAL

def selecionar_pasta_baixar():
    
    agora = datetime.now()

    # Formata o carimbo de data/hora para ser usado no nome do arquivo
    timestamp = agora.strftime("%Y%m%d_%H%M%S")

    # Adiciona o carimbo de data/hora ao nome do arquivo
    nome_arquivo = f'exportação_unificada_{timestamp}.xlsx'
    caminho_unificada_baixar = filedialog.askdirectory()
    caminho_unificada_baixar_concat = caminho_unificada_baixar + '/' + nome_arquivo
    
    # Leia o arquivo Excel e armazene os dados em dois DataFrames
    unificada_aba_recebidas_df = pd.read_excel(caminho_unificada_interface, sheet_name=0)
    unificada_aba_devolucoes_df = pd.read_excel(caminho_unificada_interface, sheet_name=2)
    
    #ok
    
    
    # Manipulação dos dados gerais da aba recebidas
    # Exclua as linhas em branco da primeira coluna
    unificada_aba_recebidas_apagar_zaradas_df = unificada_aba_recebidas_df.dropna(subset=['Unnamed: 0'])
    unificada_aba_devolucoes_apagar_zaradas_df = unificada_aba_devolucoes_df.dropna(subset=['Unnamed: 0'])

    unificada_aba_recebidas_apagar_zaradas_df.columns = unificada_aba_recebidas_apagar_zaradas_df.iloc[0]
    unificada_aba_devolucoes_apagar_zaradas_df.columns = unificada_aba_devolucoes_apagar_zaradas_df.iloc[0]

    unificada_aba_recebidas_apagar_zaradas_df = unificada_aba_recebidas_apagar_zaradas_df[1:]
    unificada_aba_devolucoes_apagar_zaradas_df = unificada_aba_devolucoes_apagar_zaradas_df[1:]

    #print(unificada_aba_recebidas_apagar_zaradas_df)
    #if (unificada_aba_devolucoes_apagar_zaradas_df == 0).all().all():
    #    print('zerado')
    #else:
    #    print(unificada_aba_devolucoes_apagar_zaradas_df)
        
    #ok    
        
    
    # Lista de colunas para excluir
    #unificada_aba_recebidas_colunas_para_excluir_df = ['CNPJ Prestador', 'Simples',
    #'Serviço', 'Pagamentos', 'IRRF', 'CSRF',
    #'INSS', 'ISS', 'Cód IRRF', 'Cód PCC',
    #'Base Cal. INSS', 'Base Cal. ISS',
    #'Descontos', 'Valor Líquido', 'P.A IR', 'P.A PCC', 'P.A INSS',
    #'P.A ISS', 'Descrição']

    #unificada_aba_devolucoes_colunas_para_excluir_df = ['CNPJ Prestador',
    #'Nota Referenciada','Pagamentos', 'Valor Líquido', 'Centro de Custo', 'Descrição']

    colunas_desejadas_recebidas = ['Prestador', 'Tipo', 'Nº Nota Fiscal', 'Emissão', 'Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS', 'Caução']
    unificada_aba_recebidas_colunas_desejadas_df = unificada_aba_recebidas_apagar_zaradas_df[colunas_desejadas_recebidas]
    
    colunas_desejadas_devolucoes = ['Prestador', 'Tipo', 'Nº Nota Fiscal', 'Natureza Da OP.', 'Nota Referenciada', 'Emissão',  'Valor Bruto']
    unificada_aba_devolucoes_colunas_desejadas_df = unificada_aba_devolucoes_apagar_zaradas_df[colunas_desejadas_devolucoes]

    #print(unificada_aba_recebidas_colunas_desejadas_df)
    #if (unificada_aba_devolucoes_colunas_desejadas_df == 0).all().all():
    #    print('zerado')
    #else:
    #    print(unificada_aba_devolucoes_colunas_desejadas_df)
    
    #ok
    
    # Exclua as colunas especificadas na lista anterior
    #unificada_aba_recebidas_colunas_excluir_colunas_df = unificada_aba_recebidas_apagar_zaradas_df.drop(columns=unificada_aba_recebidas_apagar_zaradas_df)
    #unificada_aba_devolucoes_colunas_excluir_colunas_df = unificada_aba_devolucoes_apagar_zaradas_df.drop(columns=unificada_aba_devolucoes_colunas_para_excluir_df)
    
    # Crie cópias explícitas dos DataFrames para evitar SettingWithCopyWarning
    unificada_aba_recebidas_colunas_desejadas_df = unificada_aba_recebidas_colunas_desejadas_df.copy()
    unificada_aba_devolucoes_colunas_desejadas_df = unificada_aba_devolucoes_colunas_desejadas_df.copy()

    # Adicione novas colunas
    unificada_aba_recebidas_colunas_desejadas_df['CÓD'] = ""
    unificada_aba_recebidas_colunas_desejadas_df['Débito'] = ""
    unificada_aba_recebidas_colunas_desejadas_df['Crédito'] = ""
    unificada_aba_recebidas_colunas_desejadas_df['Histórico'] = ""
    unificada_aba_recebidas_colunas_desejadas_df['H1'] = " "

    unificada_aba_devolucoes_colunas_desejadas_df['CÓD'] = ""
    unificada_aba_devolucoes_colunas_desejadas_df['Débito'] = ""
    unificada_aba_devolucoes_colunas_desejadas_df['Crédito'] = ""
    unificada_aba_devolucoes_colunas_desejadas_df['Histórico'] = ""
    unificada_aba_devolucoes_colunas_desejadas_df['H1'] = "S/"
    
    #print(unificada_aba_recebidas_colunas_desejadas_df)
    #if (unificada_aba_devolucoes_colunas_desejadas_df == 0).all().all():
    #    print('zerado')
    #else:
    #    print(unificada_aba_devolucoes_colunas_desejadas_df)
    
    
    #alterar nome de variavel para finalizar a manipulacao geral (foi idicionado como a versao 2)
    unificada_aba_recebidas_v2_df = unificada_aba_recebidas_colunas_desejadas_df
    unificada_aba_devolucoes_v2_df = unificada_aba_devolucoes_colunas_desejadas_df
    #print(unificada_aba_recebidas_v2_df.to_string())
    #print(unificada_aba_devolucoes_v2_df.to_string())
    
    #ok
    
    
    #manipulação notas

    notas_columns_para_exclusive = ['Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS', 'Caução']
    notas = unificada_aba_recebidas_v2_df.drop(columns=notas_columns_para_exclusive)
    notas = notas.rename(columns={'Valor Bruto': 'Valor'})
    notas = notas[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'Tipo', 'H1', 'Nº Nota Fiscal', 'Prestador']]
    notas['H1'] = 'Nº'
    notas['Crédito'] = '2.01.02.01.0001'
    notas['Valor'] = pd.to_numeric(notas['Valor'], errors='coerce')
    notas['Valor'] = notas['Valor'].round(2)
    #notas['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

    #manipulação impostos
    #manipulação irrf
    irrf_colunas_para_excluir = ['Valor Bruto', 'Valor CSRF', 'Valor INSS','Valor ISS', 'Caução']
    irrf = unificada_aba_recebidas_v2_df.drop(columns=irrf_colunas_para_excluir)
    irrf = irrf.dropna(subset='Valor IRRF')
    irrf = irrf[irrf['Valor IRRF'] != 0]
    irrf = irrf.rename(columns={'Valor IRRF': 'Valor'})
    irrf['H1'] = 'IRRF S/ '

    #manipulação pcc
    pcc_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor INSS','Valor ISS', 'Caução']
    pcc = unificada_aba_recebidas_v2_df.drop(columns=pcc_colunas_para_excluir)
    pcc = pcc.dropna(subset='Valor CSRF')
    pcc = pcc[pcc['Valor CSRF'] != 0]
    pcc = pcc.rename(columns={'Valor CSRF': 'Valor'})
    pcc['H1'] = 'PCC S/ '

    #manipulação inss
    inss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF','Valor ISS', 'Caução']
    inss = unificada_aba_recebidas_v2_df.drop(columns=inss_colunas_para_excluir)
    inss = inss.dropna(subset='Valor INSS')
    inss = inss[inss['Valor INSS'] != 0]
    inss = inss.rename(columns={'Valor INSS': 'Valor'})
    inss['H1'] = 'INSS S/ '

    #manipulação iss
    iss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Caução']
    iss = unificada_aba_recebidas_v2_df.drop(columns=iss_colunas_para_excluir)
    iss = iss.dropna(subset='Valor ISS')
    iss = iss[iss['Valor ISS'] != 0]
    iss = iss.rename(columns={'Valor ISS': 'Valor'})
    iss['H1'] = 'ISS S/ '

    #juntar tudo
    # Lista de DataFrames
    lista_impostos = [irrf, pcc, inss, iss]

    # Concatenar os DataFrames em um único DataFrame
    impostos = pd.concat(lista_impostos)

    # Adicionar uma coluna 'Débito' com o valor '2.01.02.01.0001'
    impostos['Débito'] = '2.01.02.01.0001'

    # Função para mapear valores da coluna 'H1' para a coluna 'Crédito'
    def mapear_credito(valor_h1):
        if 'IRRF' in valor_h1:
            return '1.02.04.02.001'
        elif 'INSS' in valor_h1:
            return '1.02.04.02.003'
        elif 'PCC' in valor_h1:
            return '1.02.04.02.004'
        elif 'ISS' in valor_h1:
            return '1.02.04.02.005'
        else:
            return None

    # Aplicar a função mapear_credito à coluna 'H1' e criar uma nova coluna 'Crédito'
    impostos['Crédito'] = impostos['H1'].apply(mapear_credito)

    # Adicionar uma coluna 'Histórico' com valores vazios
    impostos['Histórico'] = ""

    # Selecionar colunas relevantes
    impostos = impostos[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
    impostos['Valor'] = pd.to_numeric(impostos['Valor'], errors='coerce')
    impostos['Valor'] = impostos['Valor'].round(2)
    #impostos['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

    #manipulação caucao

    caucao_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS']
    caucao = unificada_aba_recebidas_v2_df.drop(columns=caucao_colunas_para_excluir)
    #print(caucao.to_string())
    caucao = caucao.dropna(subset='Caução')
    caucao = caucao[caucao['Caução'] != 0]
    caucao = caucao.rename(columns={'Caução': 'Valor'})
    caucao = caucao[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
    caucao['Valor'] = pd.to_numeric(caucao['Valor'], errors='coerce')
    caucao['Valor'] = caucao['Valor'].round(2)
    caucao['H1'] = 'RETENÇÃO CONTRATUAL S/'
    #caucao['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

    #manipulação devolucao
    #print(unificada_aba_devolucoes_df.to_string())
    #devolucoes_colunas_para_excluir = ['CNPJ Prestador', 'Nota Referenciada', 'Pagamentos', 'Valor Líquido', 'Centro de Custo', 'Descrição']
    #devolucoes = unificada_aba_devolucoes_v2_df.drop(columns=devolucoes_colunas_para_excluir)


    devolucoes = unificada_aba_devolucoes_v2_df.rename(columns={'Valor Bruto': 'Valor'})
    #print(devolucoes.to_string())

    devolucoes = devolucoes[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'Natureza Da OP.', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
    devolucoes['Valor'] = pd.to_numeric(devolucoes['Valor'], errors='coerce')
    devolucoes['Valor'] = devolucoes['Valor'].round(2)
    #caucao['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

    # Obtém o carimbo de data/hora atual

    writer = pd.ExcelWriter(caminho_unificada_baixar_concat, engine='xlsxwriter')
    notas.to_excel(writer, sheet_name='Notas')
    impostos.to_excel(writer, sheet_name='Impostos Retidos')
    caucao.to_excel(writer, sheet_name='Retenções Contratuais')
    devolucoes.to_excel(writer, sheet_name='Devoluções')
    writer.close()
    janela.destroy()
    messagebox.showinfo('Gerador de Cargas', 'Arquivo gerado com sucesso! Agora é só copiar do arquivo gerado em excel para a Carga!')
    
janela = tk.Tk()
janela.title('Gerador de Cargas')
#janela.geometry('300x90')

btn_selecionar = tk.Button(janela, text="Selecionar unificada", command=selecionar_arquivo)
btn_selecionar.pack(padx=10, pady=(10, 5))

btn_baixar_unificada = tk.Button(janela, text="Baixar Carga", command=selecionar_pasta_baixar)
btn_baixar_unificada["state"] = tk.DISABLED
btn_baixar_unificada.pack(padx=(10), pady=(5, 10))

janela.mainloop()


#implementar depois
# quero que crie um campo que quando a pessoa selecione o arquivo (deixar pra selecionar só em excel), ficar escrito no campo o caminho. e que a pessoa consiga baixar tambem só adicionando no campo o caminho.