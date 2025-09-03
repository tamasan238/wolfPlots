import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

device = "Intel Core i7-12700"

label_kem = [
    ("RSA\n2048", "public", 96.457),
    ("RSA\n2048", "private", 2.421),
    ("DH\n2048", "key gen", 5.497),
    ("DH\n2048", "agree", 5.393),
    ("ECC\nSECP256R1", "key gen", 85.357),
    ("ECDH\nSECP256R1", "agree", 27.814),
    ("ML-KEM\n512", "key gen", 142.481),
    ("ML-KEM\n512", "encap", 137.161),
    ("ML-KEM\n512", "decap", 296.040),
    ("ML-KEM\n768", "key gen", 70.371),
    ("ML-KEM\n768", "encap", 69.326),
    ("ML-KEM\n768", "decap", 256.994),
    ("ML-KEM\n1024", "key gen", 41.760),
    ("ML-KEM\n1024", "encap", 40.955),
    ("ML-KEM\n1024", "decap", 185.762),
]

label_sign = [
    ("ECDSA\nSECP256R1", "sign", 59.483),
    ("ECDSA\nSECP256R1", "verify", 29.772),
    ("ML-DSA\n44", "key gen", 28.762),
    ("ML-DSA\n44", "sign", 6.958),
    ("ML-DSA\n44", "verify", 26.026),
    ("ML-DSA\n65", "key gen", 14.819),
    ("ML-DSA\n65", "sign", 4.423),
    ("ML-DSA\n65", "verify", 16.538),
    ("ML-DSA\n87", "key gen", 10.731),
    ("ML-DSA\n87", "sign", 3.695),
    ("ML-DSA\n87", "verify", 10.326),
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
plot_benchmark(axes[0], label_kem, "Benchmark (KEM / Key Exchange)",350)
plot_benchmark(axes[1], label_sign, "Benchmark (Signatures)",70)

plt.tight_layout()
plt.savefig(f"pqc_benchmark_multiple_{device}.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
