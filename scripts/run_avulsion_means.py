"""Generate compensational datasets with avulsion means 15 and 30."""

import numpy as np

from scripts._common import OUTPUT_DIR, save_comparison_figure, save_history_csv
from triangle_stacking_model import simulate_compensational_stacking


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    scenarios = []

    for name, avulsion_mean, title in (
        ("compensational_stacking_meanX", 15.0, "Compensational ($T_A=X$, X=15)"),
        ("compensational_stacking_mean2X", 30.0, "Compensational ($T_A=2X$, X=15)"),
    ):
        np.random.seed(42)
        history, cycle_ids = simulate_compensational_stacking(
            num_steps=2000,
            num_cols=40,
            channel_width=2.0,
            element_height=2.0,
            avulsion_mean=avulsion_mean,
            avulsion_std_dev=0.0,
            avulsion_strategy="low",
            clip_edges=0,
            clip_bottom=0,
            clip_top=0,
            return_cycle_ids=True,
        )
        csv_path = OUTPUT_DIR / f"{name}.csv"
        save_history_csv(history, csv_path)
        print(f"Saved {csv_path}")
        scenarios.append((title, history, cycle_ids))

    figure_path = OUTPUT_DIR / "avulsion_mean_datasets.png"
    save_comparison_figure(scenarios, figure_path)
    print(f"Saved {figure_path}")


if __name__ == "__main__":
    main()
