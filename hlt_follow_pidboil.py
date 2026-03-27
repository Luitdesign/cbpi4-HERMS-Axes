from asyncio import sleep

from cbpi.api import *
from cbpi.controller.kettle_logic import PIDBoil


@parameters([
    Property.Kettle(
        label="Source Kettle",
        description="Kettle whose target temperature should be followed",
    ),
    Property.Number(
        label="Delta Temp",
        configurable=True,
        default_value=0,
        description="Offset added to the source kettle target temperature",
    ),
    Property.Number(
        label="Sync Interval",
        configurable=True,
        default_value=2,
        description="Seconds between source-target synchronization",
    ),
])
class HLTFollowPIDBoil(PIDBoil):
    """
    HLT controller that follows the target temperature of another kettle,
    adds a configurable delta, and runs normal PIDBoil control on the result.
    """

    async def run(self):
        source_kettle_id = int(self.props.get("Source Kettle"))
        delta = float(self.props.get("Delta Temp", 0))
        sync_interval = max(float(self.props.get("Sync Interval", 2)), 0.5)

        while self.running:
            source_kettle = self.api.kettle.get_kettle(source_kettle_id)
            source_target = 0
            if source_kettle is not None:
                source_target = float(getattr(source_kettle, "target_temp", 0) or 0)

            followed_target = source_target + delta

            # Keep this kettle target in sync with source + delta
            if float(self.kettle.target_temp or 0) != followed_target:
                await self.set_target_temp(followed_target)

            # Let PIDBoil drive power using the synchronized target.
            await self.control()
            await sleep(sync_interval)



def setup(cbpi):
    cbpi.plugin.register("HLTFollowPIDBoil", HLTFollowPIDBoil)
