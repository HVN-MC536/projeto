# Etapa 3 - Análises com o primeiro modelo lógico

## Primeiro Modelo Conceitual

## Primeiros Modelos Lógicos

~~~
PAÍS(_nome_, _ano_, gdp_for_year, gdp_per_capita)

GERAÇÃO(_idade_, geração)

SUICÍDIOS(_pais_nome_, _pais_ano_, _idade_, _sexo_, suicidio_no, taxa_suicidio)
~~~

## Primeiro programa de extração e conversão de dados

[Programa de conversão da etapa 3](../stage03/src)

## Primeiro conjunto de queries

[Conjunto de queries da etapa 3](../stage03/notebook)

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
| Suicide Rates Overview | `[Link](https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016)` | `Dataset em formato CSV com estatísticas de suicídio organizadas por anos (1985 a 2016), países, sexo, faixas etárias e índices de desenvolvimento sócioeconômicos.`

## Arquivos de Dados

nome do arquivo | link | breve descrição
----- | ----- | -----
| tabela.csv | [link](../stage03/tabela.csv) | Dataset original da fonte de dados |
`suicides.csv` | `[link](../stage03/suicides.csv)` | `Tabela normalizada com país, ano, sexo, número e taxa de suicídios`
`pais.csv` | `[link](../stage03/pais.csv)` | `Tabela normalizada com país, ano, população, PIB por ano e PIB per capita`
`generation.csv` | `[link](../stage03/generation.csv)` | `Tabela normalizada com geração e faixa etária`