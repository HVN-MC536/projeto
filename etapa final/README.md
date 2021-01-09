# Etapa Final

## Projeto Mídias e Consequências psicológicas

## Equipe

- Natan Rodrigues de Oliveira

## Slides de apresentação

Os slides usados na apresentação da Etapa Final podem ser vistos [aqui](slides/HVN\ -\ Apresentação\ final.pdf).

## Resumo do projeto

- Rigatto

## Motivação e Contexto

- Rigatto

## Detalhamento do projeto

Com objetivo de construir um modelo tal que pudéssemos verificar a ocorrência de um aumento na média das taxas de suicídio em relação a lançamentos de alguns títulos no cinema, buscamos fontes de dados que conseguissem nos dar informações sobre suicídios ao longo tempo em determinados países e os lançamentos de filmes variados com suas respectivas avaliações. Tais fontes podem ser verificadas mais abaixo.

Uma destas fontes nos trouxe informações sobre diversos países e as taxas de suicídio de acordo com ano, idade, sexo, gênereo e PIB de um determinado país em uma tabela. Algumas colunas tinham muitos valores nulos e outras traziam valores repetidos que não nos serviam para este contexto. Sendo assim, foi nessessário uma normalização da tabela de acordo com a normalização BCNF. O código das normalizações feitas se encontra [neste arquivo](src/normalizacao.py).

A partir da tabela normalizada e disponibilizada em ```.csv```, identificada como [tabela de suicídios](data/raw/tabela.csv), levantamos alguns questionamentos como:

- Qual o PIB do país com maiores taxas de suicídio em 2015?
- Qual a faixa etária das pessoas que mais se suicidaram neste mesmo país?

entre outros questionamentos que fizemos. Conseguimos respondê-los com queries SQL contidas neste [notebook](notebooks/queries_sql.ipynb).

Por meio dos resultados obtidos com as queries acima, verificamos que alguns países tinham taxas exorbitantes e números muito duvidosos, mesmo após a normalização. Portanto foi necessário fazer um tratamento de dados desconsiderando as taxas acima de 100% e, consequentemente, selecionamos países como EUA, Brasil e França para a correlação feita com a fonte de dados sobre filmes.

Já para a fonte de dados dos filmes, buscamos uma fonte do IMDb que trás informações sobre os títulos como nome, gênereo, ano de lançamento e outras em uma tabela ```.csv```, bem como o número de avaliações. Tal tabela pode ser vista [aqui](data/processed/movies.csv).

Usamos o Neo4J para queries das correlações. Separamos <HEIGON, CONTINUA POR FAVOR>

## Evolução do projeto

A primeira proposta do trabalho era relacionar as taxas de suicídios com os filmes, do qual fizemos, porém, estava planejado acrescentar uma outra relação com redes sociais. O objetivo era enxergar um aumento nas taxas de suicídio não só pelos filmes mas também pelo crescimento do uso das redes sociais após seu _boom_ na era dos _smartphones_, com intuito de observar nos dados conclusões bastante conhecidas pela ciência.

As fontes de dados que conseguimos sobre redes sociais, mostrava um crescimento a cada ano do número de usuários, mas não tínhamos uma tabela que documentasse esses números. Então, criamos uma [tabela própria](data/not\ used/redessociais.csv) mas sem muito objetivo no contexto do trabalho.

Após discussão com o professor, decidimos focar apenas na correlação com os filmes e apresentar os resultados, relacionando com o Efeito Werther.

O modelo relacional não sofreu mudanças ao longo do semestre, continuamos com objetivo de relacionar os países e grupos de pessoas com as taxas de suicídio e conseguimos uma boa execução desde o começo, apesar dos valores duvidosos da fonte de dados. Já o modelo em grafo, sofreu diversas mudanças como mostram as figuras abaixo:

### Modelo relacional:
![relacional](assets/ModeloLógicoEtapa3Revisado.jpg)

### Modelo antigo de grafo:
![grafo-redes](assets/graph.png)

### Modelo atualizado de grafo:
![grafo-filmes](assets/GrafoCompletoEstrela.png)

Como podemos perceber, o primeiro grafo não tem pouca informações e não tem relações significativas. Já o segundo, apesar de não ser homogêneo, nos dá muitas informações sobre popularidade dos filmes e, também, os países que sofreram com maiores taxas de suicídio.

## Resultados e discussão

- Heigon

## Conclusões

- Natan

## Modelo Conceitual final

- Rigatto: pegar a imagem em assets

## Modelos lógicos finais

- Natan e Heigon

## Programa de extração e conversão de dados

- Rigatto: o programa está em src

## Conjunto de queries para todos os modelos

- Natan e Heigon (fica mais direto)

## Base de dados

- Rigatto: copiar da etapa 4 ou 3 (nao lembro onde está)

## Arquivos de dados

- Rigatto: mesmo lugar do de cima
