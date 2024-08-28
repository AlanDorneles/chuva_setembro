import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as mlines

base_de_dados_sao_lou= pd.read_csv('./sao_lou.csv', sep=';')
base_de_dados_sao_lou['valorMedida'] = base_de_dados_sao_lou['valorMedida'].str.replace(',', '.').astype(float)
base_de_dados_sao_lou['datahora'] = pd.to_datetime(base_de_dados_sao_lou['datahora']).dt.date
soma_por_data_sao_lou = base_de_dados_sao_lou.groupby('datahora')['valorMedida'].sum().reset_index()
#print(soma_por_data_sao_lou)

base_de_dados_rg= pd.read_csv('./rio_grande.csv', sep=';')
base_de_dados_rg['Chuva (mm)'] = base_de_dados_rg['Chuva (mm)'].str.replace(',', '.').astype(float)
soma_por_data_rg = base_de_dados_rg.groupby('Data')['Chuva (mm)'].sum().reset_index()
base_de_dados_rg['Data'] = pd.to_datetime(base_de_dados_rg['Data'], format='%d/%m/%Y').dt.date
soma_por_data_rg = base_de_dados_rg.groupby('Data')['Chuva (mm)'].sum().reset_index()
#print(soma_por_data_rg)

fenomeno_rg = pd.Series(['A', 'B', 'C', 'B', 'C', 'B', 'A', 'D', 'A', 'D','A', 'B', 'C', 'B', 'C', 'B', 'A', 'D', 'A', 'D','A', 'B', 'C', 'B', 'C', 'B', 'A', 'D', 'A', 'D'])
fenomenos_slou = pd.Series(['A', 'B', 'C', 'B', 'C', 'B', 'A', 'A', 'D', 'A', 'D','A', 'B', 'C', 'B', 'C', 'B', 'A', 'D', 'A', 'D','A', 'B', 'C', 'B', 'C','C', 'B', 'A', 'D'])


soma_por_data_sao_lou['datahora'] = pd.to_datetime(soma_por_data_sao_lou['datahora'])
soma_por_data_rg['Data'] = pd.to_datetime(soma_por_data_rg['Data'])
marker_line = mlines.Line2D([], [], color='blue', marker='o', markersize=8, linestyle='None', label='Marcador São Lourenço do Sul')
marker_square = mlines.Line2D([], [], color='green', marker='s', markersize=8, linestyle='None', label='Marcador Rio Grande')

print(type(soma_por_data_rg['Chuva (mm)']))

plt.figure(figsize=(10, 6))
plt.plot(soma_por_data_sao_lou['datahora'], soma_por_data_sao_lou['valorMedida'], label='São Lourenço do Sul')
plt.plot(soma_por_data_rg['Data'], soma_por_data_rg['Chuva (mm)'], label='Rio Grande')

plt.legend(handles=[marker_line, marker_square], loc='upper left', title='Marcadores')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.xlabel('Data')
plt.ylabel('Chuva (mm)')
plt.title('Comparação de Chuva Diária entre São Luís e Rio Grande')
plt.xticks(rotation=0)
plt.legend()
plt.show()





