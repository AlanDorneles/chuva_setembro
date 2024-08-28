import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Lendo dados da chuva de São Lourenço (CEMADEN)
base_de_dados_sao_lou = pd.read_csv('./sao_lou.csv', sep=';')
base_de_dados_sao_lou['valorMedida'] = base_de_dados_sao_lou['valorMedida'].str.replace(',', '.').astype(float) # Troca , por . no valor de chuva
base_de_dados_sao_lou['datahora'] = pd.to_datetime(base_de_dados_sao_lou['datahora']).dt.date # Captando somente a data
base_de_dados_sao_lou['datahora'] = base_de_dados_sao_lou['datahora'].apply(lambda x: x.strftime('%d-%m-%Y')) 
soma_por_data_sao_lou = base_de_dados_sao_lou.groupby('datahora')['valorMedida'].sum().reset_index() # Soma a chuva da estação por dia
print(soma_por_data_sao_lou['valorMedida'].sum())
"""
# Lendo dados da chuva de Rio Grande (INMET A802)
base_de_dados_rg = pd.read_csv('./rio_grande.csv', sep=';')
base_de_dados_rg['Chuva (mm)'] = base_de_dados_rg['Chuva (mm)'].str.replace(',', '.').astype(float) # Troca , por . no valor de chuva
base_de_dados_rg['Data'] = pd.to_datetime(base_de_dados_rg['Data'], format='%d/%m/%Y').dt.date # Captando somente a data e deixando no formato dd/MM/YYYY
base_de_dados_rg['Data'] = base_de_dados_rg['Data'].apply(lambda x: x.strftime('%d-%m-%Y')) 
soma_por_data_rg = base_de_dados_rg.groupby('Data')['Chuva (mm)'].sum().reset_index() # Soma a chuva da estação por dia
print(soma_por_data_rg)

# Fenômenos meteorológicos
fenomeno_rg = pd.Series(['ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD', 'CCM', 'CCM', 'ESTABILIDAD', 'ESTABILIDAD','FRENTE FRIA', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'CICLONE', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA','FRENTE FRIA', 'ESTABILIDAD', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD']) 

fenomeno_slou = pd.Series(['ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD', 'CCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD','ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'CICLONE', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD','FRENTE FRIA', 'FRENTE FRIA', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'SCM', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD']) 

# Cores para cada fenômeno
color_map = {
    'CCM': '#FF5733',              # Cor para CCM    # Cor para Estabilidade
    'FRENTE FRIA': 'purple',  # Cor para Sistema Frontal
    'FRENTE ESTACIONÁRIA': 'green', # Cor para Frente Estacionária
    'SCM': '#BE7C4D',  # Cor para Célula Convectiva
    'CICLONE': '#1ABC9C',      # Cor para Frente Fria
}


# Configuração do gráfico
plt.figure(figsize=(14, 7))
plt.plot(soma_por_data_rg['Data'], soma_por_data_rg['Chuva (mm)'], label='Rio Grande', color='#FBDE4D', linewidth=4, zorder=1) # Série RG
plt.plot(soma_por_data_sao_lou['datahora'], soma_por_data_sao_lou['valorMedida'], label='São Lourenço do Sul', color='#373B93', linewidth=3) #SERIE SLOU

# Plotar os marcadores com cores alternadas
for tipo, color in color_map.items():
    subset_rg = soma_por_data_rg[fenomeno_rg == tipo]  # Filtra os dados para o fenômeno
    plt.scatter(subset_rg['Data'], subset_rg['Chuva (mm)'], marker='o', color=color, label=f'{tipo}', zorder=2, s=100) # Marcadores RG
    subset_slou = soma_por_data_sao_lou[fenomeno_slou == tipo]  # Filtra os dados para o fenômeno
    plt.scatter(subset_slou['datahora'], subset_slou['valorMedida'], marker='o', color=color, zorder=2, s=100) # Marcadores SLOU

plt.axhline(y=5, color='gray', linestyle='--', linewidth=2, label='Limiar (5mm)')
# Configurar formato dos ticks
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))  # Ajustar frequência dos ticks

# Adicionar a legenda
plt.legend(loc='upper left', title='Legenda') # Legenda
plt.grid(True)
plt.gca().spines['top'].set_visible(False) # Retirando a linha superior da caixa do gráfico
plt.gca().spines['right'].set_visible(False) # Retirando a linha direita da caixa do gráfico
plt.xlabel('Data') # Rótulo do eixo X 
plt.ylabel('Chuva (mm)') # Rótulo do eixo Y
#plt.ylim(1, soma_por_data_rg['Chuva (mm)'].max().max() + 1)
plt.title('Chuva Diária em Rio Grande e São Lourenço do Sul e seus fenômenos meteorológicos associados a precipitação') 
plt.subplots_adjust(bottom=0.2)  
current_labels = plt.gca().get_xticks()  # Obtém as posições dos rótulos
new_labels = current_labels[:-1]  # Remove o último rótulo
plt.gca().set_xticks(new_labels)
plt.xticks(rotation=0) 
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()



plt.plot(soma_por_data_sao_lou['datahora'], soma_por_data_sao_lou['valorMedida'], label='São Lourenço do Sul', color='#FBDE4D', linewidth=3) #SERIE SLOU


for tipo, color in color_map.items():
    subset_slou = soma_por_data_sao_lou[fenomeno_slou == tipo]  # Filtra os dados para o fenômeno
    plt.scatter(subset_slou['datahora'], subset_slou['valorMedida'], marker='o', color=color, label=f'{tipo}', zorder=2,s=100) # Marcadores RG

# Configurar formato dos ticks
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))  # Ajustar frequência dos ticks
#plt.ylim(1, soma_por_data_sao_lou['valorMedida'].max().max() + 1)
# Adicionar a legenda
plt.legend(loc='upper left', title='Legenda') # Legenda
plt.gca().spines['top'].set_visible(False) # Retirando a linha superior da caixa do gráfico
plt.gca().spines['right'].set_visible(False) # Retirando a linha direita da caixa do gráfico
plt.xlabel('Data') # Rótulo do eixo X 
plt.ylabel('Chuva (mm)') # Rótulo do eixo Y
plt.title('Chuva Diária em São Lourenço do Sul e seus fenômenos meteorológicos associados a precipitação') 
plt.subplots_adjust(bottom=0.2)  
current_labels = plt.gca().get_xticks()  # Obtém as posições dos rótulos
new_labels = current_labels[:-1]  # Remove o último rótulo
plt.gca().set_xticks(new_labels)
plt.xticks(rotation=0) 
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()"""