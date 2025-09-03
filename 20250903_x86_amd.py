import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

device = "AMD EPYC 9174F"

label_kem = [
    ("RSA\n2048", "public", 83.900),
    ("RSA\n2048", "private", 2.450),
    ("DH\n2048", "key gen", 4.810),
    ("DH\n2048", "agree", 4.799),
    ("ECC\nSECP256R1", "key gen", 103.157),
    ("ECDH\nSECP256R1", "agree", 24.505),
    ("ML-KEM\n512", "key gen", 313.796),
    ("ML-KEM\n512", "encap", 288.330),
    ("ML-KEM\n512", "decap", 260.102),
    ("ML-KEM\n768", "key gen", 190.054),
    ("ML-KEM\n768", "encap", 189.587),
    ("ML-KEM\n768", "decap", 225.599),
    ("ML-KEM\n1024", "key gen", 130.607),
    ("ML-KEM\n1024", "encap", 124.763),
    ("ML-KEM\n1024", "decap", 162.428),
]

label_sign = [
    ("ECDSA\nSECP256R1", "sign", 67.450),
    ("ECDSA\nSECP256R1", "verify", 22.673),
    ("ML-DSA\n44", "key gen", 22.546),
    ("ML-DSA\n44", "sign", 5.155),
    ("ML-DSA\n44", "verify", 19.985),
    ("ML-DSA\n65", "key gen", 12.162),
    ("ML-DSA\n65", "sign", 3.413),
    ("ML-DSA\n65", "verify", 12.782),
    ("ML-DSA\n87", "key gen", 8.327),
    ("ML-DSA\n87", "sign", 2.767),
    ("ML-DSA\n87", "verify", 7.879),
]

def plot_benchmark(ax, labels, title, ylim=300):
    groups = defaultdict(list)
    for alg, op, val in labels:
        groups[alg].append((op, val))

    bar_width = 0.2
    x_base = np.arange(len(groups)) * 0.95

    for i, (group, items) in enumerate(groups.items()):
        n = len(items)
        offsets = (np.arange(n) - (n - 1) / 2) * bar_width * 1.2
        x_positions = x_base[i] + offsets
        ax.bar(x_positions, [val for _, val in items], width=bar_width, label=group)
        for x, (op, val) in zip(x_positions, items):
            ax.text(x, val + 2, f"{op}", ha="center", va="bottom", fontsize=10, rotation=90)

    ax.set_xticks(x_base)
    ax.set_xticklabels(groups.keys(), fontsize=12)
    ax.set_ylabel("1000 ops/sec", fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.tick_params(axis="y", labelsize=10)
    ax.set_ylim(0, ylim)
    # ax.legend(fontsize=10)


fig, axes = plt.subplots(1, 2, figsize=(18, 7))

fig.suptitle(f"Benchmark on {device}", fontsize=20)
plot_benchmark(axes[0], label_kem, "Benchmark (KEM / Key Exchange)", 400)
plot_benchmark(axes[1], label_sign, "Benchmark (Signatures)", 80)

plt.tight_layout()
plt.savefig(f"pqc_benchmark_multiple_{device}.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
