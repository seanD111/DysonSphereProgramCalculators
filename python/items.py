import numpy as np
from enum import IntEnum, auto


class Item(IntEnum):
    iron_ore = 0
    copper_ore = auto()
    silicon_ore = auto()
    stone_ore = auto()
    titanium_ore = auto()
    crude_oil = auto()
    refined_oil = auto()
    hydrogen = auto()
    graphite = auto()
    iron_ingot = auto()
    copper_ingot = auto()
    silicon_ingot = auto()
    titanium_ingot = auto()
    circuit = auto()
    microcrystal = auto()
    processor = auto()
    electric_motor = auto()
    magnetic_coil = auto()
    magnet = auto()
    gear = auto()
    sorter_mk1 = auto()
    sorter_mk2 = auto()



item_count = len(Item)

RECIPES = np.ndarray((item_count, item_count), dtype=np.float32)
RECIPES[:] = 0.0
r = RECIPES

# ratios for natural mats to prevent algorithm from breaking
r[Item.iron_ore, Item.iron_ore] = 1.0
r[Item.copper_ore, Item.copper_ore] = 1.0
r[Item.silicon_ore, Item.silicon_ore] = 1.0
r[Item.crude_oil, Item.crude_oil] = 1.0


# basic furnace smelting
r[Item.copper_ore, Item.copper_ingot] = 1.0
r[Item.iron_ore, Item.iron_ingot] = 1.0
r[Item.iron_ore, Item.magnet] = 1.0
r[Item.silicon_ore, Item.silicon_ingot] = 2.0
r[Item.titanium_ore, Item.titanium_ingot] = 1.0

# refinery recipes
r[Item.crude_oil, Item.refined_oil] = 1.0
r[Item.crude_oil, Item.hydrogen] = 2.0
r[Item.refined_oil, Item.hydrogen] = 1.0
r[Item.refined_oil, Item.graphite] = 1.0




# material recipes
r[Item.iron_ingot, Item.gear] = 1.0

r[Item.copper_ingot, Item.circuit] = 0.5
r[Item.iron_ingot, Item.circuit] = 1.0

r[Item.silicon_ingot, Item.microcrystal] = 2.0
r[Item.copper_ingot, Item.microcrystal] = 1.0

r[Item.circuit, Item.processor] = 2.0
r[Item.microcrystal, Item.processor] = 2.0

r[Item.magnet, Item.magnetic_coil] = 1.0
r[Item.copper_ingot, Item.magnetic_coil] = 0.5

r[Item.iron_ingot, Item.electric_motor] = 2.0
r[Item.gear, Item.electric_motor] = 1.0
r[Item.magnetic_coil, Item.electric_motor] = 1.0

r[Item.iron_ingot, Item.sorter_mk1] = 1.0
r[Item.circuit, Item.sorter_mk1] = 1.0
r[Item.sorter_mk1, Item.sorter_mk2] = 1.0
r[Item.electric_motor, Item.sorter_mk2] = 0.5

















