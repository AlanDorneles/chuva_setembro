import pandas as pd
import matplotlib.pyplot as plt


fenomeno_rg = pd.Series(['ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD', 'CCM', 'CCM', 'ESTABILIDAD', 'ESTABILIDAD','FRENTE FRIA', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'CICLONE', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA','FRENTE FRIA', 'ESTABILIDAD', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD']) 

fenomeno_slou = pd.Series(['ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD', 'CCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD','ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'FRENTE ESTACIONÁRIA', 'CICLONE', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD', 'FRENTE ESTACIONÁRIA', 'ESTABILIDAD', 'ESTABILIDAD','FRENTE FRIA', 'FRENTE FRIA', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'SCM', 'SCM', 'ESTABILIDAD', 'ESTABILIDAD', 'ESTABILIDAD']) 


quant_eventos_rg = fenomeno_rg.value_counts()
quant_eventos_slou = fenomeno_slou.value_counts()
#print("EVENTOS RG:" , quant_eventos_rg['ESTABILIDADE'])
#print("EVENTOS SLOU:", quant_eventos_slou['ESTABILIDADE'])

# Unindo as contagens em um DataFrame
eventos = pd.DataFrame({
    'Rio Grande': quant_eventos_rg,
    'São Lourenço do Sul': quant_eventos_slou
}).fillna(0).drop('ESTABILIDAD')  # Preenche com 0 onde não há eventos
cores = ['#FBDE4D', '#373B93']

# Configurações do gráfico
ax = eventos.plot(kind='bar', figsize=(14, 7), color=cores)
# Configurações dos rótulos e título
plt.title('Comparação de Eventos Meteorológicos entre Rio Grande e São Lourenço do Sul')
plt.gca().spines['top'].set_visible(False) # Retirando a linha superior da caixa do gráfico
plt.gca().spines['right'].set_visible(False) # Retirando a linha direita da caixa do gráfico
plt.xlabel('Evento meteorológicos')
plt.ylabel('Quantidade de eventos')
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo X para melhor legibilidade
plt.legend(title='Cidade')

# Mostrar o gráfico
plt.tight_layout()
plt.show()