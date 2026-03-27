# cbpi4-HERMS-Axes

## HLT Follow PIDBoil plugin

This repository now includes a CraftBeerPi4 kettle logic plugin called `HLTFollowPIDBoil`.

### What it does

- Reads the target temperature from another kettle (`Source Kettle`)
- Adds a configurable offset (`Delta Temp`)
- Uses that calculated value as this kettle's target temperature
- Runs standard `PIDBoil` control against that synchronized target

### Plugin parameters

- **Source Kettle**: The kettle to follow
- **Delta Temp**: Offset to add to the source target
- **Sync Interval**: Seconds between target sync updates

### File

- `hlt_follow_pidboil.py`
