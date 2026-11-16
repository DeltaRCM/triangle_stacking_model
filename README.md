# Triangle Stacking Model

A 2D model for simulating compensational and random stacking of triangular
channel deposits.

## Requirements

Python 3 with NumPy and Matplotlib. The `sandplover` conda environment can be
used if it has these packages installed.

## Run the simulations

From the project directory, run either script as a module:

```powershell
python -m scripts.run_theoretical
python -m scripts.run_avulsion_means
```

The first run generates the theoretical compensational and random datasets,
both with avulsion mean 1. The second generates compensational datasets with
avulsion means 15 and 30 (where X = 15). Each run writes its CSV files and a
comparison figure to `outputs/`.

The model can also be imported without starting a simulation:

```python
from triangle_stacking_model import simulate_compensational_stacking

history = simulate_compensational_stacking()
```
