Title: Estatística Descritiva com Python
Date: 2019-05-23 00:00
Modified: 2019-05-23 00:00
Category: Tutoriais
Tags: Python, Estatística
Slug: estatistica-descritiva-com-python
Author: hugo
Summary: Aplicação dos conceitos mais básicos de Estatística Descritiva utilizando a linguagem Python e os pacotes Pandas, Numpy e Matplotlib.
Cover: assets/img/post-2/giphy.webp

A Estatística pode ser definida de forma simplificada e resumida, como: uma subárea da Matemática que busca estudar, descrever, interpretar e organizar a informação, através da coleta, descrição e análise de dados.

Assim, obviamente, a Estatística é considerada um dos pilares fundamentais em Data Science, juntamente com a parte de Tecnologia e Negócios.

Neste post, vamos ver e aplicar através da linguagem Python alguns dos conceitos mais básicos da Estatística Descritiva, uma das subdivisões da Estatística, responsável principalmente pelo resumo e descrição da informação.

Para isso, vamos utilizar alguns dos principais pacotes open-source e gratuitos voltados à análise de dados que compõem a **Toolbox de um Data Scientist**. São eles: Pandas, Numpy e Matplotlib.

Também utilizaremos para aplicar os conceitos o Dataset da famosa [Competição do Titanic](https://www.kaggle.com/c/titanic) no Kaggle (Titanic: Machine Learning from Disaster).

Para auxiliar na estrutura do post, vou estar me baseando no excelente livro Estatística Básica, do professor adjunto da Escola de Administração de Empresas da FGV, Wilton Bussab, e do professor titular do Instituto de Matemática e Estatística da Universidade de São Paulo (IME), Pedro Morettin. Todas as demais referências, links e materiais estarão ao final do post.

Então chega de conversa. Vamos lá!

## Preparação dos Pacotes e Dataset

Antes de começar qualquer coisa, precisamos importar os pacotes que utilizaremos, que serão:

- Pandas. Pandas é um poderoso pacote de análise de dados com linguagem Python, ele permite, por exemplo, que trabalhemos facilmente com Dataframes, consigamos informações estatísticas das nossas variáveis e até mesmo plotar gráficos.

- Numpy. O Numpy é um pacote voltado para computação científica com Python, possui um objeto array N-dimensional que facilita a manipulação de matrizes, sendo fundamental para a Álgebra Linear.

- Matplotlib. O Matplotlib é uma das principais bibliotecas para plotar gráficos em Python, com ele é possível, por exemplo, plotar gráficos de linha, barra, setor, histogramas e até graficos em 3D.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# O comando abaixo é um comando específico do Jupyter Notebook, ele é utilizado para que o Matplotlib não abra uma nova página para plotar os gráficos e plote no output da célula.
%matplotlib inline
```

Agora que já importamos os pacotes, vamos usar a função `pd.read_csv()` do Pandas para importar o Dataset da Competição do Titanic e salvá-lo na variável `df`. Apenas o arquivo "train.csv" de teste já é suficiente para o que precisamos.

Após isso, vamos utilizar o método `.head()` para visualizar os cinco primeiros registros do nosso Dataframe.


```python
df = pd.read_csv('train.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## Resumo de Dados

- **Distribuição de Frequências**

Bom, quando falamos de Estatística Descritiva, estamos buscando compreender melhor o comportamento das variáveis com que estamos trabalhando. Um dos conceitos mais básicos empregado nesta tarefa é a noção de ***Distribuição de Frequências,*** que procura resumir o comportamento de uma variável pela contabilização da frequência dos atributos contidos nela.

Vamos obter a *distribuição de frequências* das variáveis Pclass, que se refere a classe socioeconômica da tripulação do Titanic, e Survived, que indica quem sobreviveu ou não ao naufrágio.

Podemos obter a *distribuição de frequências* de uma variável tanto com Pandas quanto Numpy. Com Pandas, podemos simplesmente utilizar o método `.value_counts()`


```python
df['Pclass'].value_counts()
```




    3    491
    1    216
    2    184
    Name: Pclass, dtype: int64




```python
pd.DataFrame(df['Pclass'].value_counts())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>491</td>
    </tr>
    <tr>
      <th>1</th>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(df['Survived'].value_counts())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>549</td>
    </tr>
    <tr>
      <th>1</th>
      <td>342</td>
    </tr>
  </tbody>
</table>
</div>



Usando apenas o método `.value_counts()`sem nenhum parâmetro, conseguimos obter a frequência de cada atributo da variável, ou seja, a *distribuição de frequência absoluta*. Se quisermos saber qual a *distribuição de frequência relativa*, isto é, quanto cada atributo representa no total de registros da variável, podemos passar o parâmetro `.value_counts(normalize=True)`


```python
pd.DataFrame(df['Pclass'].value_counts(normalize=True))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>0.551066</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.242424</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.206510</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(df['Survived'].value_counts(normalize=True))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.616162</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.383838</td>
    </tr>
  </tbody>
</table>
</div>



Também podemos obter a *distribuição de frequências*, absoluta e relativa de uma variável, usando o Numpy.


```python
np.unique(df['Pclass'], return_counts=True)
```




    (array([1, 2, 3], dtype=int64), array([216, 184, 491], dtype=int64))




```python
values, freq = np.unique(df['Pclass'], return_counts=True)
pd.DataFrame({'Pclass': freq}, index=values)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184</td>
    </tr>
    <tr>
      <th>3</th>
      <td>491</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.unique(df['Survived'], return_counts=True)
```




    (array([0, 1], dtype=int64), array([549, 342], dtype=int64))




```python
values, freq = np.unique(df['Survived'], return_counts=True)
pd.DataFrame({'Survived': freq/df['Survived'].size}, index=values)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.616162</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.383838</td>
    </tr>
  </tbody>
</table>
</div>



Também podemos obter a *distribuição de frequências acumulada* utilizando o método `.cumsum()` com Pandas, e a função, de mesmo nome, `np.cumsum()` com Numpy.


```python
pd.DataFrame(df['Pclass'].value_counts(sort=False).cumsum())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>891</td>
    </tr>
  </tbody>
</table>
</div>




```python
values, freq = np.unique(df['Pclass'], return_counts=True)
pd.DataFrame({'Pclass': np.cumsum(freq)}, index=values)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>891</td>
    </tr>
  </tbody>
</table>
</div>



- **Histogramas**


```python
plt.hist(df['Age'][df['Age'].notna()], bins='auto')
plt.grid(True)
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
```


![png]({static}/assets/img/post-2/output_22_0.png)



```python
(min(df['Age']), max(df['Age']))
```




    (0.42, 80.0)




```python

```

## Medidas Resumo

- **Medidas de Posição**
    - Moda
    - Mediana
    - Média

- **Medidas de Dispersão**


```python

```

## Referências
- Estatística Básica - Bussab & Morettin

- https://www.kaggle.com/c/titanic


```python

```

___

# ROTEIRO - POST ESTATÍSTICA BÁSICA

## Introdução
- Apresentar o objetivo do post
- Explicar o que é Estatística Descritiva
- Pacotes Usados
- Falar sobre as referências


## Resumo de Dados
#### Distribuição de frequências
- Distribuição de Frequências= .value_counts() pandas
- Frequência acumulada (pg 47)
- Uso de gráficos de barras e setores ("pizza") para resumir a distribuição de frequências para variáveis QUALITATIVAS
- Para variáveis QUANTITATIVAS, além das formas das qualitativas também temos o Histograma

## Medidas - Resumo
#### Medidas de Posição
- Moda
- Mediana
- Média

#### Medidas de Dispersão

___


```python

```


```python

```


```python

```


```python

```
