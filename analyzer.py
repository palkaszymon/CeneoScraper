import os
import pandas as pd

print(*[filename.split('.')[0] for filename in os.listdir('./opinions')], sep='\n')
ceneo_id = input('Insert item id')

opinions = pd.read_json(f"opinions/{ceneo_id}.json")
print(opinions)