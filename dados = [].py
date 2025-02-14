dados = []

for i in range(15):
    while True:
        try:
            altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
            genero = input(f"Digite o gênero da pessoa {i+1} (Masculino/Feminino): ").strip().capitalize()
            if genero not in ["Masculino", "Feminino"]:
                raise ValueError("Gênero inválido. Digite Masculino ou Feminino.")
            dados.append({"altura": altura, "genero": genero})
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

alturas = [pessoa["altura"] for pessoa in dados]
maior_altura = max(alturas)
menor_altura = min(alturas)


alturas_masculinas = [pessoa["altura"] for pessoa in dados if pessoa["genero"] == "Masculino"]
media_masculina = sum(alturas_masculinas) / len(alturas_masculinas) if alturas_masculinas else 0

num_feminino = sum(1 for pessoa in dados if pessoa["genero"] == "Feminino")


print(f"Maior altura: {maior_altura} m")
print(f"Menor altura: {menor_altura} m")
print(f"Média de altura dos homens: {media_masculina:.2f} m")
print(f"Número de mulheres: {num_feminino}")
