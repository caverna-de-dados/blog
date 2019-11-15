Title: Como instalar o R no Jupyter Notebook usando o Anaconda
Date: 2019-05-07 01:00
Modified: 2019-05-07 01:00
Category: Tutoriais
Tags: R, Jupyter Notebook, Anaconda
Slug: como-instalar-o-r-no-jupyter-notebook-usando-o-anaconda
Author: hugo
Summary: Saiba como instalar o Setup 'R Essentials' no Anaconda e poder usar no Jupyter Notebook, o R, e mais de 80 pacotes voltados a Data Science.
Cover: assets/img/post-1/anaconda.jpg

[Jupyter Notebook](https://jupyter.org/) é uma Aplicação Web Open-Source e uma das principais ferramentas usadas pelos Data Scientists!

Ele permite criar e compartilhar documentos que suportam desde códigos em múltiplas linguagens, como por exemplo, Python, R e Julia, até textos em Markdown, equações em LaTeX e visualizações de gráficos, imagens e vídeos, além de ser facilmente instalável pelo [Anaconda](https://anaconda.org/).

Habitualmente em Data Science, a linguagem Python acaba por ser a mais utilizada no Jupyter, enquanto que o R possui seu próprio software de análises, o [RStudio](https://www.rstudio.com/).

Contudo, é perfeitamente possível instalar setups de outras linguagens no Anaconda e usá-las no Jupyter Notebook. Então, bora lá!



## INSTALANDO O "R ESSENTIALS"

O "R Essentials" é um setup criado pela equipe do Anaconda que reúne os principais pacotes de R, com aproximadamente 80 sendo voltados para Data Science, como dplyr, ggplot2, tidyr, entre outros.

Ao instalar esse setup, é possível fazer o uso da linguagem R no Jupyter Notebook, bem como todos os pacotes vindos com ele.

Antes de instalar o "R Essentials" é necessário prestar **atenção a um pequeno ponto**: você pode instalar o "R Essentials" no seu environment (ambiente) de uso atual ou instalá-lo em um novo environment.

Ao utilizar um novo environment, você terá um novo ambiente apenas para o armazenamento e organização dos pacotes de R, isso pode ajudar caso no futuro você queira deixar esse ambiente ainda mais robusto e customizado. Ainda assim, não há nenhum problema em usar o mesmo envinroment para os pacotes de Python e R.

Então, no prompt do Anaconda:

Para instalar o "R Essentials" no seu **environment atual**, utilize o comando:

```
conda install -c r r-essentials 
```



Caso você queira criar um **novo environment**, basta usar o comando abaixo (para explicitar o interpretador do R como padrão, adicionamos o r-base  ao final do comando):

```
conda create -n r_env r-essentials r-base
```



Pronto! Agora é só esperar a conclusão da instalação e você já terá um environment configurado com a linguagem R e seus principais pacotes.



## Utilizando o R no Jupyter Notebook

Se você instalou o "R Essentials" no seu environment corrente, então basta abrir o Jupyter Notebook e você já verá a linguagem R disponível.

![Imagem retirada do site do Anaconda: https://docs.anaconda.com/anaconda/navigator/tutorials/r-lang/]({static}/assets/img/post-1/jupyter.jpg)

Caso você tenha usado um novo environment, então é necessário ativá-lo antes de abrir o Jupyter Notebook.

```
conda activate r_env
jupyter notebook
```

Agora é só criar um novo notebook com a linguagem R. Vamos fazer alguns testes apenas para confirmar que está tudo funcionando bem.

Vamos chamar o pacote dplyr:

![Screenshot at 12-37-43]({static}/assets/img/post-1/library.jpg)

Podemos usar agora o famoso dataset Iris:

![Screenshot at 12-42-14]({static}/assets/img/post-1/dataset.jpg)

Pronto! Nosso pequeno teste demonstrou que está tudo funcionando ok. Agora você já pode criar e compartilhar seus Jupyter Notebooks com a linguagem R!

Espero que este breve post tenha te ajudado. Até a próxima!
