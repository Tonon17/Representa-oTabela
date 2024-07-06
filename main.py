import pandas as pd

data = {
        'Nome' : ['Grylo', 'Bob', 'Wanderson', 'Jô Soares'],
        'Idade' : [55, 10, 70, 70],
        'Cidade' : ['Brazilandia', 'Valinhos', 'Barão Geralo', 'São Paulo']  
}

df = pd.DataFrame(data)
print(df)