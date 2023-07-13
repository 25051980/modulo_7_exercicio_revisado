#!/usr/bin/env python
# coding: utf-8

# <img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">
# 
# ---
# 
# # **Módulo 07** | Python: Programação Orientada a Objetos
# Caderno de **Exercícios**<br> 
# Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)
# 
# ---

# # **Tópicos**
# 
# <ol type="1">
#   <li>from / import / as;</li>
#   <li>Módulo;</li>
#   <li>Pacote;</li>
#   <li>Baixando pacotes.</li>
# </ol>

# ---

# # **Exercícios**

# ## 0\. Preparação do ambiente

# Neste exercício vamos utilizar a base de dados de ações da bolsa de valores dos EUA, a Dow Jones. Os dados estão disponíveis para *download* neste [link](https://archive.ics.uci.edu/ml/datasets/Dow+Jones+Index). Vamos utilizar o pacote `wget` para fazer o *download* dos dados.

#  - Instalando o pacote `wget` na versão 3.2.

# In[1]:


get_ipython().system('pip install wget==3.2')


#  - Fazendo o download dos dados no arquivo compactado `dados.zip`.

# In[2]:


import wget

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')


#  - Descompactando os `dados` na pasta dados com o pacote nativo `zipfile`.

# In[3]:


import zipfile

with zipfile.ZipFile('./dados.zip', 'r') as fp:
  fp.extractall('./dados')


# Verifique a pasta dados criada, ela deve conter dois arquivos:
# 
#  - **dow_jones_index.data**: um arquivo com os dados;
#  - **dow_jones_index.names**: um arquivo com a descrição completa dos dados.
# 
# É possível observar que o arquivo de dados é um arquivo separado por virgulas, o famoso `csv`. Vamos renomear o arquivo de dados para que ele tenha a extensão `csv` com o pacote nativo `os`.

# - Renomeando o arquivo com o pacote nativo `os`.

# In[4]:


import os

os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')


# Pronto! Abra o arquivo e o Google Colab irá apresentar uma visualização bem legal dos dados.

# ---

# ## 1\. Pandas

# Para processar os dados, vamos utilizar o pacote `pandas` na versão `1.1.5`. A documentação completa por ser encontrada neste [link](https://pandas.pydata.org/docs/)

# In[5]:


get_ipython().system('pip install pandas==1.1.5')


# Vamos importar o pacote com o apelido (alias) `pd`.

# In[6]:


import pandas as pd


# Estamos prontos para ler o arquivo.

# In[7]:


df = pd.read_csv('./dados/dow_jones_index.csv')


# O pandas trabalha com o conceito de dataframe, uma estrutura de dados com muitos métodos e atributos que aceleram o processamento de dados. Alguns exemplos:

#  - Visualizando as `n` primeiras linhas:

# In[8]:


df.head(n=10)


#  - Visualizando o nome das colunas:

# In[9]:


df.columns.to_list()


#  - Verificando o número de linhas e colunas.

# In[10]:


linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')


# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações do McDonalds, listado na Dow Jones como MCD:

#  - Selecionando as linha do dataframe original `df` em que a coluna `stock` é igual a `MCD`.

# In[11]:


df_mcd = df[df['stock'] == 'MCD']


#  - Selecionando apenas as colunas de data e valores de ações.

# In[12]:


df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]


# Excelente, o problema é que as colunas com os valores possuem o carater `$` e são do tipo texto (`object` no `pandas`).

# In[13]:


df_mcd.head(n=10)


# In[14]:


df_mcd.dtypes


# Vamos limpar as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` remove o caracter **$** e faz a conversão do tipo de `str` para `float`.

# In[15]:


for col in ['open', 'high', 'low', 'close']:
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))


# Verifique novamente os dados e seus tipos.

# In[16]:


df_mcd.head(n=10)


# In[17]:


df_mcd.dtypes


# Excelente, agora podemos explorar os dados visualmente.

# **Agora é a sua vez!** Conduza o mesmo processo para extrair e tratar os dados da empresa Coca-Cola (`stock` column igual a `KO`).

#  - Selecionando as linha do dataframe original `df` em que a coluna `stock` é igual a `KO`.

# In[30]:


# extração e tratamento dos dados da empresa Coca-Cola.
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./dados/dow_jones_index.csv')

# Selecionar as linhas com stock igual a KO
coca_cola_df = df.loc[df['stock'] == 'KO']

# Imprimir as linhas selecionadas
print(coca_cola_df)


# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações da empresa Coca-Cola, listado na Dow Jones como KO:

#  - Selecionando apenas as colunas de data e valores de ações.

# In[31]:


import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./dados/dow_jones_index.csv')

# Filtrar as colunas desejadas
coca_cola_df = df.loc[df['stock'] == 'KO', ['date', 'open', 'close', 'high', 'low']]

# Imprimir as colunas selecionadas
print(coca_cola_df)


# Excelente, o problema é que as colunas com os valores possuem o carater `$` e são do tipo texto (`object` no `pandas`).

# In[32]:


# Visualize os dados do dataframe
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./dados/dow_jones_index.csv')

# Filtrar as colunas desejadas
coca_cola_df = df.loc[df['stock'] == 'KO', ['date', 'open', 'close', 'high', 'low']]

# Visualizar os dados
print(coca_cola_df.head())


# In[33]:


# Verifique o tipo dos dados
print(coca_cola_df.dtypes)


# Vamos limpar as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` remove o caracter **$** e faz a conversão do tipo de `str` para `float`.

# In[34]:


