import json, re

with open("recipes.json") as f:
    recipes = json.load(f)

# keyword -> (base color, icing/accent color, topping key)
# Note: these specific rules are checked before the generic "chocolate" rule
# below, so e.g. a cranberry-and-white-chocolate recipe reads as cranberry.
RULES = [
    (r"cranberry", "#b3243f", "#f7d0da", "berries"),
    (r"peppermint|candy cane", "#c23b4a", "#ffffff", "none"),
    (r"christmas pudding|figgy pudding|mincemeat|mince pie", "#4a2a1a", "#8a5a3a", "nuts"),
    (r"stollen|marzipan|panettone", "#f0d98a", "#fff6e3", "citrusZest"),
    (r"eggnog", "#f0e3b8", "#fff8e0", "none"),
    (r"chocolate|cocoa|fudge|brownie|double choc", "#6b4028", "#3f2414", "chocDrizzle"),
    (r"red velvet", "#9c1c2e", "#fdf4f0", "none"),
    (r"lemon", "#f6d34a", "#fff7d6", "citrusZest"),
    (r"carrot", "#e07a2f", "#f3e3c8", "nuts"),
    (r"funfetti|birthday|sprinkle", "#ffe3ef", "#ffffff", "sprinkles"),
    (r"coconut", "#fffaf0", "#f5ead3", "coconut"),
    (r"banana", "#f0d26a", "#fff3cf", "none"),
    (r"pumpkin|spice", "#d9792e", "#f0c48a", "none"),
    (r"strawberr", "#f06d93", "#ffd9e4", "berries"),
    (r"coffee|espresso|tiramisu|affogato", "#5a3a28", "#d9c3a8", "none"),
    (r"pistachio", "#9db36a", "#e4edd4", "nuts"),
    (r"matcha", "#8aa65a", "#e6edd0", "none"),
    (r"peanut butter", "#c6873f", "#efcd8e", "none"),
    (r"caramel|toffee|dulce|salted caramel", "#b3762f", "#e8b96a", "caramelDrizzle"),
    (r"blondie|white chocolate|macadamia", "#e8d2a0", "#fff6e6", "nuts"),
    (r"gingerbread|molasses|spice cookie", "#8a4a22", "#d9a15c", "none"),
    (r"sugar cookie|shortbread|snickerdoodle|crinkle", "#e8c98f", "#fff5df", "none"),
    (r"macaroon", "#fdf6e3", "#f0e0b0", "coconut"),
    (r"blueberr|berry", "#5b4a8a", "#d8d0f0", "berries"),
    (r"raspberr", "#b23a56", "#f4c6d4", "berries"),
    (r"apple", "#c23b2e", "#f0c48a", "none"),
    (r"rhubarb", "#d9597a", "#f6d3de", "none"),
    (r"peach", "#f0a36a", "#ffe3cc", "none"),
    (r"pear", "#c7d98a", "#eef3d9", "none"),
    (r"plum", "#7a4a7a", "#e3cfe8", "none"),
    (r"apricot", "#f0a046", "#ffe0b3", "none"),
    (r"cherry", "#9c1f2e", "#f4b8bf", "none"),
    (r"key lime|lime", "#b7d87a", "#eef7d9", "citrusZest"),
    (r"pecan", "#8a5a2e", "#d9a15c", "nuts"),
    (r"meringue", "#fff8ec", "#ffe9b3", "none"),
    (r"banoffee", "#c6873f", "#f0d9a8", "caramelDrizzle"),
    (r"fruit tart|glazed fruit", "#e8607a", "#ffe3ea", "berries"),
    (r"ganache|chocolate tart|chocolate cream", "#4a2a1a", "#8a5a3a", "chocDrizzle"),
    (r"custard|vanilla pudding|panna cotta|crem", "#fdf2d8", "#f5e2ab", "none"),
    (r"black rice", "#4a2a5c", "#d9c3e8", "none"),
    (r"arroz con leche", "#e8b25c", "#fff3d6", "citrusZest"),
    (r"rice pudding", "#f5ecd8", "#e8d9b0", "none"),
    (r"bread pudding", "#c98a4f", "#e8c08a", "none"),
    (r"sticky toffee", "#7a4a26", "#d9a15c", "caramelDrizzle"),
    (r"butterscotch", "#b3762f", "#f0cb84", "none"),
    (r"mint choc", "#6fae8a", "#cdeedd", "chocDrizzle"),
    (r"mango", "#f0a63a", "#ffe2ad", "none"),
    (r"cookies and cream|cookies & cream|oreo", "#4a4a4a", "#ffffff", "chocDrizzle"),
    (r"semifreddo|ice cream sandwich", "#f0e6d2", "#fff8ec", "none"),
    (r"frozen yogurt", "#fdf2f0", "#f6d9e2", "berries"),
    (r"croissant|danish|palmier|turnover", "#e3a85c", "#f5d9a8", "none"),
    (r"cinnamon roll|churro", "#c6873f", "#e8c08a", "caramelDrizzle"),
    (r"eclair|cream puff|profiterole", "#6b4028", "#3f2414", "chocDrizzle"),
    (r"baklava", "#c6873f", "#e8c08a", "nuts"),
    (r"beignet", "#f0e0bf", "#ffffff", "none"),
    (r"glazed donut", "#f0e0bf", "#ffffff", "none"),
    (r"chocolate frosted donut", "#4a2a1a", "#8a5a3a", "sprinkles"),
    (r"jelly filled", "#c23b56", "#f0e0bf", "none"),
    (r"cinnamon sugar", "#c6873f", "#e8c08a", "none"),
    (r"boston cream", "#4a2a1a", "#f0e0bf", "none"),
    (r"apple cider donut", "#c6873f", "#e8c08a", "none"),
    (r"maple bacon", "#9c5a2a", "#d9a15c", "none"),
    (r"powdered sugar", "#f0e0bf", "#ffffff", "none"),
    (r"cheesecake", "#fdf2d8", "#f5e2ab", "berries"),
    (r"tres leches", "#f5ecd8", "#e8d9b0", "none"),
    (r"mochi", "#f5d9e8", "#ffffff", "none"),
    (r"truffle|rocky road", "#4a2a1a", "#3f2414", "nuts"),
    (r"fudge", "#4a2a1a", "#6b4028", "none"),
    (r"mango sticky rice", "#f0d26a", "#fff3cf", "none"),
    (r"cannoli", "#fdf2d8", "#f5e2ab", "nuts"),
]

DEFAULT = ("#d9a441", "#f3d9cd", "none")

def classify(name):
    n = name.lower()
    for pattern, main, light, topping in RULES:
        if re.search(pattern, n):
            return main, light, topping
    return DEFAULT

for r in recipes:
    main, light, topping = classify(r["name"])
    r["mainColor"] = main
    r["lightColor"] = light
    r["topping"] = topping

with open("recipes.json", "w") as f:
    json.dump(recipes, f, indent=0)

print("enriched", len(recipes), "recipes")
from collections import Counter
print(Counter(r["topping"] for r in recipes))
