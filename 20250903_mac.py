import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

device = "Apple M2 Pro"

label_kem = [
    ("RSA\n2048", "public", 75.537075),
    ("RSA\n2048", "private", 2.109846),
    ("DH\n2048", "keygen", 4.065183),
    ("DH\n2048", "agree", 4.412652),
    ("ECC\nSECP256R1", "keygen", 90.785563),
    ("ECDH\nSECP256R1", "agree", 26.720157),
    ("ML-KEM\n512", "keygen", 316.212697),
    ("ML-KEM\n512", "encap", 281.892069),
    ("ML-KEM\n512", "decap", 253.503900),
    ("ML-KEM\n768", "keygen", 217.973652),
    ("ML-KEM\n768", "encap", 187.165550),
    ("ML-KEM\n768", "decap", 184.627985),
    ("ML-KEM\n1024", "keygen", 128.062079),
    ("ML-KEM\n1024", "encap", 114.839573),
    ("ML-KEM\n1024", "decap", 133.211262),
]

label_sign = [
    ("ECDSA\nSECP256R1", "sign", 60.799391),
    ("ECDSA\nSECP256R1", "verify", 26.019002),
    ("ML-DSA\n44", "keygen", 35.777745),
    ("ML-DSA\n44", "sign", 8.374332),
    ("ML-DSA\n44", "verify", 30.999601),
    ("ML-DSA\n65", "keygen", 17.512544),
    ("ML-DSA\n65", "sign", 5.464112),
    ("ML-DSA\n65", "verify", 19.617546),
    ("ML-DSA\n87", "keygen", 13.191518),
    ("ML-DSA\n87", "sign", 4.522534),
    ("ML-DSA\n87", "verify", 12.431949),
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

fig, axes = plt.subplots(1, 2, figsize=(18, 7))

fig.suptitle(f"Benchmark on {device}", fontsize=20)
plot_benchmark(axes[0], label_kem, "Benchmark (KEM / Key Exchange)", 400)
plot_benchmark(axes[1], label_sign, "Benchmark (Signatures)", 80)

plt.tight_layout()
plt.savefig(f"pqc_benchmark_multiple_{device}.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
