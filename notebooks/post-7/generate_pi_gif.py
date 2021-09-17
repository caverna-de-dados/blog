# É importante salientar que da para otimizar este codigo, 
# ele esta ineficiente no sentido de que para calcular
# 1 frame, ele recalcula tudo, não reutilizando o que 
# ja foi computado, para grande numero de frames,
# isso impacta bastante, mas creio que da maneira que esta
# fica mais fácil de entender. 

# Importa as bibliotecas necessarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import  animation

# Semente para reprodutibilidade.
np.random.seed(312)

# Inicializa variaveis uteis para fazer o gif.
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# Obtem os pontos de exemplo, vão ser obtidos
# uniformemente no intervalo -1, 1, ou seja
# pontos ~ Unif(-1, 1).
#
# qtd_pontos -> quantidade de pontos a serem simulados,
# para efeitos de teste, substitua por um valor pequeno.
qtd_pontos = 35000
points = np.random.uniform(-1,1,(qtd_pontos, 2)) 

# Função responsavel por gerar um frame no "instante
# de tempo" i
def animate(i):
    # esvazia o "canvas"
    ax1.clear()
    
    # Desenha a circunferencia de radio 1.
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(np.cos(theta), np.sin(theta))
    
    # Gera o mapa de cores e atualiza a quantidade de pontos
    # dentro da circunferencia:
    # azul -> dentro da circunferencia
    # vermelho -> fora da circunferencia
    cores = []
    qtd_pontos_dentro = 0
    for j in range(i+1):
        if np.linalg.norm(points[j, :]) <= 1:
            cores.append("blue")
            qtd_pontos_dentro += 1
        else:
            cores.append("red")
    
    # Exibe os pontos para o frame i, com as respectivas cores
    ax1.scatter(points[:i+1, 0], points[:i+1,1], s=3, c=cores)
    
    #Isso é para evitar que o matplotlib "deforme" os eixos,
    # caso contrario, a esfera pareceria uma elipse rs.
    ax1.axis('equal')
    
    # Atualiza o titulo para mostrar a aproximacao de pi atual,
    # esta vem do fato de que para um radio = 1/2 a area é pi(1/2)ˆ2
    # pi(1/2)ˆ2 \approx qtd_pontos_dentro/qtd_pontos => pi \approx 4*qtd_pontos_dentro/qtd_pontos
    #
    # importante evitar divisao por 0.
    if i == 0:
        ax1.set_title("Para n = {}, pi = {}".format(0, 0))
    else:
        ax1.set_title("Para n = {}, pi = {:.3f}".format(i, 4*(qtd_pontos_dentro/i)))
    
# Chama o motor de animação do matplotlib, para renderizar qtd_pontos/2000 frames,
# com um intervalo de 1s entre eles.
ani = animation.FuncAnimation(fig, animate, frames=range(0, qtd_pontos, 2000), interval=1000)
# Salva o gif utilizando imagemagick, da para usar o ffmpeg, mas as 
# configurações são diferentes.
ani.save('circle_pi.gif', writer='imagemagick', fps=3)
plt.close()
