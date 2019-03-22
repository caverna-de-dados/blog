Title: Como instalar o R no Jupyter Notebook usando o Anaconda
Date: 2019-03-21 22:30
Modified: 2019-03-21 22:30
Category: Python, Jupyter Notebook
Tags: pelican, publishing
Slug: como-instalar-o-r-no-jupyter-notebook-usando-o-anaconda
Authors: hugo
Summary: Saiba como instalar o Setup "R Essentials" no Anaconda e poder usar no Jupyter Notebook, o R, e mais 400 pacotes voltados a essa linguagem.
Cover: assets/img/anaconda.jpg

[Jupyter Notebook](https://jupyter.org/) é uma Aplicação Web Open-Source e uma das principais ferramentas usadas pelos Data Scientists.

Ele permite criar e compartilhar documentos que suportam desde códigos em múltiplas linguagens, como por exemplo, Python, R e Julia, até textos em Markdown, equações em LaTeX e visualizações de gráficos, imagens e vídeos, além de ser facilmente instalável pelo [Anaconda](https://anaconda.org/).

Habitualmente em Data Science, a linguagem Python acaba por ser a mais utilizada no Jupyter, enquanto que o R possui seu próprio software de análises, o [RStudio](https://www.rstudio.com/).

Contudo, é perfeitamente possível instalar setups de outras linguagens no Anaconda e usá-las no Jupyter Notebook. Então, bora lá!



## INSTALANDO O "R ESSENTIALS"

O "R Essentials" é um setup criado pela equipe do Anaconda e que contém mais de 400 pacotes de R, com aproximadamente 80 sendo voltados para Data Science, como dplyr, ggplot2, tidyr, entre outros.

Ao instalar esse setup, é possível fazer o uso da linguagem R no Jupyter Notebook, bem como todos os pacotes vindos com ele.

Antes de instalar o "R Essentials" é necessário prestar **atenção a um pequeno ponto**: você pode instalar o "R Essentials" no seu environment (ambiente) de uso atual ou instalá-lo em um novo environment.

Ao utilizar um novo environment, você terá um novo ambiente apenas para o armazenamento e organização dos pacotes de R, isso pode te ajudar caso no futuro você queria deixar esse ambiente ainda mais robusto e customizado. Ainda assim, não há nenhum problema em usar o mesmo envinroment para os pacotes de Python e R.

Então, no prompt do Anaconda:

Para instalar o "R Essentials" no seu environment atual, utilize o comando:

```
conda install -c r r-essentials 
```


Caso você queira criar um novo environment, basta usar o comando abaixo:

```
conda create -n r_env r-essentials r-base
```





ALTERAR TAMANHO DO H2 PARA 35PX!!!

