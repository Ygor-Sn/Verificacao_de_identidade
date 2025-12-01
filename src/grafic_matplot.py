import matplotlib.pyplot as plt
from vars import alt_array_dis_por as vars_dis_por, alt_recon_time as vars_recon_time
import numpy as np

alt_array_dis_por = vars_dis_por
alt_recon_time = vars_recon_time
plt.figure(figsize=(10, 4))
plt.plot(alt_recon_time, marker='o')
plt.title("Tempo De Latência do Reconhecimento")
plt.xlabel("Excução Numeroº")
plt.ylabel("Tempo em Segundos")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(alt_array_dis_por, marker='o', color='green')
plt.title("Taxa de Similaridade Facial em Porcentagem")
plt.xlabel("Excução Numeroº")
plt.ylabel("Similaridade %")
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
