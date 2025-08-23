import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

labels = [
    ("RSA\n2048", "public", 110.672),
    ("RSA\n2048", "private", 3.082),
    ("DH\n2048", "key gen", 6.087),
    ("DH\n2048", "agree", 6.107),
    ("ML-KEM\n512", "key gen", 248),
    ("ML-KEM\n512", "encap", 262),
    ("ML-KEM\n512", "decap", 198),
    ("ML-KEM\n768", "key gen", 153.386),
    ("ML-KEM\n768", "encap", 152.174),
    ("ML-KEM\n768", "decap", 120),
    ("ML-KEM\n1024", "key gen", 93.254),
    ("ML-KEM\n1024", "encap", 92.52),
    ("ML-KEM\n1024", "decap", 76.172),
    ("ECC\nSECP256R1", "key gen", 178.749),
    ("ECDH\nSECP256R1", "agree", 84.646),
    ("ECDSA\nSECP256R1", "sign", 106),
    ("ECDSA\nSECP256R1", "verify", 59.289),
    ("ML-DSA\n44", "key gen", 51.434),
    ("ML-DSA\n44", "sign", 16.575),
    ("ML-DSA\n44", "verify", 45.635),
    ("ML-DSA\n65", "key gen", 28.986),
    ("ML-DSA\n65", "sign", 11.905),
    ("ML-DSA\n65", "verify", 27.264),
    ("ML-DSA\n87", "key gen", 17.192),
    ("ML-DSA\n87", "sign", 7.968),
    ("ML-DSA\n87", "verify", 15.952)
]

groups = defaultdict(list)
for alg, op, val in labels:
    groups[alg].append((op, val))

bar_width = 0.2
fig, ax = plt.subplots(figsize=(16,7))
x_base = np.arange(len(groups)) * 0.95

for i, (group, items) in enumerate(groups.items()):
    n = len(items)
    offsets = (np.arange(n) - (n-1)/2) * bar_width * 1.2
    x_positions = x_base[i] + offsets
    ax.bar(x_positions, [val for _, val in items], width=bar_width, label=group)
    for x, (op, val) in zip(x_positions, items):
        ax.text(x, val+2, f"{op}", ha='center', va='bottom', fontsize=12, rotation=90)

ax.set_xticks(x_base)
ax.set_xticklabels(groups.keys(), fontsize=14)
ax.set_ylabel("ops/sec", fontsize=16)
ax.tick_params(axis='y', labelsize=12)
ax.set_title("Benchmark on STM32 NUCLEO-F439ZI ARM Cortex M4", fontsize=18)

plt.ylim(0, 300)
plt.tight_layout()
plt.savefig("pqc_benchmark.png", format="png", dpi=300, bbox_inches="tight")

