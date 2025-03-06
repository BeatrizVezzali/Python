import numpy as np
import matplotlib.pyplot as plt

# Criando a grade de valores para x
x = np.linspace(-10, 10, 100)

# Definição das retas do sistema
y1 = 16 - x # Equação x + y = 16 -> y = 16 - x
y2 = x + 10 # Equação x - y = 10 -> y = x + 10

# Criando a figura
plt.figure(figsize = (8, 6))

# Plotando as retas
plt.plot(x, y1, label = r'$x + y = 16$', color = 'red')
plt.plot(x, y2, label = r'$x - y = -10$', color = 'blue')

# Plotando a solução (3, 13)
plt.scatter(3, 13, color = 'black', s = 100, label = "Solução (3,13)")

# Rótulos e título
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Interseção das Retas - Solução do Sistema')
plt.axhline(0, color = 'black', linewidth = 0.5)
plt.axvline(0, color = 'black', linewidth = 0.5)
plt.legend()
plt.grid()

#Exibir o gráfico
plt.show()
