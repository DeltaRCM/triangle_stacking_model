import csv
from pathlib import Path
from typing import Sequence, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "outputs"


def save_history_csv(history: np.ndarray, path: Path) -> None:
    """Write an elevation history with timestep and spatial-column headers."""
    header = ["timestep"] + [f"col_{i}" for i in range(history.shape[1])]
    with path.open("w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        for timestep, row in enumerate(history):
            writer.writerow([timestep, *row])


def save_comparison_figure(
    scenarios: Sequence[Tuple[str, np.ndarray, np.ndarray]], path: Path
) -> None:
    """Plot each scenario's elevation profiles, colored by avulsion cycle."""
    fig, axes = plt.subplots(
        1, len(scenarios), figsize=(4 * len(scenarios), 3.5), dpi=120, sharey=True
    )
    axes = np.atleast_1d(axes)
    cycle_cmap = plt.get_cmap("tab10")

    for ax, (title, history, cycle_ids) in zip(axes, scenarios):
        for step in range(0, history.shape[0], 3):
            ax.plot(
                history[step, :],
                color=cycle_cmap(int(cycle_ids[step]) % cycle_cmap.N),
                linewidth=0.5,
                alpha=0.7,
            )
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("horizontal distance (m)", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.grid(True, linestyle=":", alpha=0.5)

    axes[0].set_ylabel("elevation (m)", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
