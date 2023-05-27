from twilio.rest import Client
import pandas as pd

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values [0]
        print(f'Vendedor com mais 55000 encontrado. \nMês: {mes} \nVendedor: {vendedor} com {vendas} vendas')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+15558675309",
            from_="+15017250604",
            body=f'Vendedor com mais 55000 encontrado. \nMês: {mes} \nVendedor: {vendedor} com {vendas} vendas')
        print(message.sid)


