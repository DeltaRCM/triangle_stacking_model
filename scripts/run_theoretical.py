"""Generate the compensational and random datasets with avulsion mean 1."""

import numpy as np

from scripts._common import OUTPUT_DIR, save_comparison_figure, save_history_csv
from triangle_stacking_model import simulate_compensational_stacking


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    run_kwargs = {
        "num_steps": 2000,
        "num_cols": 40,
        "channel_width": 2.0,
        "element_height": 2.0,
        "avulsion_mean": 1.0,
        "avulsion_std_dev": 0.0,
        "clip_edges": 0,
        "clip_bottom": 0,
        "clip_top": 0,
    }
    scenarios = []

    for name, strategy, title in (
        ("compensational_stacking", "low", "Compensational ($T_A=1$)"),
        ("random_stacking", "random", "Random ($T_A=1$)"),
    ):
        np.random.seed(42)
        history, cycle_ids = simulate_compensational_stacking(
            **run_kwargs, avulsion_strategy=strategy, return_cycle_ids=True
        )
        csv_path = OUTPUT_DIR / f"{name}.csv"
        save_history_csv(history, csv_path)
        print(f"Saved {csv_path}")
        scenarios.append((title, history, cycle_ids))

    figure_path = OUTPUT_DIR / "theoretical_datasets.png"
    save_comparison_figure(scenarios, figure_path)
    print(f"Saved {figure_path}")


if __name__ == "__main__":
    main()
