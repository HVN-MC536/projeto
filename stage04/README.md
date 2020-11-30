# Etapa 4 - Análises com o segundo modelo lógico

## Slides de apresentação da etapa

[Slides](slides/stage04.pdf)

## Modelo conceitual atualizado (Etapa 3)

Como discutido mais abaixo, normalizamos a tabela retirada do Kaggle e, portando, foi possível atualizar nosso modelo conceitual para os dados de país, geração e números de suicídios.

![Modelo](assets/ModeloLógicoEtapa3Revisado.jpg)

## Modelos lógicos atualizados (Etapa 3)

Revisamos os modelos lógicos da etapa anterior de acordo com a normalização da tabela original do Kaggle. Chegamos ao seguinte resultado:

~~~
PAÍS(_nome_, _ano_, gdp_for_year, gdp_per_capita)

GERAÇÃO(_idade_, geração)

SUICÍDIOS(_pais_nome_, _pais_ano_, _idade_, _sexo_, suicidio_no, taxa_suicidio)
~~~

## Programa para extração e conversão dos dados atualizados

[Programas de conversão para a etapa 3](../stage03/src)

## Conjunto de queries dos modelos

[Conjunto de queries da etapa 3](../stage03/notebook)

## Base de dados
título da base | link | breve descrição
----- | ----- | -----
| Suicide Rates Overview | [Link](https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016) | Dataset em formato CSV com estatísticas de suicídio organizadas por anos (1985 a 2016), países, sexo, faixas etárias e índices de desenvolvimento sócioeconômicos. |
| Number of monthly active Facebook users | [Link](https://www.statista.com/statistics/264810/number-of-monthly-active-facebook-users-worldwide/) | Número de usuários do Facebook a cada mês de 2008 a 2020 |
| Number of monthly active international users | [Link](https://www.statista.com/statistics/274565/monthly-active-international-twitter-users/) | Número de usuários do Twitter a cada mês de 2009 a 2019|

## Arquivos de dados
nome do arquivo | link | breve descrição
----- | ----- | -----
| tabela.csv | [Link](../stage03/data/rawtabela.csv) | Dataset original da fonte de dados. |
| suicides.csv | [Link](../stage03/data/processed/suicides.csv) | Tabela normalizada com país, ano, sexo, número e taxa de suicídios. |
| pais.csv | [Link](../stage03/data/processed/pais.csv) | Tabela normalizada com país, ano, população, PIB por ano e PIB per capita. |
| generation.csv | [Link](../stage03/data/processed/generation.csv) | Tabela normalizada com geração e faixa etária. |
| redessociais.csv | [Link](../stage04/data/processed/redessociais.csv) | Tabela com dados compilados do números de usuários em diferentes redes sociais|
