import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

device = "STM32 NUCLEO-F439ZI ARM Cortex M4"

label_kem = [
    ("RSA\n2048", "public", 110.672),
    ("RSA\n2048", "private", 3.082),
    ("DH\n2048", "key gen", 6.087),
    ("DH\n2048", "agree", 6.107),
    ("ECC\nSECP256R1", "key gen", 178.749),
    ("ECDH\nSECP256R1", "agree", 84.646),
    ("ML-KEM\n512", "key gen", 248),
    ("ML-KEM\n512", "encap", 262),
    ("ML-KEM\n512", "decap", 198),
    ("ML-KEM\n768", "key gen", 153.386),
    ("ML-KEM\n768", "encap", 152.174),
    ("ML-KEM\n768", "decap", 120),
    ("ML-KEM\n1024", "key gen", 93.254),
    ("ML-KEM\n1024", "encap", 92.52),
    ("ML-KEM\n1024", "decap", 76.172),
]

label_sign = [
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
    ax.set_ylabel("ops/sec", fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.tick_params(axis="y", labelsize=10)
    ax.set_ylim(0, ylim)
    # ax.legend(fontsize=10)


fig, axes = plt.subplots(1, 2, figsize=(18, 7))

fig.suptitle(f"Benchmark on {device}", fontsize=20)
plot_benchmark(axes[0], label_kem, "Benchmark (KEM / Key Exchange)")
plot_benchmark(axes[1], label_sign, "Benchmark (Signatures)", 120)

plt.tight_layout()
plt.savefig(f"pqc_benchmark_multiple_{device}.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
