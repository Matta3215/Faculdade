mb = (input("Digite o tamanho do arquivo(em MB): "))

mbps = (input("Digite a velocidade(em Mbps) "))

tempos = mb / (mbps / 8)

tempom = tempos / 60

print(f"O tempo aproximado de download será de {tempom} minutos")