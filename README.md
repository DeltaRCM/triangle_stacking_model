# Triangle Stacking Model

A 2D model for simulating compensational and random stacking of triangular
channel deposits.

The model is an implementation of an object-based staxking model described in Wang et al., 2011:

> We model basin filling with discrete triangular elements that are meant to represent channel or lobe deposits. During each time step one element is deposited in the basin while the subsidence is set to balance mean basin aggradation. An approximation of the avulsion process is modeled by placing channel elements with the following rules. At every nth time step during basin filling, the active channel relocates to the absolute topographic low in the model domain. For all other time steps deposition follows a random walk with elements moving one channel width left or right of the previous element.

**Key references:**

- Straub, K. M., Paola, C., Mohrig, D., Wolinsky, M. A., & George, T. (2009).
  Compensational stacking of channelized sedimentary deposits.
  *Journal of Sedimentary Research*, 79(9), 673–688.
  <https://doi.org/10.2110/jsr.2009.070>
- Wang, Y., Straub, K. M., & Hajek, E. A. (2011). Scale-dependent compensational
  stacking: An estimate of autogenic time scales in channelized sedimentary
  deposits. *Geology*, 39(9), 811–814.
  <https://doi.org/10.1130/G32068.1>


## Requirements

Python 3 with NumPy and Matplotlib. 

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
