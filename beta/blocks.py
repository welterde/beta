class Block(object):

    def __init__(self, slot, name, drop=None, replace=0):
        """
        A block in a chunk.

        :Parameters:
            slot : int
                The index of this block. Globally unique.
            name : str
                A common name for this block.
            drop : int
                The type of block that should be dropped when an instance of
                this block is destroyed. Defaults to the slot value, to drop
                instances of this same type of block.
            replace : int
                The type of block to place in the map when instances of this
                block are destroyed. Defaults to air.
        """

        self.slot = slot
        self.name = name

        if drop is None:
            self.drop = slot
        else:
            self.drop = drop

        self.replace = replace

names = [
    "air",
    "stone",
    "grass",
    "dirt",
    "cobblestone",
    "wood",
    "sapling",
    "bedrock",
    "water",
    "spring",
    "lava",
    "lava-spring",
    "sand",
    "gravel",
    "gold-ore",
    "iron-ore",
    "coal-ore",
    "log",
    "leaves",
    "sponge",
    "glass",
    "red-cloth",
    "orange-cloth",
    "yellow-cloth",
    "lime-cloth",
    "green-cloth",
    "aqua-cloth",
    "cyan-cloth",
    "blue-cloth",
    "purple-cloth",
    "indigo-cloth",
    "violet-cloth",
    "magenta-cloth",
    "pink-cloth",
    "black-cloth",
    "grey-cloth",
    "white-cloth",
    "flower",
    "rose",
    "brown-mushroom",
    "red-mushroom",
    "gold",
    "iron",
    "double-step",
    "step",
    "brick",
    "tnt",
    "bookshelf",
    "mossy-cobblestone",
    "obsidian",
    "torch",
    "fire",
    "mob-spawner",
    "wooden-stairs",
    "chest",
    "redstone-wire",
    "diamond-ore",
    "diamond",
    "workbench",
    "crops",
    "soil",
    "furnace",
    "burning-furnace",
    "signpost",
    "wooden-door",
    "ladder",
    "tracks",
    "stone-stairs",
    "wall-sign",
    "lever",
    "stone-plate",
    "iron-door",
    "wooden-plate",
    "redstone-ore",
    "glowing-redstone-ore",
    "redstone-torch",
    "redstone-torch-on",
    "stone-button",
    "snow",
    "ice",
    "snow-block",
    "cactus",
    "clay",
    "reed",
    "jukebox",
    "fence",
    "pumpkin",
    "brimstone",
    "slow-sand",
    "lightstone",
    "portal",
    "jack-o-lantern",
]

drops = {}

# Block -> block drops.
# If the drop block is zero, then it drops nothing.
drops[2]  = 3  # Grass           -> Dirt
# XXX should drop saplings occasionally
drops[18] = 0  # Leaves
drops[20] = 0  # Glass
drops[60] = 3  # Soil            -> Dirt
drops[62] = 61 # Burning Furnace -> Furnace
drops[78] = 0  # Snow
drops[79] = 0  # Ice

# Block -> item drops.
drops[16] = 263 # Coal Ore Block    -> Coal
drops[56] = 264 # Diamond Ore Block -> Diamond
drops[63] = 323 # Sign Post         -> Sign Item
drops[64] = 324 # Wooden Door       -> Wooden Door Item
drops[68] = 323 # Wall Sign         -> Sign Item
drops[71] = 330 # Iron Door         -> Iron Door Item
drops[83] = 338 # Reed              -> Reed Item
drops[89] = 348 # Lightstone        -> Lightstone Dust

replaces = {}

replaces[79] = 8 # Ice -> Water

blocks = {}

for i, name in enumerate(names):
    kwargs = {}
    if i in drops:
        kwargs["drop"] = drops[i]
    if i in replaces:
        kwargs["replace"] = replaces[i]
    b = Block(i, name, **kwargs)
    blocks[i] = b
    blocks[name] = b
