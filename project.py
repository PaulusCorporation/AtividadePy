
dados_pessoas = [
    (1.75, 'Masculino'),
    (1.80, 'Feminino'),
    (1.65, 'Masculino'),
    (1.90, 'Feminino'),
    (1.82, 'Masculino'),
    (1.70, 'Feminino'),
    (1.85, 'Masculino'),
    (1.60, 'Feminino'),
    (1.78, 'Masculino'),
    (1.68, 'Feminino'),
    (1.95, 'Masculino'),
    (1.72, 'Feminino'),
    (1.88, 'Masculino'),
    (1.74, 'Feminino'),
    (1.80, 'Masculino')
]


maior_altura = float('-inf')
menor_altura = float('inf')
soma_masculino = 0
count_masculino = 0
count_feminino = 0


for altura, genero in dados_pessoas:
    
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    
    
    if genero == 'Masculino':
        soma_masculino += altura
        count_masculino += 1
    
   
    if genero == 'Feminino':
        count_feminino += 1


media_masculino = soma_masculino / count_masculino if count_masculino > 0 else 0

print(f"A maior altura do grupo é: {maior_altura:.2f} metros.")
print(f"A menor altura do grupo é: {menor_altura:.2f} metros.")
print(f"A média de altura das pessoas do gênero Masculino é: {media_masculino:.2f} metros.")
print(f"O número de pessoas do gênero Feminino é: {count_feminino}.")




