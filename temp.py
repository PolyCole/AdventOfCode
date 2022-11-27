import os
print(os.getcwd())
path = os.getcwd()
looking = f'{path}/2021/06'
print(f'exists: {os.path.exists(looking)}')
