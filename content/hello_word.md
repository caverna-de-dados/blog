Title: Uma abordagem prática da Lei dos Grandes Números
Date: 2019-03-15 00:41
Modified: 2019-03-15 00:41
Category: Matemática
Tags: pelican, publishing
Slug: uma-abordagem-pratica-da-lei-dos-grandes-numeros
Authors: diego
Summary: Veja uma abordagem prática da aplicação da Lei dos Grandes Números a um experimento de Roleta Maluca

Quando estamos na escola, ou algum momento da nossa vida, nos deparamos com o ensino de probabilidade, estátistica e afins, e nos deparamos com o seguinte problema: dada uma moeda, qual a chance de cair cara ou coroa?

Diante desse desafio, vemos que há 50% chances de cair cara e 50% chances de cair coroa! E isso está correto, porém como bons cientistas e curiosos que somos, vamos ao experimento, e lançamos a moeda algumas dez vezes, contudo, vemos na prática que ocorre mais caras do que coroas, ou o inverso..

Ora, como isso é possível? Será que as contas que foram feitas estão erradas? Será que a matemática é falha?

Bom … Isso intrigou alguns pensadores até o momentos, dentre eles estava Jakob Bernoulli (1654-1705). Ele disse que existem algum número de tentativa que devemos fazer, para que o número calculado de fato ocorra. Um número grande, dai o nome.

Ou seja, existem um número de lançamentos, no caso da moeda, para qual o número de vezes que sai coroa é aproximadamente metade e de sair cara, também. E este número tende a ser grande.

Para demostrar essa idéia, não usarei o exemplo da moeda, pois não há tempo de lançar uma moeda 10⁶ vezes. Usarei um trabalho de faculdade, o qual me motivou a escreve este texto.

Se trata de uma roleta maluta (nome do trabalho), um jogo em que o usuário informa um número, entre 2 e 100, que será o total de possibilidades da roleta. Por exemplo caso o usuário digite 50, haverá 50 possibilidades na roleta.

Para cada possibilidade há uma probabilidade de escolha atribuida ao número, o que signifca que para cair o número 0 há uma probabilidade x e para o 1 é y, assim por diante.

E por fim, se trata de uma competição com a máquina, cujo cada um, máquina e jogador, devem escolher um número e ganha aquele que chegar mais perto do número.

Para efeitos de observação, irei simular algumas jogadas e exibir uma tabela para ver como os números se comportam.

(Explicando as tabelas: x é o número em questão. Peso, é o peso (rs) atribuido a variável x, Prob(x) é a probabilidade calculada de sair x e Freq(x) é a frequência observada de fato nos sorteios de números)