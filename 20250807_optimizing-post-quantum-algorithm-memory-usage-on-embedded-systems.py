import matplotlib.pyplot as plt
import numpy as np

data = {
    "Small code": [
        ("ML-KEM\n512", 23568, 7552, 31120, 3),
        ("ML-KEM\n768", 32672, 11968, 44640, 3),
        ("ML-KEM\n1024", 42400, 17568, 59968, 3),
        ("ML-DSA\n44", 15904, 50304, 66208, 2),
        ("ML-DSA\n65", 17440, 77952, 95392, 2),
        ("ML-DSA\n87", 19376, 120960, 140336, 2),
    ],
    "Small code + small mem": [
        ("ML-KEM\n512", 23696, 3968, 27664, 3),
        ("ML-KEM\n768", 32928, 5824, 38752, 3),
        ("ML-KEM\n1024", 42656, 7840, 50496, 3),
        ("ML-DSA\n44", 15856, 15656, 31512, 2),
        ("ML-DSA\n65", 17392, 20776, 38168, 2),
        ("ML-DSA\n87", 19328, 26920, 46248, 2),
    ],
    "Small code + small mem + stack": [
        ("ML-KEM\n512", 2112, 19306, 21418, 17),
        ("ML-KEM\n768", 2112, 27306, 29418, 17),
        ("ML-KEM\n1024", 2112, 35786, 37898, 17),
        ("ML-DSA\n44", 2112, 28211, 30323, 7),
        ("ML-DSA\n65", 2112, 33331, 35443, 7),
        ("ML-DSA\n87", 2160, 39475, 41635, 7),
    ]
}

# KB単位に変換
for conf in data:
    for i, row in enumerate(data[conf]):
        data[conf][i] = (row[0], row[1]/1024, row[2]/1024, row[3]/1024, row[4])

# バーの幅と間隔
bar_width = 0.2
bar_spacing = 0.05
fig, ax = plt.subplots(figsize=(12, 7))
algorithms = [row[0] for row in data["Small code"]]
x = np.arange(len(algorithms))

label_letters = ['(a)', '(b)', '(c)']
label_mapping = {
    '(a)': 'Small code',
    '(b)': 'Small code + small mem',
    '(c)': 'Small code + small mem + stack'
}

# 視認性の良い色
colors = ["tab:blue", "tab:orange"]

for i, (conf, values) in enumerate(data.items()):
    offset = i * (bar_width + bar_spacing)
    stacks = [row[1] for row in values]
    heaps = [row[2] for row in values]
    ax.bar(x + offset, stacks, width=bar_width, color=colors[0], label="Stack" if i==0 else "")
    ax.bar(x + offset, heaps, bottom=stacks, width=bar_width, color=colors[1], label="Heap" if i==0 else "")
    for xi, stack, heap in zip(x + offset, stacks, heaps):
        ax.text(xi, stack + heap + 2, f"{label_letters[i]}", ha='center', va='bottom', fontsize=16, color='black')

# 凡例ラベル
for j, letter in enumerate(label_letters):
    ax.text(0, -25 - j*10, f"{letter}: {label_mapping[letter]}", fontsize=16, ha='left', va='top', color='black', transform=ax.transData)

ax.set_xticks(x + (len(data)/2 - 0.5) * (bar_width + bar_spacing))
ax.set_xticklabels(algorithms, fontsize=16)
ax.set_ylabel("Memory (KB)", fontsize=18)
ax.set_title("Memory Usage (Stack + Heap) by Configuration", fontsize=22)
ax.legend(loc='upper left', fontsize=16)
ax.tick_params(axis='y', labelsize=16)

plt.ylim(0, 160)
plt.tight_layout()
# plt.show()

plt.savefig("pqc_benchmark.png", format="png", dpi=300, bbox_inches="tight")

