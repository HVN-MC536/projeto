import pandas as pd
import numpy as np

def normalize_generation(tabela):
    age_gen = tabela[['age', 'generation']]

    gen_arr = np.unique(age_gen['generation'].values)
    age_arr = np.unique(age_gen['age'].values)

    gen_table = {'G.I. Generation' : '75+ years', 'Silent' : '55-74 years',
                'Boomers' : '35-54 years', 'Generation X' : '25-34 years',
                'Millenials' : '15-24 years', 'Generation Z' : '5-14 years'}
            
    gen_final_table = pd.DataFrame({'generation' : gen_table.keys(), 'age' : gen_table.values()})
    gen_final_table.to_csv('generation.csv', index=False)

def normalize_pais(tabela):
    pais_pop = tabela[['country', 'year', 'sex', 'population']]
    pais_gdp = tabela[['country', 'year', 'gdp_for_year', 'gdp_per_capita']]

    gdp = pais_gdp.groupby(['country', 'year']).max()

    res = pais_pop.groupby(by=['country', 'year', 'sex']).sum()
    ressize = len(res.index)
    population = np.array(int(ressize/2)*[0])
    vec = res.values

    for i in range(0,ressize,2):
        population[int(i/2)] = vec[i][0]+vec[i+1][0]

    pais_pop = pais_pop[['country', 'year']]
    pais_vec = np.unique(pais_pop['country'].values)
    year_vec = np.unique(pais_pop['year'].values)

    pop = 0
    pais_table = [[], [], [], [], []]
    for p in pais_vec:
        for y in year_vec:
            if pais_pop.eq([p, y]).all(1).any():
                pais_table[0].append(p)
                pais_table[1].append(y)
                pais_table[2].append(population[pop])
                pop += 1
    for i in range(len(gdp.index)):
        pais_table[3].append(gdp['gdp_for_year'][i])
        pais_table[4].append(gdp['gdp_per_capita'][i])

    final_table = pd.DataFrame({'country' : pais_table[0], 'year' : pais_table[1],
                                'population' : pais_table[2], 'gdp_for_year' : pais_table[3],
                                'gdp_per_capita' : pais_table[4]})
    final_table.to_csv('pais.csv', index=False)

def normalize_principal(tabela):
    principal = tabela[['country', 'year', 'sex', 'age', 'suicides_no', 'suicides_rate']]
    principal.to_csv('suicides.csv', index=False)

def main():
    tabela = pd.read_csv('tabela.csv')
    # normalize_generation(tabela)
    normalize_pais(tabela)
    # normalize_principal(tabela)

if __name__ == "__main__":
    main()