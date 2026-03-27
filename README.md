# cbpi4-HERMS-Axes

## HLT Follow PIDBoil plugin

This repository provides a CraftBeerPi4 kettle logic plugin called `HLTFollowPIDBoil`.

### What it does

- Reads the target temperature from another kettle (`Source Kettle`)
- Adds a configurable offset (`Delta Temp`)
- Uses that calculated value as this kettle's target temperature
- Runs standard `PIDBoil` control against that synchronized target

### Plugin parameters

- **Source Kettle**: The kettle to follow
- **Delta Temp**: Offset to add to the source target
- **Sync Interval**: Seconds between target sync updates

## Installation

Install into the same Python environment as CBPI so the plugin entry point is registered:

```bash
pip install .
```

Then restart CBPI. In kettle configuration, choose logic **HLTFollowPIDBoil**.

## Why the logic may not appear

CBPI discovers plugins via Python entry points. This repo now includes a `setup.py` with a `cbpi.plugin` entry point, so after `pip install .` and restart, the kettle logic is visible in the UI.

### Files

- `hlt_follow_pidboil.py`
- `setup.py`
