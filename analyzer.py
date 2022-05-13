import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print(*[filename.split('.')[0] for filename in os.listdir('./opinions')], sep='\n')
ceneo_id = input('Insert item id: ')

opinions = pd.read_json(f"opinions/{ceneo_id}.json")

opinions.stars = opinions.stars.map(lambda x: float(x.split('/')[0].replace(',', '.')))
opinions_count = len(opinions.index)
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean().round(2)

recommendation = opinions.recomendation.value_counts(dropna = False).sort_index().reindex(['Nie polecam', 'Polecam', None])
recommendation.plot.pie(
    label="", 
    autopct='%1.1f%%',
    colors=['crimson', 'lightskyblue', 'forestgreen'],
    labels=['Nie polecam', 'Polecam', 'Nie mam zdania']
    )

plt.title('Rekomendacja')
plt.savefig()
plt.close()

stars = opinions.stars.value_counts().sort_index().reindex(list(np.arrange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
plt.title('Oceny produktu')
plt.xlabel('Liczba gwiazdek')
plt.ylabel('Liczba opinii')
plt.grid(True)
plt.xticks(rotation=0)
plt.savefig(f'plots/{ceneo_id}_stars.png')
plt.close()