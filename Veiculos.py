# Dados de entrada
dist = 100  
vcarro = 110  
tpedagio_caminhao = 5/60 
vcaminhao = 80  
 

#tempo de viagem do carro
tcarro = dist / vcarro

#tempo de viagem do caminhão
tcaminhao = dist / vcaminhao + (2 * tpedagio_caminhao)  #ida e a volta pelos dois pedágios

# Comparação dos tempos de viagem
if tcarro < tcaminhao:
    print("O carro está mais próximo da cidade de Ribeirão Preto.")
elif tcarro > tcaminhao:
    print("O caminhão está mais próximo da cidade de Ribeirão Preto.")
else:
    print("O carro e o caminhão estarão no mesmo ponto na rodovia.")

#O código está utilizando os dados informados, como distância entre Ribeirão Preto e Franca, velocidades do carro e do caminhão, tempo de passagem em cada pedágio pelo
#caminhão e em seguida, realiza os cálculos para obter os tempos de viagem do carro e do caminhão e determina qual está mais próximo da cidade.

#De maneira mais matemática ficaria da seguinte forma: Tempo Caminhão = Distância / Velocidade -- T = 100 / 80 -- T = 1,25 horas
#Tempo carro = T = 100/110 -- T = 0,91 horas - Considerando que o caminhão leva 5m a mais para passar em cada pedágio, é possível desonciderar o tempo dos pedágios na comparação 
#o Carro está mais perto.