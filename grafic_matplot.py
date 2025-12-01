import matplotlib.pyplot as plt
from vars import alt_recon_time as recon_time, alt_array_dis_por as array_dis_por

plt.figure(figsize=(10, 4))
plt.plot(recon_time, marker='o')
plt.title("Tempo De Latência do Reconhecimento")
plt.xlabel("Excução Numeroº")
plt.ylabel("Tempo em Segundos")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(array_dis_por, marker='o', color='green')
plt.title("Taxa de Similaridade Facial em Porcentagem")
plt.xlabel("Excução Numeroº")
plt.ylabel("Similaridade %")
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
