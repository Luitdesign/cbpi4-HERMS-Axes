from setuptools import setup

setup(
    name="cbpi4-HERMS-Axes",
    version="0.0.2",
    description="CBPI4 HLT-following PIDBoil kettle logic for HERMS",
    py_modules=["hlt_follow_pidboil"],
    entry_points={
        "cbpi.plugin": [
            "cbpi4-HERMS-Axes = hlt_follow_pidboil:setup",
        ],
    },
)
