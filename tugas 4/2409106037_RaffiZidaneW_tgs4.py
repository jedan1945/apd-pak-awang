import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] 
y = [2, 4, 6, 8, 10]  

plt.figure(figsize=(8, 5))  
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, label='y = 2x')
plt.title("Grafik Garis Sederhana", fontsize=14)
plt.xlabel("Sumbu X", fontsize=12)
plt.ylabel("Sumbu Y", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10)
plt.show()
