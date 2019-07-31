Title: Estatística Descritiva com Python (Parte 1)
Date: 2019-05-23 00:00
Modified: 2019-05-23 00:00
Category: Tutoriais
Tags: Python, Estatística
Slug: estatistica-descritiva-com-python
Author: hugo
Summary: Aplicação dos conceitos mais básicos de Estatística Descritiva utilizando a linguagem Python e os pacotes Pandas e Matplotlib.
Cover: assets/img/post-2/giphy.webp

A Estatística pode ser definida de forma simplificada e resumida, como: uma subárea da Matemática que busca estudar, descrever, interpretar e organizar a informação, através da coleta, descrição e análise de dados.

Assim, obviamente, a Estatística é considerada um dos pilares fundamentais em Data Science, juntamente com a parte de Tecnologia e Negócios.

Neste post, vamos ver e aplicar através da linguagem Python alguns dos conceitos mais básicos da Estatística Descritiva, uma das subdivisões da Estatística, responsável principalmente pelo resumo e descrição da informação.

Para isso, vamos utilizar alguns dos principais pacotes open-source e gratuitos voltados à análise de dados que compõem a **Toolbox de um Data Scientist**. São eles: Pandas e Matplotlib.

Também utilizaremos para aplicar os conceitos o Dataset da famosa [Competição do Titanic](https://www.kaggle.com/c/titanic) no Kaggle (Titanic: Machine Learning from Disaster).

Para auxiliar na estrutura do post, vou estar me baseando no excelente livro Estatística Básica, do professor adjunto da Escola de Administração de Empresas da FGV, Wilton Bussab, e do professor titular do Instituto de Matemática e Estatística da Universidade de São Paulo (IME), Pedro Morettin. Todas as demais referências, links e materiais estarão ao final do post.

Então chega de conversa. Vamos lá!

## Preparação dos Pacotes e Dataset

Antes de começar qualquer coisa, precisamos importar os pacotes que utilizaremos, que serão:

- Pandas. Pandas é um poderoso pacote de análise de dados com linguagem Python, ele permite, por exemplo, que trabalhemos facilmente com Dataframes, consigamos informações estatísticas das nossas variáveis e até mesmo plotar gráficos.

- Matplotlib. O Matplotlib é uma das principais bibliotecas para plotar gráficos em Python, com ele é possível, por exemplo, plotar gráficos de linha, barra, setor, histogramas e até graficos em 3D.


```python
import pandas as pd
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

Vamos obter a *distribuição de frequências* da variável Sex, que se refere ao sexo da tripulação do Titanic.

Podemos obter a *distribuição de frequências* de uma variável com Pandas, podemos simplesmente utilizar o método `.value_counts()`. Também utilizaremos a função `pd.DataFrame()` para termos uma melhor visualização dos resultados através de tabelas.


```python
pd.DataFrame(df['Sex'].value_counts())
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
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>male</th>
      <td>577</td>
    </tr>
    <tr>
      <th>female</th>
      <td>314</td>
    </tr>
  </tbody>
</table>
</div>



Usando apenas o método `.value_counts()`sem nenhum parâmetro, conseguimos obter a frequência de cada atributo da variável, ou seja, a *distribuição de frequências absoluta*. Se quisermos saber qual a *distribuição de frequências relativa*, isto é, quanto cada atributo representa no total de registros da variável, podemos passar o parâmetro `.value_counts(normalize=True)`


```python
pd.DataFrame(df['Sex'].value_counts(normalize=True))
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
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>male</th>
      <td>0.647587</td>
    </tr>
    <tr>
      <th>female</th>
      <td>0.352413</td>
    </tr>
  </tbody>
</table>
</div>



Uma outra forma de olhar para a distribuição de frequências de uma variável, é através da *distribuição de frequências acumulada*. A *distribuição de frequências acumulada* indica quantos elementos ou que percentual deles estão abaixo de determiado valor. Para isso, podemos aplicar o método `.cumsum()` do Pandas juntamente com o `.value_counts()`, para que ele retorne uma série cumulativa das frequências.


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



Para obtermos a *distribuição de frequências acumulada relativa*, como já fizemos, basta adicionar o parâmetro `normalize=True`no método `.value_counts(normalize=True)`


```python
pd.DataFrame(df['Pclass'].value_counts(normalize=True, sort=False).cumsum())
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
      <td>0.242424</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.448934</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



- **Gráficos para Variáveis Qualitativas: Gráficos de Barras e de Setores(Pizza)**

Há muitos tipos de gráficos e muitas formas diferentes de visualizar dados. Contudo, temos alguns que são mais comuns e mais utilizados.

Quando estamos analisando uma variável qualitativa, os *Gráficos de Barras* e de *Composição de Setores* são alguns destes mais conhecidos. Em nosso dataset, temos algumas variáveis qualitativas que podemos visualizar através destes gráficos, como por exemplo a variável Sex(que se refere ao Sexo da tripulação) e a Embarked(que se refere ao portão de embarque).

Vamos visualizar a distribuição de frequências da variável Sex novamente.


```python
pd.DataFrame(df['Sex'].value_counts())
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
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>male</th>
      <td>577</td>
    </tr>
    <tr>
      <th>female</th>
      <td>314</td>
    </tr>
  </tbody>
</table>
</div>



Se quisessemos visualizar essa distribuição em um gráfico de barras, podemos utilizar os gráficos do pacote Matplotlib pra fazer isso.

O Matplotlib possui uma variedade imensa de gráficos que podem ser usados. No caso do gráfico de barras, podemos plotá-lo através da função `plt.bar()`, onde precisamos passar pelo menos dois parâmetros com os eixos X e Y consecutivamente.

Vamos criar duas variáveis, uma chamada **sexo** e outra **frequencia**. A variável sexo irá conter o index do dataframe de distribuição de frequências que fizemos acima, o index do dataframe, neste caso, se refere aos próprios valores da variável. Enquanto que os valores do dataframe são as frequências de cada valor e serão armazenados na variável frequencia.

Assim, podemos adicionar os métodos `.index` e `.values` à distribuição de frequência da variável Sex obtida com `df['Sex'].value_counts()` para recebermos dois arrays com os valores e a quantidade de vezes que eles aparecem na variável,


```python
sexo = df['Sex'].value_counts().index
frequencia = df['Sex'].value_counts().values
sexo, frequencia
```




    (Index(['male', 'female'], dtype='object'), array([577, 314], dtype=int64))



Pronto! Agora podemos utilizar a função `plt.bar()` do Matplotlib e adicionar os parâmetros dos eixos X e Y com as variáveis sexo e frequencia. Vamos utilizar também a função `plt.show()` para visualizamos a figura do gráfico no modo display.


```python
plt.bar(sexo, frequencia)
plt.show()
```


![png]({static}/assets/img/post-2/output_19_0.png)


Ótimo! Nós também podemos customizar os gráficos, e como boa prática, é bom que adicionemos pelo menos um título e o nome dos eixos. Para isso, vamos utilizar as funções `plt.title()` para o título, `plt.xlabel()` para o eixo X e `plt.ylabel()` para o eixo Y. É bem simples, basta passarmos uma string dentro a função para plotarmos um novo gráfico com estas informações.


```python
plt.title("Distribuição de Frequências da Variável Sex")
plt.xlabel("Sexo")
plt.ylabel("Frequência")
plt.bar(sexo, frequencia)
plt.show()
```


![png]({static}/assets/img/post-2/output_21_0.png)


Excelente! Conseguimos plotar o nosso primeiro gráfico de barras com a distribuição de frequências de uma variável. Vamos tentar obter agora a *distribuição de frequências relativa* da variável Sex, porém, visualizada em um gráfico de setores(pizza).

Podemos fazemos isso utilizando a função `plt.pie()`. Como já fizemos anteriormente, precisamos passar alguns parâmetros nesta função para plotarmos o gráfico. Aqui vamos precisar de pelo menos três parâmetros para termos as principais informações, a frequência relativa, o label de cada setor e o percentual que os valores representam na variável.

Estes parâmetros serão `x=frequencia` com a variável frequencia preenchendo o parâmetro, `labels=sexo` com a variável sexo preenchendo o parâmetro necessário para plotarmos os valores da variável no label de cada setor e o parâmetro `autopct='%2.2f%%'`com a string `'%2.2f%%'`, essa string se refere ao formato em que o valor com o percentual de cada setor tem na variável é apresentado, neste caso, estaremos usando um formato com valores flutuantes do tipo: 'aa.aa%'.

Não podemos esquecer de colocar o título e nomes dos eixos X e Y, além da função `plt.show()` para o modo display.


```python
plt.pie(x=frequencia, labels=sexo, autopct='%2.2f%%')
plt.title('Distribuição de Frequências Relativa da Variável Sex')
plt.xlabel('Sexo')
plt.ylabel('Frequência Relativa')
plt.show()
```


![png]({static}/assets/img/post-2/output_23_0.png)


- **Gráficos para Variáveis Quantitativas: Histogramas**


```python
plt.hist(df['Age'][df['Age'].notna()], bins='auto')
plt.grid(True)
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
```


![png]({static}/assets/img/post-2/output_25_0.png)



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
    - Variância
    - Desvio Padrão


```python

```

## Referências
- Estatística Básica - Bussab & Morettin

- https://www.kaggle.com/c/titanic

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