coca_cola_df['open'] = coca_cola_df['open'].apply(lambda x: float(x.replace('$', '')))
coca_cola_df['close'] = coca_cola_df['close'].apply(lambda x: float(x.replace('$', '')))
coca_cola_df['high'] = coca_cola_df['high'].apply(lambda x: float(x.replace('$', '')))
coca_cola_df['low'] = coca_cola_df['low'].apply(lambda x: float(x.replace('$', '')))


# Verifique novamente os dados e seus tipos.

# In[35]:


# Visualize novamente os dados do dataframe
print(coca_cola_df)


# In[36]:


# Verifique novamente o tipo dos dados
print(coca_cola_df.dtypes)


# Excelente, agora podemos explorar os dados visualmente.

# ---

# ## 2\. Seaborn

# Para visualizar os dados, vamos utilizar o pacote `seaborn` na versão `0.11.1`. A documentação completa por ser encontrada neste [link](https://seaborn.pydata.org/)

# In[23]:


get_ipython().system('pip install seaborn==0.11.1')


# Vamos importar o pacote com o apelido (alias) `sns`.

# In[37]:


import seaborn as sns


# Vamos visualizar os valores de abertura das ações ao longo do tempo.

# In[25]:


plot = sns.lineplot(x="date", y="open", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)


# Vamos também visualizar os valores de fechamento das ações ao longo do tempo.

# In[26]:


plot = sns.lineplot(x="date", y="close", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)


# Para facilitar a comparação, vamo visualizar os quatro valores no mesmo gráfico.

# In[38]:


plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_mcd, ['date']))
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)


# Para finalizar, vamos salvar o gráfico numa figura.

# In[39]:


plot.figure.savefig("./mcd.png")


# **Agora é a sua vez,** faça o gráfico acima para a empresa Coca-Cola e salve a imagem com o nome `ko.png`.

# In[40]:


# visualização dos dados da Coca-Cola.
import matplotlib.pyplot as plt

# Criar o gráfico
plt.plot(coca_cola_df['date'], coca_cola_df['close'])

# Configurar os rótulos dos eixos
plt.xlabel('Data')
plt.ylabel('Valor de Fechamento')

# Título do gráfico
plt.title('Valores de Fechamento da Coca-Cola (KO)')

# Salvar o gráfico como uma imagem
plt.savefig('ko.png')

# Mostrar o gráfico
plt.show()


# Vamos visualizar os valores de abertura das ações ao longo do tempo.

# In[41]:


import matplotlib.pyplot as plt

# Criar o gráfico
plt.plot(coca_cola_df['date'], coca_cola_df['open'])

# Configurar os rótulos dos eixos
plt.xlabel('Data')
plt.ylabel('Valor de Abertura')

# Título do gráfico
plt.title('Valores de Abertura das Ações da Coca-Cola (KO)')

# Mostrar o gráfico
plt.show()


# Vamos também visualizar os valores de fechamento das ações ao longo do tempo.

# In[42]:


import matplotlib.pyplot as plt

# Criar o gráfico
plt.plot(coca_cola_df['date'], coca_cola_df['close'])

# Configurar os rótulos dos eixos
plt.xlabel('Data')
plt.ylabel('Valor de Fechamento')

# Título do gráfico
plt.title('Valores de Fechamento das Ações da Coca-Cola (KO)')

# Mostrar o gráfico
plt.show()


# Para facilitar a comparação, vamo visualizar os quatro valores no mesmo gráfico.

# In[43]:


import matplotlib.pyplot as plt

# Criar o gráfico
plt.plot(coca_cola_df['date'], coca_cola_df['open'], label='Abertura')
plt.plot(coca_cola_df['date'], coca_cola_df['close'], label='Fechamento')
plt.plot(coca_cola_df['date'], coca_cola_df['high'], label='Máximo')
plt.plot(coca_cola_df['date'], coca_cola_df['low'], label='Mínimo')

# Configurar os rótulos dos eixos
plt.xlabel('Data')
plt.ylabel('Valor das Ações')
plt.title('Valores das Ações da Coca-Cola (KO)')

# Adicionar legenda
plt.legend()

# Mostrar o gráfico
plt.show()


# Para finalizar, vamos salvar o gráfico numa figura.

# In[44]:


plt.savefig('ko.png')


# Analise as duas imagens e escreva pelo menos um *insight* que você consegue extrair dos dados. Fique a vontade para escrever quantos *insights* você quiser.

# Obs: *Insights* são observações sobre o que você percebe/entende/interpreta em suas análises. No caso deste exercício, você vai analisar os dados dos gráficos da empresa McDonalds e da empresa Cola-Cola e notar o que os dados gerados podem ser interessante, que tipo de interpretação o comportamento dos dados estão te trazendo.

# Insight 

# Tendência de crescimento: Podemos observar uma tendência geral de crescimento nos valores de abertura e fechamento das ações da Coca-Cola ao longo do tempo. Isso indica um desempenho positivo da empresa no mercado financeiro.
# 
# Flutuações diárias: Podemos observar que existem flutuações diárias nos valores de abertura e fechamento das ações. Isso indica a influência de fatores externos, como notícias, eventos econômicos e mudanças nas condições de mercado, que afetam o preço das ações em curto prazo.
# 
# Sazonalidade: Podemos identificar possíveis padrões sazonais nos valores das ações da Coca-Cola ao longo do tempo. Por exemplo, podem existir períodos de maior demanda e valorização durante certas épocas do ano, como feriados e estações específicas.
# 
# Relação entre abertura e fechamento: Podemos analisar a relação entre os valores de abertura e fechamento das ações. Se os valores de fechamento estiverem consistentemente acima dos valores de abertura, isso indica um desempenho positivo das ações no período considerado.

# ---
