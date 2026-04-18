import matplotlib.pyplot as plt

labels = ['Speed', 'Accuracy', 'Automation']
traditional = [40, 60, 30]
proposed = [90, 92, 95]

x = range(len(labels))

plt.figure()
plt.bar(x, traditional, width=0.4, label='Traditional')
plt.bar([i + 0.4 for i in x], proposed, width=0.4, label='Proposed')

plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Performance (%)")
plt.title("System Comparison")
plt.legend()

plt.savefig("comparison.png")
plt.show()