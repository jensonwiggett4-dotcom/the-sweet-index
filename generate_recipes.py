import json, re

recipes = []
_id = 0
def nid():
    global _id
    _id += 1
    return f"r{_id:03d}"

def add(name, category, time, servings, difficulty, icon, gradient, ingredients, steps, tip):
    recipes.append({
        "id": nid(),
        "name": name,
        "category": category,
        "time": time,
        "servings": servings,
        "difficulty": difficulty,
        "icon": icon,
        "gradient": gradient,
        "ingredients": ingredients,
        "steps": steps,
        "tip": tip,
    })

GRADIENTS = [
    ["#ffd6e8","#ffe9f1"],["#d6f0e6","#e9f8f0"],["#e3d6f5","#f1e9fb"],["#fff0c6","#fff8e2"],
    ["#cfeaf5","#e5f5fb"],["#ffe1cc","#fff1e5"],["#dcf0d6","#edf8e9"],["#f7d8e4","#fcedf2"],
    ["#d6e0f7","#e9effc"],["#f6e7d7","#fbf3ea"],["#ebd9f7","#f6edfc"],["#d2f3ec","#e9faf6"],
    ["#ffdede","#fff1f1"],["#e3f0d2","#f1f8e9"],["#f0e0ff","#f9f0ff"],["#ffeedb","#fff8ee"],
]
gi = 0
def grad():
    global gi
    g = GRADIENTS[gi % len(GRADIENTS)]
    gi += 1
    return g

# =========================================================
# 1. LAYER CAKES — in-depth method
# =========================================================
cake_variants = [
    ("Classic Vanilla Layer Cake", "vanilla bean paste", "vanilla buttercream", None),
    ("Rich Chocolate Layer Cake", "cocoa powder and a shot of hot espresso", "chocolate ganache frosting", "70% dark chocolate chips"),
    ("Red Velvet Layer Cake", "cocoa powder and red food colouring", "cream cheese frosting", None),
    ("Lemon Drizzle Layer Cake", "lemon zest and juice", "lemon curd buttercream", "candied lemon slices"),
    ("Carrot Layer Cake", "grated carrot, cinnamon and nutmeg", "cream cheese frosting", "toasted walnuts"),
    ("Funfetti Birthday Cake", "a splash of almond extract", "vanilla buttercream", "rainbow sprinkles"),
    ("Coconut Layer Cake", "coconut milk and extract", "coconut cream cheese frosting", "toasted coconut flakes"),
    ("Banana Layer Cake", "mashed ripe banana", "brown-butter cream cheese frosting", "banana chips"),
    ("Spiced Pumpkin Layer Cake", "pumpkin puree and warm spices", "maple cream cheese frosting", "candied pecans"),
    ("Strawberry Layer Cake", "freeze-dried strawberry powder", "strawberry buttercream", "fresh strawberry halves"),
    ("Coffee Walnut Layer Cake", "strong brewed coffee", "coffee buttercream", "chopped walnuts"),
    ("Pistachio Rose Layer Cake", "ground pistachio and rosewater", "pistachio buttercream", "crushed pistachios"),
]
for name, flavor, frosting, mixin in cake_variants:
    g = grad()
    ing = [
        {"item": "all-purpose flour", "amount": "350 g (2¾ cups)"},
        {"item": "granulated sugar", "amount": "300 g (1½ cups)"},
        {"item": "unsalted butter, softened", "amount": "225 g (1 cup)"},
        {"item": "large eggs, room temperature", "amount": "4"},
        {"item": "baking powder", "amount": "2½ tsp"},
        {"item": "fine salt", "amount": "½ tsp"},
        {"item": "whole milk or buttermilk, room temperature", "amount": "240 ml (1 cup)"},
        {"item": flavor, "amount": "as needed"},
    ]
    if mixin:
        ing.append({"item": mixin, "amount": "100 g, for topping/folding"})
    ing.append({"item": frosting + " (butter, icing sugar, flavouring)", "amount": "enough for a 20 cm/8 in layer cake"})
    steps = [
        "Take the butter, eggs and milk out of the fridge at least an hour before you start so everything is properly at room temperature — cold ingredients won't emulsify smoothly into the batter.",
        "Preheat the oven to 175°C (350°F). Grease two 20 cm (8 in) round cake tins, line the bases with parchment circles, and dust the sides lightly with flour, tapping out the excess.",
        "In a medium bowl, whisk the flour, baking powder and salt together thoroughly so the leavening is evenly distributed, then set aside.",
        "In the bowl of a stand mixer fitted with the paddle (or using a hand mixer), beat the softened butter alone for 1 minute until smooth, then add the sugar and cream together on medium-high speed for 3-4 minutes, until noticeably pale, light and fluffy — this traps the air that gives the cake its rise.",
        "Add the eggs one at a time, beating well after each addition and scraping down the sides of the bowl, so each egg is fully incorporated before the next goes in.",
        f"Mix in {flavor} on low speed until just combined.",
        "With the mixer on low, add the flour mixture in three additions, alternating with the milk in two additions — start and finish with the flour. Mix only until each addition just disappears; stop as soon as no streaks of flour remain to avoid a tough, dense crumb.",
        "Divide the batter evenly between the two tins (weigh the filled tins on a kitchen scale if you have one, for perfectly level layers), then smooth the tops with an offset spatula and tap each tin firmly on the counter twice to release any large air bubbles.",
        "Bake for 28-32 minutes, rotating the tins halfway through for even colouring. The cakes are done when the tops spring back when lightly pressed and a skewer inserted into the centre comes out clean or with a few moist crumbs.",
        "Cool the cakes in their tins on a wire rack for 10 minutes — this lets them firm up enough to handle — then run a knife around the edge, turn them out onto the rack, peel off the parchment, and cool completely, at least 1 hour, before frosting.",
        f"While the cakes cool, make the {frosting}: beat the butter alone until pale and creamy, then add the icing sugar gradually on low speed to avoid a sugar cloud, before beating on high for 2-3 minutes until light, fluffy and spreadable.",
        "If either cake layer has domed on top, level it with a long serrated knife so the layers will stack flat and even.",
        "Place the first layer cut-side up on a cake board or stand, spread an even layer of frosting over the top with an offset spatula, then set the second layer on top, cut-side down.",
        "Spread a thin 'crumb coat' of frosting over the entire outside of the cake to seal in any loose crumbs, then chill in the fridge for 15-20 minutes until this layer is firm to the touch.",
        f"Apply a final, generous layer of frosting over the chilled crumb coat, smoothing the sides with a bench scraper and the top with an offset spatula" + (f", then finish with {mixin}." if mixin else "."),
        "Slice with a long, thin knife, wiping it clean between cuts. Store leftovers in an airtight container — at cool room temperature for up to 2 days, or in the fridge for up to 5, brought back to room temperature before serving.",
    ]
    add(name, "Cakes", "1 hr 20 min", "10-12 slices", "Intermediate", "cake", g, ing, steps,
        "Bring all your dairy and eggs to room temperature first — it makes the batter emulsify smoothly and gives an even crumb.")

# =========================================================
# 2. CUPCAKES — in-depth method
# =========================================================
cupcake_variants = [
    ("Vanilla Bean Cupcakes", "vanilla bean paste", "vanilla Swiss meringue buttercream", None),
    ("Double Chocolate Cupcakes", "cocoa powder and melted dark chocolate", "chocolate buttercream", "chocolate curls"),
    ("Salted Caramel Cupcakes", "a swirl of salted caramel sauce", "salted caramel buttercream", "flaky sea salt"),
    ("Red Velvet Cupcakes", "cocoa and buttermilk tang", "cream cheese frosting", None),
    ("Lemon Meringue Cupcakes", "lemon curd centre", "torched meringue topping", None),
    ("Peanut Butter Cup Cupcakes", "creamy peanut butter", "peanut butter frosting", "chopped mini peanut butter cups"),
    ("Carrot Cake Cupcakes", "grated carrot and cinnamon", "cream cheese frosting", "chopped pecans"),
    ("Strawberries & Cream Cupcakes", "diced fresh strawberries", "whipped vanilla frosting", "freeze-dried strawberry dust"),
    ("Pumpkin Spice Cupcakes", "pumpkin puree and pumpkin pie spice", "brown sugar cream cheese frosting", None),
    ("Cookies & Cream Cupcakes", "crushed chocolate sandwich cookies", "cookies and cream buttercream", "half a cookie on top"),
]
for name, flavor, frosting, mixin in cupcake_variants:
    g = grad()
    ing = [
        {"item": "all-purpose flour", "amount": "190 g (1½ cups)"},
        {"item": "granulated sugar", "amount": "150 g (¾ cup)"},
        {"item": "unsalted butter, softened", "amount": "115 g (½ cup)"},
        {"item": "large eggs, room temperature", "amount": "2"},
        {"item": "baking powder", "amount": "1½ tsp"},
        {"item": "fine salt", "amount": "¼ tsp"},
        {"item": "whole milk, room temperature", "amount": "120 ml (½ cup)"},
        {"item": flavor, "amount": "as needed"},
        {"item": frosting + " ingredients", "amount": "enough to pipe 12 cupcakes"},
    ]
    if mixin:
        ing.append({"item": mixin, "amount": "for decorating"})
    steps = [
        "Preheat the oven to 175°C (350°F) and line a 12-cup muffin tin with paper liners.",
        "Whisk the flour, baking powder and salt together in a bowl and set aside — breaking up any lumps now means a smoother batter later.",
        "Cream the softened butter and sugar together on medium-high speed for about 3 minutes until noticeably lighter in both colour and texture.",
        "Add the eggs one at a time, beating well and scraping the bowl between additions so nothing sits unmixed at the bottom.",
        f"Mix in {flavor} on low speed until evenly combined.",
        "Add the flour mixture in three additions, alternating with the milk in two, mixing on low speed just until each addition is incorporated — overmixing at this stage is the most common cause of dense, tough cupcakes.",
        "Divide the batter evenly among the liners using a spring-loaded ice cream scoop for consistency, filling each one about two-thirds full so there's room to rise without overflowing.",
        "Bake for 18-20 minutes, checking at the 18-minute mark: a toothpick inserted into the centre of a cupcake should come out clean, and the tops should spring back when pressed gently.",
        "Cool the cupcakes in the tin for 5 minutes — this lets the structure set — then transfer them to a wire rack and cool completely, at least 30 minutes, before frosting; warm cupcakes will melt the frosting.",
        f"While they cool, prepare the {frosting}, beating it on high speed for 2-3 minutes until light, smooth and holds soft peaks when the beater is lifted.",
        "Spoon the frosting into a piping bag fitted with your preferred tip (a large open star works well for a classic swirl).",
        "Pipe the frosting onto each cooled cupcake in a steady spiral, starting from the outside edge and working inward and up" + (f", then finish with {mixin}." if mixin else "."),
        "Serve the same day for the freshest texture, or store in an airtight container in the fridge for up to 3 days, bringing back to room temperature before eating.",
    ]
    add(name, "Cupcakes", "45 min", "12 cupcakes", "Easy", "cupcake", g, ing, steps,
        "Don't overfill the liners — two-thirds full gives you a nice domed top without overflowing.")

# =========================================================
# 3. COOKIES — in-depth method
# =========================================================
cookie_variants = [
    ("Classic Chocolate Chip Cookies", "250 g (1½ cups) semi-sweet chocolate chips", "none", "Fold the chips in at the end for pockets of melty chocolate in every bite."),
    ("Chewy Oatmeal Raisin Cookies", "150 g (1½ cups) rolled oats and 120 g (1 cup) raisins", "1 tsp cinnamon", "Soak the raisins in warm water for 10 minutes first so they stay plump after baking."),
    ("Peanut Butter Cookies", "200 g (¾ cup) smooth peanut butter", "none", "Press a criss-cross pattern on top with a fork before baking — it's classic and helps them cook evenly."),
    ("Snickerdoodles", "2 tbsp cinnamon-sugar coating", "1 tsp cream of tartar", "Roll each dough ball in the cinnamon sugar right before baking for that signature crackled top."),
    ("Soft Sugar Cookies", "1 tsp almond extract", "none", "Chill the dough for at least an hour so the cookies hold their shape and don't spread too thin."),
    ("Double Chocolate Fudge Cookies", "60 g (½ cup) extra cocoa powder and 150 g chocolate chunks", "none", "Slightly underbake these for a fudgy, brownie-like centre."),
    ("White Chocolate Macadamia Cookies", "150 g white chocolate chips and 100 g macadamia nuts", "none", "Toast the macadamias lightly first to bring out their buttery flavour."),
    ("Gingerbread Cookies", "2 tsp ground ginger, cinnamon and cloves, plus 3 tbsp molasses", "none", "These are perfect for cutting into shapes and decorating with royal icing."),
    ("Classic Shortbread", "none extra — let the butter shine", "none", "Use the best butter you can find; shortbread has so few ingredients that quality really shows."),
    ("Molasses Spice Cookies", "3 tbsp molasses and 1½ tsp mixed spice", "none", "Roll the dough balls in granulated sugar before baking for a lightly crackled, sparkly top."),
    ("Lemon Crinkle Cookies", "zest of 2 lemons and 2 tbsp lemon juice", "none", "Roll generously in icing sugar — the crackle effect as they bake is part of the fun."),
    ("Coconut Macaroons", "300 g (3⅓ cups) sweetened shredded coconut", "none", "Dip the cooled bases in melted dark chocolate for an extra treat."),
]
for name, mixin, extra_spice, tip in cookie_variants:
    g = grad()
    ing = [
        {"item": "all-purpose flour", "amount": "280 g (2¼ cups)"},
        {"item": "unsalted butter, softened", "amount": "225 g (1 cup)"},
        {"item": "brown sugar", "amount": "150 g (¾ cup)"},
        {"item": "granulated sugar", "amount": "100 g (½ cup)"},
        {"item": "large eggs", "amount": "1-2"},
        {"item": "vanilla extract", "amount": "1 tsp"},
        {"item": "baking soda", "amount": "1 tsp"},
        {"item": "fine salt", "amount": "½ tsp"},
        {"item": mixin, "amount": "as listed"},
    ]
    if extra_spice != "none":
        ing.append({"item": extra_spice, "amount": "as listed"})
    steps = [
        "Preheat the oven to 175°C (350°F) and line two baking sheets with parchment paper.",
        "Whisk the flour, baking soda and salt together in a bowl" + (f", along with the {extra_spice}" if extra_spice != "none" else "") + ", and set aside.",
        "Cream the softened butter with the brown and granulated sugar on medium-high speed for 2-3 minutes until noticeably light and fluffy — the brown sugar adds moisture and chew, so don't skip creaming it in properly.",
        "Beat in the egg(s) and vanilla extract one at a time, mixing until fully combined and scraping down the bowl as needed.",
        "Add the dry ingredients to the wet mixture in two additions, mixing on low speed just until the last streaks of flour disappear — overworking the dough here develops gluten and makes tough cookies.",
        f"Fold in {mixin} by hand with a spatula so it's evenly distributed without overmixing the dough.",
        "If the dough feels soft or sticky, chill it in the fridge for 20-30 minutes; this stops the cookies spreading too thin in the oven.",
        "Scoop rounded tablespoons of dough (about 30 g each) onto the prepared sheets, spacing them 5 cm (2 in) apart to allow for spreading.",
        "Bake one sheet at a time for 9-12 minutes, until the edges are set and lightly golden but the centres still look a touch underdone and soft — they'll firm up as they cool.",
        "Let the cookies rest on the hot baking sheet for 5 minutes so they finish setting, then transfer to a wire rack to cool completely.",
        "Store in an airtight container at room temperature for up to 5 days, or freeze the raw dough balls for up to 3 months and bake straight from frozen, adding an extra minute or two to the baking time.",
    ]
    add(name, "Cookies", "35 min", "24 cookies", "Easy", "cookie", g, ing, steps, tip)

# =========================================================
# 4. BROWNIES & BARS — in-depth method
# =========================================================
bar_variants = [
    ("Classic Fudge Brownies", "200 g dark chocolate, melted, plus 100 g chocolate chips", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment, leaving an overhang on two sides to lift the brownies out later.",
        "Melt the butter and dark chocolate together in a heatproof bowl set over a pan of gently simmering water, stirring occasionally until smooth and glossy; take it off the heat as soon as it melts.",
        "Whisk the sugar into the warm chocolate mixture until combined, then whisk in the eggs one at a time — whisking vigorously here for about 30 seconds per egg is what gives brownies their shiny, crackly top.",
        "Sift in the flour, cocoa powder and a pinch of salt, then fold gently with a spatula until just combined; stop as soon as no dry flour remains.",
        "Fold in the chocolate chips, then pour the batter into the prepared tin and spread it into an even layer with an offset spatula.",
        "Bake for 25-28 minutes. The brownies are ready when the top is set and crackly but a skewer inserted in the centre still comes out with a few moist crumbs clinging to it — this is what keeps them fudgy rather than cakey.",
        "Cool completely in the tin on a wire rack, at least 1 hour — this is essential, as warm brownies will crumble when cut.",
        "Lift the whole slab out using the parchment overhang, then slice into squares with a sharp knife, wiping the blade clean between cuts for neat edges.",
    ], "Underbake slightly and chill before slicing for the fudgiest texture."),
    ("Blondies", "200 g white chocolate chips and 100 g chopped pecans", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper, leaving an overhang for easy removal.",
        "Melt the butter in a saucepan over medium heat and continue cooking for 2-3 minutes, swirling often, until it turns golden brown and smells nutty — this brown butter step adds deep flavour, so don't rush it.",
        "Whisk the brown sugar into the hot browned butter until smooth, then let the mixture cool for 5 minutes before whisking in the eggs and vanilla, so you don't accidentally scramble the eggs.",
        "Fold in the flour and salt until just combined, then stir through the white chocolate chips and chopped pecans.",
        "Spread the thick batter evenly into the prepared tin, pushing it right into the corners.",
        "Bake for 22-25 minutes until the top is golden and a skewer comes out with a few moist crumbs; the centre should still look slightly soft.",
        "Cool completely in the tin before lifting out and cutting into bars.",
    ], "Brown butter the butter first for a deeper, nuttier flavour."),
    ("Lemon Bars", "zest and juice of 3 lemons for the curd layer", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Make the shortbread base: rub cold butter into the flour and sugar with your fingertips until the mixture resembles coarse crumbs, then press firmly and evenly into the base of the tin.",
        "Bake the base for 15 minutes until pale gold, while you prepare the filling.",
        "Whisk the eggs, sugar, lemon juice and zest together thoroughly until smooth and fully combined.",
        "Pour the lemon filling over the hot base immediately after it comes out of the oven, so the two layers bond together.",
        "Return to the oven and bake for a further 18-20 minutes, until the filling is just set — it should have a very slight wobble in the centre but no longer look liquid.",
        "Cool completely to room temperature, then chill in the fridge for at least 2 hours so the filling firms up fully before slicing.",
        "Lift out using the parchment, dust generously with icing sugar, and slice into squares with a sharp knife wiped clean between cuts.",
    ], "Line the tin with overhanging parchment so you can lift the whole slab out cleanly."),
    ("Rice Krispie Treats", "170 g mini marshmallows and 150 g crisped rice cereal", [
        "Line a 23 cm (9 in) square tin with parchment paper and lightly butter it.",
        "Melt the butter in a large pot over low heat until fully liquid.",
        "Add the marshmallows and stir continuously over low heat until completely melted and smooth, with no lumps remaining — keep the heat low so the marshmallow doesn't scorch.",
        "Remove the pot from the heat and fold in the crisped rice cereal with a spatula until every piece is evenly coated in the marshmallow mixture.",
        "Transfer to the prepared tin and press down firmly and evenly using a buttered spatula or the back of a buttered spoon — pressing too hard will make them dense, so use gentle, even pressure.",
        "Let cool at room temperature for at least 30 minutes until fully set before cutting into squares with a sharp, lightly buttered knife.",
    ], "Press gently, not hard — overpacking makes them dense instead of light and chewy."),
    ("Magic Bars", "sweetened condensed milk, chocolate chips, coconut and chopped nuts", [
        "Preheat the oven to 160°C (325°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Press the graham cracker crumb base evenly and firmly into the bottom of the tin using the back of a spoon.",
        "Layer the chocolate chips evenly over the base, followed by the shredded coconut, and finally the chopped nuts.",
        "Pour the sweetened condensed milk evenly and slowly over the top, making sure it seeps down to bind all the layers together.",
        "Bake for 25-30 minutes until the coconut on top is golden brown and the condensed milk is bubbling at the edges.",
        "Cool completely in the tin, then chill, ideally overnight, so the layers set firmly before slicing cleanly into bars.",
    ], "Let these sit overnight before cutting — they slice much more cleanly the next day."),
    ("Peanut Butter Bars", "200 g peanut butter swirled through the batter and a peanut butter glaze", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Cream the butter, peanut butter and sugars together until smooth and well combined, about 2 minutes.",
        "Beat in the eggs and vanilla until the mixture is light and fully incorporated.",
        "Fold in the flour, baking powder and salt until just combined, then spread the thick batter evenly into the prepared tin.",
        "Bake for 20-22 minutes until the edges are golden and the centre is just set with a slight softness.",
        "Cool completely in the tin, then whisk together a glaze of melted peanut butter and icing sugar loosened with a little milk, and drizzle it generously over the top before slicing.",
    ], "Use a natural, no-stir peanut butter for the smoothest batter."),
    ("Caramel Brownies", "a layer of soft caramel sauce swirled through the middle", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Make a fudge brownie batter by melting chocolate and butter together, whisking in sugar and eggs, then folding in the flour and cocoa.",
        "Pour half of the brownie batter into the prepared tin and spread evenly.",
        "Drizzle a generous, even layer of soft caramel or dulce de leche over the batter, keeping it away from the very edges so it doesn't leak during baking.",
        "Pour the remaining brownie batter over the caramel layer, spreading gently to cover it completely, then swirl the surface lightly with the tip of a knife for a marbled effect.",
        "Bake for 28-30 minutes until the top is set and a skewer inserted away from the caramel pocket comes out with moist crumbs.",
        "Cool completely in the tin, ideally with an hour in the fridge afterwards, so the caramel firms up enough to slice cleanly.",
    ], "Use thick dulce de leche rather than runny caramel so it doesn't sink to the bottom."),
    ("S'mores Bars", "crushed digestive biscuits, mini marshmallows and milk chocolate", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Mix the crushed digestive biscuits with melted butter and press into the base of the tin, then bake for 8 minutes to firm up.",
        "Pour a prepared fudge brownie batter over the hot base and spread evenly.",
        "Bake for 20 minutes until the brownie layer is almost set with a slight softness in the centre.",
        "Scatter mini marshmallows and chunks of milk chocolate generously over the top and return to the oven for 5 minutes, until the marshmallows are puffed and lightly toasted.",
        "For extra colour, finish briefly under a hot grill for 20-30 seconds, watching closely so the marshmallows don't burn.",
        "Cool for 15-20 minutes, then slice while still a little warm so the marshmallow stays gooey.",
    ], "Toast the marshmallow topping under the grill for a few seconds for a campfire finish."),
    ("Raspberry Crumb Bars", "300 g fresh or frozen raspberries", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Make an oat crumble mixture of flour, oats, butter and sugar, rubbing the butter in with your fingertips until it clumps into coarse crumbs.",
        "Press two-thirds of the crumble mixture firmly into the base of the tin to form an even layer.",
        "Toss the raspberries with sugar and a little cornflour, then spread this fruit mixture evenly over the base.",
        "Scatter the remaining one-third of the crumble mixture loosely over the fruit, leaving some gaps for a rustic, textured top.",
        "Bake for 35-40 minutes until the crumble topping is golden and the fruit filling is bubbling at the edges.",
        "Cool completely to room temperature, then chill for at least 1 hour — the fruit layer needs this time to firm up before you slice cleanly.",
    ], "Cool completely, even in the fridge, before cutting or the fruit layer will ooze."),
    ("Date & Walnut Bars", "chopped dates simmered into a sticky paste, plus walnuts", [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Simmer the chopped dates with a splash of water and a squeeze of lemon juice over low heat for 8-10 minutes, mashing occasionally, until they break down into a thick, spreadable paste.",
        "Make an oat crumble mixture of flour, oats, butter and a little sugar, rubbing together until it forms coarse, even crumbs.",
        "Press half of the crumble mixture into the base of the tin, spread the date paste evenly over the top, then scatter over the chopped walnuts.",
        "Cover with the remaining crumble mixture, pressing down very gently so it holds together without compacting the layers below.",
        "Bake for 30 minutes until the top is golden brown.",
        "Cool completely in the tin before lifting out and slicing into bars.",
    ], "No refined sugar needed here — the dates provide all the sweetness."),
]
for name, mixin, steps_custom, tip in bar_variants:
    g = grad()
    ing = [
        {"item": "unsalted butter", "amount": "170 g (¾ cup)"},
        {"item": "granulated or brown sugar", "amount": "200 g (1 cup)"},
        {"item": "large eggs", "amount": "2"},
        {"item": "all-purpose flour", "amount": "150 g (1¼ cups)"},
        {"item": "fine salt", "amount": "¼ tsp"},
        {"item": mixin, "amount": "as listed"},
    ]
    add(name, "Brownies & Bars", "55 min", "16 bars", "Easy", "brownie", g, ing, steps_custom, tip)

# =========================================================
# 5. PIES & TARTS — in-depth method
# =========================================================
pie_variants = [
    ("Classic Apple Pie", "6 Granny Smith apples, peeled and sliced, with cinnamon and brown sugar", "Double pie crust", "bake"),
    ("Pumpkin Pie", "pumpkin puree, evaporated milk, eggs and warm spices", "Single pie crust", "bake"),
    ("Pecan Pie", "corn syrup, brown sugar, eggs and 250 g pecan halves", "Single pie crust", "bake"),
    ("Key Lime Pie", "condensed milk, egg yolks and fresh lime juice", "Graham cracker crust", "bake"),
    ("Cherry Pie", "pitted cherries, sugar and a little cornflour to thicken", "Double pie crust", "bake"),
    ("Chocolate Cream Pie", "a rich stovetop chocolate custard and whipped cream topping", "Pre-baked pie crust", "chill"),
    ("Lemon Meringue Pie", "a tangy lemon curd filling topped with toasted meringue", "Pre-baked pie crust", "chill"),
    ("Banoffee Pie", "sliced bananas, thick caramel and whipped cream", "Digestive biscuit crust", "chill"),
    ("Fresh Fruit Tart", "vanilla pastry cream topped with glazed seasonal fruit", "Sweet shortcrust tart shell", "chill"),
    ("Chocolate Ganache Tart", "a silky dark chocolate and cream ganache", "Chocolate shortcrust tart shell", "chill"),
]
for name, filling, crust, method in pie_variants:
    g = grad()
    ing = [
        {"item": crust + " ingredients (flour, cold butter, ice water, pinch of salt)", "amount": "for a 23 cm (9 in) pie or tart tin"},
        {"item": filling, "amount": "as listed"},
        {"item": "granulated sugar", "amount": "100-150 g, to taste"},
        {"item": "large eggs (where needed)", "amount": "2-3"},
    ]
    if method == "bake":
        steps = [
            f"Make the {crust.lower()}: whisk the flour and a pinch of salt together, then cut in the cold, cubed butter using your fingertips or a pastry cutter until the mixture looks like coarse breadcrumbs with some pea-sized lumps remaining.",
            "Add ice water one tablespoon at a time, mixing with a fork until the dough just comes together — stop as soon as it holds when pressed, overworking it here makes a tough crust.",
            "Shape the dough into one or two discs, wrap tightly in clingfilm, and chill in the fridge for at least 30 minutes to relax the gluten and firm up the butter.",
            "On a lightly floured surface, roll the chilled dough out to about 3 mm thick and large enough to overhang a 23 cm (9 in) pie tin by about 2 cm.",
            "Ease the dough into the tin without stretching it, press it gently into the base and sides, then trim the excess and crimp the edges decoratively with your fingers or a fork.",
            f"Prepare the filling: combine {filling} according to the recipe, whisking the wet ingredients thoroughly and tossing any fruit with sugar and a thickener like cornflour so the juices set rather than run.",
            "Pour or arrange the filling into the lined pie tin, spreading it into an even layer.",
            "If making a double-crust pie, roll out the second disc of dough, lay it over the filling, trim and crimp the edges to seal, then cut a few small slits in the top to let steam escape; for a single crust, leave the filling exposed.",
            "Brush the top crust (or edges) with a beaten egg wash for a glossy, golden finish, and cover the edges loosely with foil if they're browning too quickly.",
            "Bake at 190°C (375°F) for 45-55 minutes, until the crust is deep golden brown and, for custard-style fillings, the centre has just a gentle wobble when the tin is nudged.",
            "Cool on a wire rack for at least 2 hours before slicing — this resting time lets the filling fully set so your slices hold their shape.",
        ]
    else:
        steps = [
            f"Make the {crust.lower()}: combine the crumbs or flour mixture with melted butter and press firmly and evenly into the base and up the sides of a 23 cm (9 in) pie or tart tin.",
            "If using a pastry crust, chill for 20 minutes then blind-bake: line with parchment and baking beans, bake at 190°C (375°F) for 12 minutes, remove the beans and parchment, and bake a further 8-10 minutes until golden. A biscuit crust can instead be chilled for 20 minutes or baked for 8 minutes to set.",
            "Cool the baked crust completely on a wire rack before filling it — a warm crust will melt a chilled filling.",
            f"Prepare the filling: whisk or cook {filling} on the stovetop as needed until smooth, thickened, and glossy, stirring constantly to prevent it catching on the bottom of the pan.",
            "Pour the warm filling into the cooled crust, smoothing the top with a spatula.",
            "If the recipe calls for a meringue topping, whisk egg whites to stiff, glossy peaks with sugar added gradually, then swirl or pipe it decoratively over the filling while still warm, and brown briefly under a hot grill or with a kitchen torch.",
            "Chill the assembled pie in the fridge for at least 4 hours, ideally overnight, until the filling is fully set and cold throughout.",
            "Just before serving, finish with any final topping — whipped cream, fruit, or a dusting of cocoa or sugar.",
            "Slice with a sharp knife dipped in hot water and wiped dry between cuts for the cleanest edges.",
        ]
    add(name, "Pies & Tarts", "1 hr 30 min (+ chilling)", "8 slices", "Intermediate", "pie", g, ing, steps,
        "Chill your pastry dough well and work quickly — cold butter is the secret to a flaky, not tough, crust.")

# =========================================================
# 5b. CRUMBLES & COBBLERS — in-depth method
# =========================================================
crumble_variants = [
    ("Classic Apple Crumble", ["Bramley or Granny Smith apples, peeled, cored and sliced", "granulated sugar", "lemon juice", "ground cinnamon"],
     "Toss the sliced apples with the sugar, a squeeze of lemon juice and the cinnamon in a large bowl, coating every piece evenly."),
    ("Rhubarb Crumble", ["fresh rhubarb, trimmed and chopped into 2 cm pieces", "granulated sugar", "orange juice and zest", "a little cornflour"],
     "Toss the chopped rhubarb with the sugar, orange juice and zest and a little cornflour, which helps thicken the sharp, juicy liquid rhubarb releases as it bakes."),
    ("Blackberry & Apple Crumble", ["Bramley apples, peeled, cored and sliced", "fresh or frozen blackberries", "granulated sugar", "a squeeze of lemon juice"],
     "Toss the sliced apples and blackberries together with the sugar and lemon juice, taking care not to crush the berries."),
    ("Peach Crumble", ["ripe peaches, stoned and sliced", "granulated sugar", "a few drops of almond extract", "a squeeze of lemon juice"],
     "Toss the sliced peaches with the sugar, almond extract and lemon juice until evenly coated."),
    ("Pear & Ginger Crumble", ["firm pears, peeled, cored and sliced", "golden syrup", "chopped stem ginger", "a squeeze of lemon juice"],
     "Toss the sliced pears with the golden syrup, chopped stem ginger and lemon juice until well coated."),
    ("Plum Crumble", ["ripe plums, halved, stoned and sliced", "granulated sugar", "ground cinnamon", "a squeeze of lemon juice"],
     "Toss the sliced plums with the sugar, cinnamon and lemon juice, letting them sit for a few minutes so the sugar starts to draw out their juices."),
    ("Mixed Berry Crumble", ["strawberries, hulled and halved", "blueberries", "raspberries", "granulated sugar and a little cornflour"],
     "Toss all the berries together gently with the sugar and cornflour, taking care not to crush them, especially the raspberries."),
    ("Apricot Crumble", ["ripe apricots, halved and stoned", "granulated sugar", "vanilla extract", "a squeeze of lemon juice"],
     "Toss the halved apricots with the sugar, vanilla and lemon juice until evenly coated."),
    ("Chocolate & Pear Crumble", ["firm pears, peeled, cored and sliced", "granulated sugar", "dark chocolate chips", "a squeeze of lemon juice"],
     "Toss the sliced pears with the sugar and lemon juice, then scatter in the chocolate chips so they melt into pockets through the fruit as it bakes."),
    ("Banana & Toffee Crumble", ["ripe bananas, sliced", "thick caramel or toffee sauce", "a squeeze of lemon juice", "a pinch of cinnamon"],
     "Toss the sliced bananas very gently with the lemon juice and cinnamon, then drizzle through half of the caramel sauce, reserving the rest for serving."),
]
for name, fruit_ing, fruit_step in crumble_variants:
    g = grad()
    ing = [{"item": i, "amount": "as needed"} for i in fruit_ing]
    ing += [
        {"item": "all-purpose flour", "amount": "180 g (1½ cups)"},
        {"item": "cold unsalted butter, cubed", "amount": "115 g (½ cup)"},
        {"item": "granulated or light brown sugar", "amount": "90 g (scant ½ cup)"},
        {"item": "rolled oats (optional, for extra crunch)", "amount": "40 g (⅓ cup)"},
        {"item": "pinch of fine salt", "amount": "1 pinch"},
        {"item": "custard, cream or vanilla ice cream, to serve", "amount": "as needed"},
    ]
    steps = [
        "Preheat the oven to 190°C (375°F) and lightly butter a medium baking dish (roughly 20 x 25 cm / 8 x 10 in, or similar capacity).",
        f"{fruit_step}",
        "Tip the prepared fruit into the baking dish and spread it out into an even layer — it should come close to the top of the dish, as fruit shrinks down considerably as it cooks.",
        "To make the crumble topping, rub the cold, cubed butter into the flour using your fingertips, lifting the mixture as you go to keep it light, until it resembles coarse breadcrumbs with a few slightly larger lumps — this takes about 3-4 minutes by hand.",
        "Stir in the sugar, oats (if using) and a pinch of salt, mixing just enough to combine without compacting the mixture — you want it to stay loose and crumbly, not pack into a dough.",
        "Scatter the crumble topping evenly over the fruit, right to the edges of the dish, without pressing it down — a loose, uneven scattering gives the best craggy, crisp texture once baked.",
        "Bake for 35-45 minutes, until the topping is deep golden brown and the fruit is bubbling up visibly at the edges of the dish.",
        "If the topping is browning too quickly before the fruit is fully tender, loosely cover the dish with foil for the final 10-15 minutes of baking.",
        "Remove from the oven and let the crumble rest for 10-15 minutes before serving — this gives the hot fruit juices time to settle so they don't immediately run everywhere when spooned out.",
        "Serve warm, spooned into bowls with a generous pour of custard, a dollop of cream, or a scoop of vanilla ice cream alongside.",
        "Store any leftovers covered in the fridge for up to 3 days, and reheat individual portions in the oven or microwave until piping hot before serving again.",
    ]
    add(name, "Crumbles & Cobblers", "1 hr", "6 servings", "Easy", "crumble", g, ing, steps,
        "Don't press the crumble topping down — keep it loose and craggy on top of the fruit for the crispest, most textured finish.")

# =========================================================
# 6. PUDDINGS & CUSTARDS — in-depth method
# =========================================================
pudding_variants = [
    ("Silky Chocolate Pudding", ["whole milk", "dark chocolate, chopped", "cocoa powder", "cornflour", "sugar", "egg yolks"], [
        "Whisk the sugar, cornflour and cocoa powder together in a saucepan while it's off the heat — mixing the dry ingredients first prevents lumps forming later.",
        "Gradually whisk in the milk and egg yolks, pouring slowly and whisking constantly until the mixture is completely smooth with no dry pockets.",
        "Set the saucepan over medium heat and cook, whisking constantly and scraping the bottom and corners of the pan, for 6-8 minutes.",
        "Keep whisking as the mixture heats — it will seem thin at first, then thicken quite suddenly once it reaches a gentle bubble; cook for 1 minute more once it does, still whisking, to fully activate the cornflour.",
        "Remove from the heat immediately and stir in the chopped chocolate, continuing to stir until it has fully melted and the pudding is glossy and smooth.",
        "Pour the pudding into individual serving glasses or one large bowl, then press a piece of clingfilm directly onto the surface to stop a skin forming.",
        "Chill for at least 2 hours, or until fully set and cold, before serving.",
    ]),
    ("Classic Vanilla Custard", ["whole milk", "egg yolks", "sugar", "cornflour", "vanilla bean or extract"], [
        "Heat the milk with the scraped vanilla bean (or extract) in a saucepan over medium heat until it's just steaming, with small bubbles forming at the edge — don't let it boil.",
        "Meanwhile, whisk the egg yolks, sugar and cornflour together in a bowl until pale and smooth.",
        "Slowly pour about a third of the hot milk into the egg mixture while whisking constantly — this tempers the eggs gently so they don't scramble.",
        "Pour the tempered egg mixture back into the saucepan with the remaining milk, whisking to combine.",
        "Cook over medium-low heat, stirring constantly with a wooden spoon or spatula in a figure-eight motion to reach every part of the pan, until the custard thickens enough to coat the back of the spoon, 4-6 minutes.",
        "Strain the custard through a fine sieve into a clean bowl to catch any bits of cooked egg, then cover with clingfilm pressed onto the surface.",
        "Chill for at least 1 hour before serving, or serve warm as a sauce.",
    ]),
    ("Classic Bread Pudding", ["stale bread or brioche, cubed", "whole milk", "eggs", "sugar", "cinnamon", "raisins (optional)"], [
        "Preheat the oven to 175°C (350°F) and butter a medium baking dish.",
        "Arrange the cubed bread evenly in the prepared dish, scattering in raisins between the layers if using.",
        "Whisk together the milk, eggs, sugar and cinnamon in a large bowl or jug until fully combined.",
        "Pour the custard mixture slowly and evenly over the bread, then press down gently on the cubes with a spatula so they all soak up some liquid.",
        "Let the dish sit for 20 minutes before baking, so the bread has time to fully absorb the custard rather than just sitting in it.",
        "Bake for 35-40 minutes until puffed, golden on top, and set in the centre with just a slight wobble.",
        "Serve warm, with a drizzle of cream, custard, or a dusting of extra cinnamon sugar.",
    ]),
    ("Classic Tiramisu", ["savoiardi (ladyfinger) biscuits", "strong brewed espresso", "mascarpone", "egg yolks", "sugar", "cocoa powder for dusting"], [
        "Brew the espresso and let it cool to room temperature in a shallow dish.",
        "Whisk the egg yolks and sugar together in a heatproof bowl set over a pan of gently simmering water, whisking constantly for 3-4 minutes until pale, thick and doubled in volume — this gently cooks the yolks for safety and stability.",
        "Remove from the heat and let cool slightly, then fold in the mascarpone a third at a time until the mixture is smooth with no lumps.",
        "Quickly dip each ladyfinger into the cooled espresso for no more than 1 second per side — any longer and they'll turn soggy rather than pleasantly moist.",
        "Arrange a layer of dipped ladyfingers in the base of a dish, then spread over half of the mascarpone mixture in an even layer.",
        "Repeat with a second layer of dipped ladyfingers and the remaining mascarpone mixture, smoothing the top.",
        "Cover and chill for at least 4 hours, ideally overnight, so the layers meld together and the biscuits soften fully.",
        "Just before serving, dust generously and evenly with cocoa powder through a fine sieve.",
    ]),
    ("Vanilla Bean Panna Cotta", ["double cream", "whole milk", "sugar", "vanilla bean", "gelatine leaves"], [
        "Submerge the gelatine leaves in a bowl of cold water and let them soften for 5-10 minutes.",
        "Meanwhile, heat the cream, milk, sugar and scraped vanilla bean together in a saucepan over medium heat, stirring until the sugar dissolves, and bring just to a simmer without letting it boil.",
        "Remove the pan from the heat. Lift the softened gelatine out of the water, squeezing out the excess, and whisk it into the warm cream mixture until it has completely dissolved with no visible strands.",
        "Strain the mixture through a fine sieve into a jug to remove the vanilla pod and any undissolved gelatine.",
        "Pour evenly into serving moulds or glasses.",
        "Chill for at least 4 hours, or ideally overnight, until fully set and no longer liquid in the centre when gently shaken.",
        "To turn out, dip each mould briefly in warm water, run a knife around the edge, and invert onto a plate; or simply serve in the glass.",
    ]),
    ("Classic Crème Brûlée", ["double cream", "egg yolks", "sugar", "vanilla bean", "extra sugar for the brûlée top"], [
        "Preheat the oven to 150°C (300°F) and place 4-6 ramekins in a deep roasting tin.",
        "Heat the cream with the scraped vanilla bean in a saucepan until just steaming, then remove from the heat and let it infuse for 10 minutes.",
        "Whisk the egg yolks and sugar together until pale, then slowly pour in the hot cream while whisking constantly to temper the eggs gently.",
        "Strain the mixture through a fine sieve into a jug to remove the vanilla pod and any bits of cooked egg, then divide evenly among the ramekins.",
        "Pour hot water into the roasting tin until it reaches halfway up the sides of the ramekins — this water bath insulates the custards for gentle, even cooking.",
        "Bake for 35-40 minutes until the custards are set at the edges but still have a gentle wobble in the centre.",
        "Carefully remove the ramekins from the water bath, cool to room temperature, then chill for at least 2 hours.",
        "Just before serving, sprinkle an even, thin layer of sugar over each custard and caramelise with a kitchen torch, moving it constantly until deep golden and crisp.",
    ]),
    ("Southern Banana Pudding", ["vanilla wafer biscuits", "sliced ripe bananas", "whole milk", "egg yolks", "sugar", "whipped cream"], [
        "Make a vanilla custard: whisk the milk, egg yolks, sugar and cornflour together, then cook over medium heat, stirring constantly, until thickened enough to coat the back of a spoon.",
        "Remove the custard from the heat and let it cool for 10 minutes, stirring occasionally to stop a skin forming.",
        "In a serving dish, layer vanilla wafers across the base, followed by a layer of sliced banana, then a generous layer of the warm custard.",
        "Repeat the layers — wafers, banana, custard — until the dish is full, finishing with a layer of custard on top.",
        "Cover and chill for at least 3 hours, which allows the wafers to soften into a soft, cake-like texture.",
        "Just before serving, top with freshly whipped cream and a few extra banana slices.",
    ]),
    ("Butterscotch Pudding", ["brown sugar", "butter", "whole milk", "double cream", "egg yolks", "cornflour", "vanilla"], [
        "Melt the butter in a saucepan over medium heat, then add the brown sugar and cook, stirring constantly, for about 2 minutes until it becomes thick, glossy and fragrant.",
        "Carefully whisk in the milk and cream — the mixture will bubble and seize up at first, so add it gradually and keep whisking until smooth, then bring back to a gentle simmer.",
        "In a separate bowl, whisk the egg yolks and cornflour together, then slowly whisk in a ladleful of the hot butterscotch mixture to temper the eggs.",
        "Pour the tempered eggs back into the pan and cook over medium-low heat, whisking constantly, until thickened, about 4-5 minutes.",
        "Remove from the heat, stir in the vanilla, then pour into serving glasses.",
        "Press clingfilm onto the surface of each pudding and chill for at least 2 hours until set and cold.",
        "Finish with a little whipped cream just before serving.",
    ]),
    ("Sticky Toffee Pudding", ["chopped dates", "boiling water", "bicarbonate of soda", "butter", "brown sugar", "eggs", "flour", "toffee sauce"], [
        "Preheat the oven to 175°C (350°F) and grease a baking dish.",
        "Pour boiling water over the chopped dates in a bowl, stir in the bicarbonate of soda, and let the mixture sit for 10 minutes — it will foam up slightly as the dates soften.",
        "Blend or mash the soaked dates with their soaking liquid into a smooth, thick paste.",
        "Cream the butter and brown sugar together until light and fluffy, then beat in the eggs one at a time.",
        "Fold in the flour until just combined, then fold in the date paste until the batter is evenly speckled and no streaks remain.",
        "Pour the batter into the prepared dish and bake for 30-35 minutes, until risen, springy to the touch, and a skewer comes out clean.",
        "While the pudding bakes, make a toffee sauce by melting butter, brown sugar and cream together in a saucepan, stirring until smooth and glossy.",
        "While the sponge is still warm, poke holes all over the surface with a skewer and pour over a generous amount of the warm toffee sauce, letting it soak in before serving the rest alongside.",
    ]),
]
for name, ing_list, steps in pudding_variants:
    g = grad()
    ing = [{"item": i, "amount": "to taste / as needed"} for i in ing_list]
    add(name, "Puddings & Custards", "40 min (+ chilling)", "6 servings", "Easy", "pudding", g, ing, steps,
        "Patience pays off — most custards and puddings taste even better after a few hours chilling in the fridge.")

# =========================================================
# 6b. RICE PUDDINGS — in-depth method
# =========================================================
rice_pudding_variants = [
    ("Classic Creamy Rice Pudding", ["pudding or arborio rice", "whole milk", "granulated sugar", "vanilla extract", "ground cinnamon or nutmeg, to finish"], [
        "Rinse the rice briefly under cold water to remove excess surface starch, then drain well.",
        "Combine the rice, milk, sugar and vanilla in a heavy-bottomed pot — a heavy base is essential, as it prevents the rice from catching and burning on the bottom during the long, slow cook.",
        "Bring to a gentle simmer over medium heat, stirring regularly so the rice doesn't settle and stick.",
        "Reduce the heat to low and cook uncovered for 35-40 minutes, stirring every few minutes, until the rice is fully tender and the mixture has thickened into a loose, creamy pudding that coats the back of a spoon.",
        "If the mixture becomes too thick before the rice is fully tender, stir in a splash more milk and continue cooking gently.",
        "Taste and adjust the sweetness if needed, then remove from the heat — it will continue to thicken slightly as it cools.",
        "Serve warm, or transfer to a bowl, cover and chill if you prefer it cold, dusting with cinnamon or nutmeg just before serving.",
    ]),
    ("Traditional Baked Rice Pudding", ["pudding rice", "whole milk", "granulated sugar", "a knob of butter", "a whole nutmeg, for grating"], [
        "Preheat the oven to 150°C (300°F) and butter a medium baking dish.",
        "Scatter the rice evenly over the base of the dish, then sprinkle over the sugar.",
        "Pour the milk over the rice and sugar, and stir gently just once or twice to distribute the rice evenly — don't overmix, as the classic version relies on the rice settling naturally.",
        "Dot the surface with small pieces of butter, then grate fresh nutmeg generously over the top.",
        "Bake uncovered for 2-2½ hours, without stirring, until a golden-brown skin has formed on top and the rice underneath is completely tender and creamy.",
        "Check after about 45 minutes and gently press any rice grains that have floated to the surface back under the milk with the back of a spoon, so they don't dry out and harden.",
        "Remove from the oven once the skin is deep golden and the pudding has a gentle wobble when the dish is nudged.",
        "Serve warm, straight from the dish, with a spoonful of jam on the side if you like — a classic British touch.",
    ]),
    ("Coconut Rice Pudding", ["jasmine or short-grain rice", "full-fat coconut milk", "whole milk", "sugar", "a pinch of salt", "toasted coconut flakes, to finish"], [
        "Rinse the rice under cold water until the water runs mostly clear, then drain well.",
        "Combine the rice, coconut milk, whole milk, sugar and a pinch of salt in a heavy-bottomed pot.",
        "Bring to a gentle simmer over medium heat, stirring occasionally to stop the rice catching on the bottom.",
        "Reduce the heat to low and cook uncovered for 30-35 minutes, stirring every few minutes, until the rice is tender and the mixture has thickened to a rich, creamy consistency.",
        "If it thickens too much before the rice is fully cooked, loosen with a splash more coconut milk.",
        "Remove from the heat and let it rest for 5 minutes — coconut-based puddings continue to thicken noticeably as they sit.",
        "Spoon into bowls and finish with a scattering of toasted coconut flakes, serving warm or chilled.",
    ]),
    ("Cardamom Pistachio Rice Pudding (Kheer)", ["basmati rice", "whole milk", "sugar", "ground cardamom", "chopped pistachios and almonds", "a pinch of saffron (optional)"], [
        "Rinse the basmati rice well, then soak it in water for 20 minutes and drain — this shortens the cooking time and helps the grains break down into the pudding.",
        "Bring the milk to a gentle simmer in a heavy-bottomed pot, then add the drained rice.",
        "Cook over low heat, stirring frequently, for 35-45 minutes, until the rice has broken down and the milk has reduced and thickened considerably, taking on a pale golden colour.",
        "Stir in the sugar, ground cardamom and saffron (if using), and continue cooking for a further 5-10 minutes until fully dissolved and fragrant.",
        "Stir in most of the chopped pistachios and almonds, reserving a little for garnish.",
        "Remove from the heat — the kheer will continue to thicken as it cools, so it should still look slightly loose at this stage.",
        "Serve warm or chilled, scattered with the reserved nuts just before serving.",
    ]),
    ("Chocolate Rice Pudding", ["pudding or arborio rice", "whole milk", "granulated sugar", "cocoa powder", "dark chocolate, chopped", "vanilla extract"], [
        "Combine the rice, milk and half the sugar in a heavy-bottomed pot and bring to a gentle simmer over medium heat.",
        "Reduce the heat to low and cook uncovered for 30 minutes, stirring regularly, until the rice is nearly tender.",
        "Whisk the cocoa powder with the remaining sugar in a small bowl to break up any lumps, then stir this into the pot.",
        "Continue cooking for a further 5-10 minutes, stirring frequently, until the rice is fully tender and the mixture is a rich, even brown.",
        "Remove from the heat and stir in the chopped dark chocolate and vanilla, stirring until the chocolate has fully melted into a glossy, thick pudding.",
        "Taste and add a touch more sugar if needed, keeping in mind dark chocolate adds a slightly bitter edge.",
        "Serve warm, or chill for a denser, more mousse-like texture, with a few chocolate shavings on top.",
    ]),
    ("Salted Caramel Rice Pudding", ["pudding or arborio rice", "whole milk", "double cream", "light brown sugar", "butter", "flaky sea salt"], [
        "Melt the butter with the brown sugar in the heavy-bottomed pot you'll cook the pudding in, over medium heat, stirring until it turns a deep amber and smells of caramel, about 2-3 minutes.",
        "Carefully whisk in a splash of the milk — it will bubble and spit, so add it slowly and keep whisking until smooth.",
        "Stir in the remaining milk and the rice, then bring to a gentle simmer.",
        "Reduce the heat to low and cook uncovered for 35-40 minutes, stirring regularly, until the rice is tender and the mixture has thickened into a rich, caramel-coloured pudding.",
        "Stir in the double cream and a generous pinch of flaky sea salt, cooking for a further 2-3 minutes to warm it through.",
        "Taste and adjust the salt — it should taste distinctly salted-caramel, not just sweet.",
        "Serve warm, finished with an extra pinch of flaky salt and, if you like, a drizzle of extra caramel sauce.",
    ]),
    ("Arroz con Leche (Cinnamon-Orange Rice Pudding)", ["short-grain rice", "whole milk", "a cinnamon stick", "strips of orange zest", "granulated sugar", "ground cinnamon, to finish"], [
        "Place the milk, cinnamon stick and strips of orange zest in a heavy-bottomed pot and bring to a gentle simmer over medium heat.",
        "Let the milk infuse with the cinnamon and zest for 5-10 minutes over low heat before continuing, so their flavour fully comes through.",
        "Remove and discard the cinnamon stick and zest strips, then stir in the rice.",
        "Cook uncovered over low heat for 30-35 minutes, stirring frequently, until the rice is tender and the mixture has thickened to a loose, creamy consistency.",
        "Stir in the sugar during the final 10 minutes of cooking, tasting and adjusting the sweetness to your liking.",
        "Remove from the heat and let the pudding rest for a few minutes — it will thicken further as it cools slightly.",
        "Spoon into bowls and dust generously with ground cinnamon before serving, warm or chilled.",
    ]),
    ("Spiced Raisin Rice Pudding", ["pudding or arborio rice", "whole milk", "granulated sugar", "raisins or sultanas", "ground cinnamon and mixed spice", "a knob of butter"], [
        "Soak the raisins in a little warm water or orange juice for 10 minutes so they plump up rather than staying hard and chewy in the finished pudding, then drain.",
        "Combine the rice, milk, sugar, cinnamon and mixed spice in a heavy-bottomed pot and bring to a gentle simmer over medium heat.",
        "Reduce the heat to low and cook uncovered for 30 minutes, stirring frequently to stop the rice catching.",
        "Stir in the drained raisins and continue cooking for a further 5-10 minutes, until the rice is fully tender and the pudding has thickened nicely.",
        "Stir in a knob of butter at the end for extra richness and a glossy finish.",
        "Taste and adjust the spicing — this pudding should taste warm and fragrant, almost like a loose Christmas pudding.",
        "Serve warm, with an extra dusting of cinnamon on top.",
    ]),
    ("Lemon & Vanilla Bean Rice Pudding", ["pudding or arborio rice", "whole milk", "granulated sugar", "zest of 1 lemon", "a vanilla bean, split and scraped", "a squeeze of lemon juice"], [
        "Combine the milk, sugar, lemon zest and scraped vanilla bean (seeds and pod) in a heavy-bottomed pot.",
        "Bring to a gentle simmer over medium heat, then stir in the rice.",
        "Reduce the heat to low and cook uncovered for 35-40 minutes, stirring regularly, until the rice is tender and the pudding has thickened to a loose, creamy consistency.",
        "Remove and discard the vanilla pod once the flavour has fully infused.",
        "Stir in a small squeeze of lemon juice right at the end, off the heat — this brightens the pudding without curdling the milk, which can happen if added too early or over direct heat.",
        "Taste and adjust the lemon and sweetness to balance — it should taste bright and fragrant, not sharp.",
        "Serve warm or chilled, with an extra curl of lemon zest on top.",
    ]),
    ("Thai Black Rice Pudding", ["Thai black glutinous rice", "coconut milk", "sugar", "a pinch of salt", "sliced mango or banana, to serve"], [
        "Rinse the black glutinous rice thoroughly, then soak it in plenty of water for at least 4 hours, or ideally overnight — black rice is much firmer than white rice and needs this soak to cook through evenly.",
        "Drain the soaked rice and place it in a pot with fresh water, enough to cover by about 3 cm.",
        "Bring to a simmer and cook uncovered for 30-40 minutes, stirring occasionally and topping up with water if it looks dry, until the rice is tender and has released a deep purple colour into the liquid.",
        "Stir in most of the coconut milk, the sugar and a pinch of salt, reserving a little coconut milk to drizzle over at the end.",
        "Continue simmering gently for a further 10-15 minutes, stirring often, until the mixture thickens into a rich, porridge-like pudding.",
        "Taste and adjust the sweetness, then remove from the heat.",
        "Serve warm, in bowls, drizzled with the reserved coconut milk and topped with slices of fresh mango or banana.",
    ]),
]
for name, ing_list, steps in rice_pudding_variants:
    g = grad()
    ing = [{"item": i, "amount": "to taste / as needed"} for i in ing_list]
    add(name, "Rice Puddings", "50 min (+ resting)", "6 servings", "Easy", "ricepudding", g, ing, steps,
        "Stir often and keep the heat low — rice puddings thicken gradually, and rushing with high heat just catches the rice on the bottom of the pan.")

# =========================================================
# 7. ICE CREAM & FROZEN — in-depth method
# =========================================================
icecream_variants = [
    ("Classic Vanilla Bean Ice Cream", ["double cream", "whole milk", "sugar", "egg yolks", "vanilla bean"]),
    ("Rich Chocolate Ice Cream", ["double cream", "whole milk", "sugar", "egg yolks", "cocoa powder and melted dark chocolate"]),
    ("Fresh Strawberry Ice Cream", ["double cream", "whole milk", "sugar", "egg yolks", "pureed fresh strawberries"]),
    ("Mint Chocolate Chip Ice Cream", ["double cream", "whole milk", "sugar", "egg yolks", "peppermint extract and chopped dark chocolate"]),
    ("Cookies and Cream Ice Cream", ["double cream", "whole milk", "sugar", "egg yolks", "crushed chocolate sandwich cookies"]),
    ("Mango Sorbet", ["pureed ripe mango", "sugar", "water", "lime juice"]),
    ("Affogato", ["good vanilla ice cream", "freshly pulled espresso"]),
    ("Ice Cream Sandwiches", ["soft chocolate chip cookies", "softened vanilla ice cream"]),
    ("Frozen Yogurt Bark", ["Greek yogurt", "honey", "mixed berries", "granola"]),
    ("Classic Semifreddo", ["double cream", "egg yolks", "sugar", "vanilla or fruit puree"]),
]
for name, ing_list in icecream_variants:
    g = grad()
    ing = [{"item": i, "amount": "to taste / as needed"} for i in ing_list]
    if "Sorbet" in name:
        steps = [
            "Puree the ripe mango in a blender or food processor with the sugar and lime juice until completely smooth, with no lumps of fruit remaining.",
            "Taste the puree — it should taste slightly oversweet, since freezing dulls sweetness — and adjust with a little more sugar or lime juice if needed.",
            "Stir in the water a little at a time until the mixture reaches a light, easily pourable consistency.",
            "Chill the mixture thoroughly in the fridge for at least 2 hours, or until completely cold — a cold base churns faster and freezes smoother.",
            "Churn in an ice cream maker according to the manufacturer's instructions, usually 20-25 minutes, until it reaches a soft-serve consistency.",
            "Transfer to a lidded container, press a piece of baking paper onto the surface, and freeze for at least 3 hours until firm enough to scoop.",
        ]
    elif name == "Affogato":
        steps = [
            "Choose small, sturdy glasses or cups that can handle hot liquid.",
            "Scoop a generous ball of good-quality vanilla ice cream into each glass just before serving — don't do this too far ahead, or it will soften too much.",
            "Pull a fresh shot of hot espresso per serving, using freshly ground coffee for the best flavour.",
            "Bring the ice cream and the espresso to the table separately, then pour the hot espresso directly over the ice cream right in front of your guests.",
            "Serve immediately with a small spoon, enjoying the contrast between the hot coffee and the melting cold ice cream.",
        ]
    elif name == "Ice Cream Sandwiches":
        steps = [
            "Bake a batch of soft chocolate chip cookies, slightly underbaking them so they stay chewy, and let them cool completely on a wire rack.",
            "Let a tub of ice cream sit at room temperature for 5-10 minutes to soften slightly, making it easier to scoop and spread without shattering the cookies.",
            "Lay out half of the cookies flat-side up, then place a generous scoop of softened ice cream in the centre of each.",
            "Top with a second cookie, flat-side down, and press down gently and evenly until the ice cream spreads to the edges.",
            "Wrap each sandwich individually in cling film or baking paper to keep its shape, then freeze for at least 1 hour to firm up before serving.",
        ]
    elif name == "Frozen Yogurt Bark":
        steps = [
            "Line a baking tray with parchment paper, making sure it's flat so the mixture sets in an even layer.",
            "Mix the Greek yogurt with honey to taste in a bowl until smooth and well combined.",
            "Pour the yogurt mixture onto the tray and spread it out evenly with an offset spatula to a thickness of about 1 cm.",
            "Scatter mixed berries and granola generously and evenly over the top, pressing down very lightly so they stick to the yogurt rather than rolling off.",
            "Freeze for at least 3 hours, or until completely solid all the way through.",
            "Break or cut into uneven shards with a sharp knife, and serve straight from the freezer as it melts quickly.",
        ]
    elif name == "Classic Semifreddo":
        steps = [
            "Line a loaf tin with clingfilm or baking paper, leaving plenty of overhang on all sides to make unmoulding easy later.",
            "Whisk the egg yolks and sugar together in a heatproof bowl set over a pan of gently simmering water, whisking constantly for 4-5 minutes until pale, thick, and doubled in volume.",
            "Remove from the heat and continue whisking occasionally as it cools to room temperature, so it doesn't deflate.",
            "In a separate bowl, whip the double cream to soft peaks — it should hold its shape but still look glossy, not stiff or grainy.",
            "Gently fold the whipped cream and your chosen flavouring into the cooled egg mixture in two additions, using a large spatula and folding carefully to keep as much air in as possible.",
            "Pour the mixture into the lined loaf tin, smoothing the top, then fold the overhanging clingfilm over to cover.",
            "Freeze for at least 6 hours, ideally overnight, until completely firm.",
            "To serve, unfold the clingfilm, invert the tin onto a board, and slice with a knife warmed under hot water.",
        ]
    else:
        steps = [
            "Heat the milk and half the sugar in a saucepan over medium heat until just steaming, with small bubbles at the edge — do not let it boil.",
            "In a separate bowl, whisk the egg yolks with the remaining sugar until pale and slightly thickened.",
            "Slowly pour about a third of the hot milk into the egg mixture while whisking constantly, to gently warm the eggs without scrambling them.",
            "Pour the tempered egg mixture back into the saucepan with the rest of the milk, and cook over medium-low heat, stirring constantly with a spatula, until the custard thickens enough to coat the back of a spoon — this takes about 5-8 minutes; do not let it boil or it will curdle.",
            "Strain the custard through a fine sieve into a clean bowl to remove any bits of cooked egg.",
            "Stir in the cream and your chosen flavouring while the custard is still warm, then cover and chill the base thoroughly in the fridge, ideally overnight, so it's completely cold before churning.",
            "Churn the cold base in an ice cream maker according to the manufacturer's instructions, usually 20-25 minutes, until it thickens to a soft-serve consistency.",
            "Transfer to a lidded container and freeze for at least 3 hours, or until firm enough to scoop neatly.",
        ]
    add(name, "Ice Cream & Frozen", "30 min (+ freezing)", "6 servings", "Intermediate", "icecream", g, ing, steps,
        "Chill your custard base overnight before churning — a cold base churns faster and gives a creamier texture.")

# =========================================================
# 8. PASTRIES — in-depth method
# =========================================================
pastry_variants = [
    ("Buttery Croissants", ["strong white flour", "fresh yeast", "milk", "sugar", "salt", "cold unsalted butter for laminating"], [
        "Make a simple yeasted dough by mixing the flour, yeast, milk, sugar and salt into a smooth ball, then knead for 5 minutes until elastic.",
        "Shape the dough into a rectangle, wrap, and chill in the fridge for at least 1 hour to relax the gluten.",
        "Meanwhile, pound a block of cold butter between two sheets of parchment with a rolling pin into a flat, even rectangle about half the size of your dough.",
        "Roll the chilled dough out and place the butter block in the centre, then fold the dough over to fully encase it, pinching the edges to seal.",
        "Roll the dough out into a long rectangle, then fold it in thirds like a letter — this is your first 'turn'. Wrap and chill for 30 minutes.",
        "Repeat the rolling and folding process two more times, chilling for 30 minutes between each turn, to build up dozens of thin, alternating layers of dough and butter.",
        "After the final turn and chill, roll the laminated dough out thinly into a large rectangle, then cut into long triangles.",
        "Starting from the wide end of each triangle, roll it up towards the point to form the classic croissant shape, curving the ends inward slightly.",
        "Place the shaped croissants on lined baking sheets, spaced well apart, and prove in a warm spot for 1.5-2 hours, until noticeably puffy and almost doubled.",
        "Brush gently with egg wash, taking care not to press down and flatten the layers.",
        "Bake at 200°C (400°F) for 16-18 minutes, until deep golden brown and crisp, rotating the sheet halfway through for even colour.",
        "Cool on a wire rack for at least 10 minutes before eating — they're best enjoyed warm the same day.",
    ]),
    ("Cinnamon Rolls", ["enriched yeasted dough", "softened butter", "brown sugar", "ground cinnamon", "cream cheese icing"], [
        "Make an enriched, slightly sweet yeasted dough using flour, milk, egg, butter, sugar and yeast, kneading for about 8 minutes until smooth and elastic.",
        "Place the dough in a greased bowl, cover, and let it rise in a warm spot for about 1 hour, until doubled in size.",
        "Punch down the risen dough and roll it out on a floured surface into a large rectangle, about 1 cm thick.",
        "Spread the softened butter evenly over the entire surface, right to the edges, then sprinkle generously and evenly with brown sugar and cinnamon.",
        "Starting from one long edge, roll the dough up tightly into a log, keeping the roll even and snug throughout.",
        "Using unflavoured dental floss or a sharp serrated knife, slice the log into even rounds about 4 cm thick.",
        "Arrange the rolls cut-side up in a greased baking dish, leaving a little space between them to allow for a second rise.",
        "Cover and let prove again for 30-45 minutes, until puffy and touching each other.",
        "Bake at 175°C (350°F) for 22-25 minutes, until golden brown on top and cooked through in the centre.",
        "While still warm, drizzle generously with cream cheese icing so it melts slightly into the swirls.",
    ]),
    ("Danish Pastry", ["laminated yeasted dough", "pastry cream or fruit filling", "egg wash", "icing glaze"], [
        "Make a laminated yeasted dough following the same lamination technique as croissants — encasing butter in the dough and folding it in thirds three times, chilling between each fold.",
        "After the final chill, roll the dough out into a large rectangle about 4 mm thick.",
        "Cut the dough into even squares, roughly 10 cm per side.",
        "Spoon a small amount of pastry cream or fruit filling into the centre of each square, then fold the corners in towards the middle to create a pinwheel, or fold two opposite corners over the filling to form a simple pocket.",
        "Arrange the shaped pastries on lined baking sheets and prove in a warm spot for 45 minutes to 1 hour, until visibly puffy.",
        "Brush the exposed dough with egg wash, avoiding the filling.",
        "Bake at 200°C (400°F) for 15-18 minutes, until deep golden brown and the layers have visibly separated.",
        "Let cool for 10-15 minutes until just warm, then drizzle with a thin icing glaze made from icing sugar and a little milk or lemon juice.",
    ]),
    ("Classic Chocolate Éclairs", ["choux pastry (butter, water, flour, eggs)", "vanilla pastry cream", "dark chocolate ganache"], [
        "Preheat the oven to 200°C (400°F) and line a baking sheet with parchment paper.",
        "Bring the butter and water to a rolling boil in a saucepan, then remove from the heat and immediately tip in all the flour at once, beating vigorously with a wooden spoon until the mixture forms a smooth ball that pulls cleanly away from the sides of the pan.",
        "Return the pan to low heat for 1-2 minutes, stirring constantly, to cook out some of the raw flour taste and dry the dough slightly — you'll see a thin film form on the base of the pan.",
        "Transfer the dough to a mixing bowl and let it cool for 5 minutes, then beat in the eggs one at a time, making sure each is fully incorporated before adding the next; the finished dough should be smooth, glossy, and fall slowly off the spoon in a 'V' shape.",
        "Spoon the choux pastry into a piping bag fitted with a large round tip, and pipe straight lines about 12 cm long onto the prepared tray, spacing them well apart.",
        "Bake for 20-25 minutes without opening the oven door — opening it too early can cause the pastry to collapse — until puffed, deep golden, and firm, hollow-sounding when tapped underneath.",
        "Cool completely on a wire rack, then use a skewer to poke a small hole in one end of each shell.",
        "Make the vanilla pastry cream, then transfer it to a piping bag fitted with a small round tip and pipe it generously into each shell through the hole until you feel it resist, meaning it's full.",
        "Melt the dark chocolate with a little cream to make a glossy ganache, then dip the top of each filled éclair into it, letting the excess drip off.",
        "Let the ganache set for 10-15 minutes at room temperature before serving.",
    ]),
    ("Cream Puffs (Profiteroles)", ["choux pastry (butter, water, flour, eggs)", "whipped cream or pastry cream", "warm chocolate sauce"], [
        "Preheat the oven to 200°C (400°F) and line a baking sheet with parchment paper.",
        "Make the choux pastry as for éclairs: boil butter and water, beat in the flour off the heat until a smooth ball forms, cook briefly to dry it out, then beat in the eggs one at a time until smooth and glossy.",
        "Pipe or spoon the choux pastry into small rounds, about 4 cm wide, spacing them well apart on the tray to allow for puffing.",
        "Bake for 20-22 minutes until golden, puffed, and firm to the touch, without opening the oven door during baking.",
        "Cool completely on a wire rack, then slice each puff in half horizontally, or poke a small hole in the base.",
        "Fill generously with whipped cream or pastry cream, either by spooning into the sliced puffs or piping through the hole.",
        "Stack the filled puffs on a serving plate just before serving.",
        "Warm the chocolate sauce gently and drizzle it generously over the stacked puffs at the table.",
    ]),
    ("Honey Baklava", ["filo pastry sheets", "melted butter", "chopped walnuts and pistachios", "cinnamon", "honey syrup"], [
        "Preheat the oven to 160°C (325°F) and butter a baking tin that fits your filo sheets.",
        "Mix the chopped walnuts and pistachios with cinnamon and a little sugar in a bowl.",
        "Lay one sheet of filo in the tin and brush thoroughly with melted butter, making sure to reach the edges and corners; repeat with 6-8 sheets, buttering each one.",
        "Scatter a third of the nut mixture evenly over the layered filo.",
        "Add another 4-5 buttered filo sheets, then another third of the nuts, repeating until all the nuts are used, finishing with a final stack of 6-8 buttered filo sheets on top.",
        "Using a sharp knife, score the top layers into diamond or square shapes before baking — this makes it much easier to cut cleanly once it's baked and syrup-soaked.",
        "Bake for 40-45 minutes, until the top is golden brown and crisp throughout.",
        "While the baklava bakes, make a honey syrup by simmering honey, sugar, water and a squeeze of lemon juice together for 5-10 minutes until slightly thickened.",
        "As soon as the baklava comes out of the oven, pour the warm syrup evenly over the hot pastry, making sure it reaches into the scored cuts.",
        "Let the baklava sit uncovered for at least 4 hours, or ideally overnight, so the syrup fully soaks in and the layers crisp back up before cutting along the scored lines.",
    ]),
    ("Spanish Churros", ["water", "butter", "flour", "eggs", "cinnamon sugar for coating", "oil for frying"], [
        "Bring the water, butter and a pinch of salt to a rolling boil in a saucepan.",
        "Remove from the heat and tip in the flour all at once, beating vigorously with a wooden spoon until a smooth, thick dough forms and pulls away from the sides of the pan.",
        "Let the dough cool for 5 minutes, then beat in the eggs one at a time until the dough is smooth, glossy, and holds its shape when piped.",
        "Heat oil in a deep pan or fryer to 180°C (350°F) — test with a small piece of dough, which should sizzle and rise immediately.",
        "Spoon the dough into a piping bag fitted with a large star tip, and pipe strips about 12 cm long directly into the hot oil, cutting them off with scissors, and frying 3-4 at a time so the oil temperature doesn't drop.",
        "Fry for 2-3 minutes, turning once, until deep golden brown and crisp on the outside.",
        "Remove with a slotted spoon and drain briefly on paper towels.",
        "While still hot, toss the churros immediately in a bowl of cinnamon sugar until fully coated.",
        "Serve warm, with melted chocolate or dulce de leche for dipping.",
    ]),
    ("New Orleans Beignets", ["yeasted dough enriched with milk and egg", "oil for frying", "powdered sugar for dusting"], [
        "Make a soft, slightly sweet yeasted dough with flour, milk, egg, sugar and yeast, kneading until smooth and elastic, about 8 minutes.",
        "Place in a greased bowl, cover, and let rise in a warm place for about 1 hour until doubled in size.",
        "Roll the risen dough out on a floured surface to about 1 cm thick.",
        "Cut into squares roughly 7 cm per side using a sharp knife or pastry cutter.",
        "Let the cut squares rest, covered, for 15-20 minutes while you heat the oil.",
        "Heat oil in a deep pan to 180°C (350°F).",
        "Fry the beignets in small batches for 2-3 minutes, turning once, until puffed and golden brown on both sides.",
        "Drain on paper towels for a minute, then dust generously and evenly with powdered sugar while still warm.",
        "Serve immediately, as beignets are best enjoyed fresh and hot.",
    ]),
    ("Palmiers (Elephant Ears)", ["puff pastry", "granulated sugar for rolling"], [
        "Sprinkle a clean work surface generously with granulated sugar.",
        "Unroll the puff pastry onto the sugared surface and sprinkle more sugar evenly over the top, then gently roll over it with a rolling pin so the sugar presses into both sides.",
        "Fold both long edges of the pastry in towards the centre line, then fold those folded edges in towards the centre again, so you have four layers meeting in the middle.",
        "Finally, fold the whole thing in half along the centre line to form a tight, multi-layered log, then wrap and chill for 20 minutes to firm up.",
        "Preheat the oven to 200°C (400°F) and line a baking sheet with parchment paper.",
        "Using a sharp knife, slice the chilled log into rounds about 1 cm thick.",
        "Arrange the rounds on the prepared tray, spacing well apart as they will spread significantly.",
        "Bake for 12-15 minutes, flipping each one over halfway through with a spatula, until both sides are deeply caramelised and golden brown.",
        "Cool on a wire rack — they will crisp up further as they cool.",
    ]),
    ("Apple Turnovers", ["puff pastry", "diced apple", "sugar", "cinnamon", "egg wash"], [
        "Cook the diced apple with sugar and cinnamon in a saucepan over medium heat for 8-10 minutes, stirring occasionally, until just softened but still holding its shape, then let it cool completely — a warm filling will melt the pastry.",
        "Preheat the oven to 200°C (400°F) and line a baking sheet with parchment paper.",
        "Cut the puff pastry into even squares, about 12 cm per side.",
        "Spoon the cooled apple filling onto one half of each square, leaving a clear border around the edge.",
        "Brush the border with a little water or egg wash, then fold the pastry over the filling diagonally to form a triangle, pressing the edges together firmly.",
        "Crimp the sealed edges with the tines of a fork to seal completely and prevent the filling leaking out during baking.",
        "Brush the tops evenly with egg wash and cut two small slits in the top of each to let steam escape.",
        "Bake for 18-20 minutes, until puffed and deep golden brown all over.",
        "Cool on a wire rack for at least 10 minutes before serving, as the filling will be very hot.",
    ]),
]
for name, ing_list, steps in pastry_variants:
    g = grad()
    ing = [{"item": i, "amount": "as needed"} for i in ing_list]
    add(name, "Pastries", "1 hr 30 min", "8-10 pieces", "Advanced", "pastry", g, ing, steps,
        "Keep butter and dough cold throughout lamination — if it gets greasy or soft, chill for 15 minutes before continuing.")

# =========================================================
# 9. DONUTS — in-depth method
# =========================================================
donut_variants = [
    ("Classic Glazed Donuts", ["enriched yeasted dough", "oil for frying", "simple vanilla glaze (icing sugar, milk, vanilla)"]),
    ("Chocolate Frosted Donuts", ["enriched yeasted dough", "oil for frying", "chocolate glaze (icing sugar, cocoa, milk)"]),
    ("Jelly Filled Donuts", ["enriched yeasted dough", "oil for frying", "fruit jam for filling", "granulated sugar for coating"]),
    ("Cinnamon Sugar Donuts", ["enriched yeasted dough", "oil for frying", "cinnamon sugar coating"]),
    ("Boston Cream Donuts", ["enriched yeasted dough", "oil for frying", "vanilla pastry cream filling", "chocolate glaze"]),
    ("Baked Apple Cider Donuts", ["flour", "apple cider reduced until concentrated", "brown sugar", "cinnamon", "buttermilk"]),
    ("Maple Bacon Donuts", ["enriched yeasted dough", "oil for frying", "maple glaze", "crispy bacon bits"]),
    ("Powdered Sugar Mini Donuts", ["enriched yeasted dough", "oil for frying", "powdered sugar for dusting"]),
    ("Baked Vanilla Donuts", ["flour", "sugar", "baking powder", "milk", "egg", "vanilla extract", "simple glaze"]),
    ("Churro Donuts", ["enriched yeasted dough", "oil for frying", "cinnamon sugar coating", "dulce de leche for dipping"]),
]
for name, ing_list in donut_variants:
    g = grad()
    ing = [{"item": i, "amount": "as needed"} for i in ing_list]
    if "Baked" in name:
        steps = [
            "Preheat the oven to 190°C (375°F) and grease a donut pan thoroughly, including the central posts, so the donuts release cleanly.",
            "If using apple cider, simmer it in a small saucepan over medium heat for 15-20 minutes until reduced by half and concentrated in flavour, then let it cool.",
            "Whisk all the dry ingredients together thoroughly in one bowl, breaking up any lumps in the baking powder or sugar.",
            "In a separate bowl or jug, whisk together the milk or buttermilk, egg, melted butter and vanilla or reduced cider until smooth.",
            "Pour the wet ingredients into the dry ingredients and fold together gently with a spatula until just combined — a few small lumps are fine; overmixing will make the donuts tough and rubbery.",
            "Spoon the batter into a piping bag or a large zip-top bag with the corner snipped off, and pipe it evenly into the donut pan cavities, filling each about two-thirds full.",
            "Bake for 10-12 minutes, until the donuts spring back when touched and a toothpick inserted comes out clean.",
            "Let the donuts cool in the pan for 5 minutes before turning them out onto a wire rack.",
            "While still slightly warm, dip, glaze, or roll the donuts in your chosen coating so it adheres well.",
        ]
    else:
        steps = [
            "Combine the flour, yeast, sugar, salt, milk, egg and softened butter in a large bowl and mix until a shaggy dough forms.",
            "Knead the dough on a floured surface, or with a stand mixer's dough hook, for 8-10 minutes until smooth, soft and elastic.",
            "Place the dough in a greased bowl, cover, and let rise in a warm spot for about 1 hour, until doubled in size.",
            "Punch down the risen dough and roll it out on a floured surface to about 1.5 cm thick.",
            "Cut out rounds using a donut cutter (or two different-sized round cutters for the hole), re-rolling the scraps as needed.",
            "Place the shaped donuts on floured baking sheets, spaced well apart, cover loosely, and let prove for 30-45 minutes until visibly puffy.",
            "Heat the oil in a deep, heavy pan to 175°C (350°F) — use a thermometer for accuracy, as oil that's too hot burns the outside before the inside cooks, and oil that's too cool makes greasy donuts.",
            "Fry the donuts in small batches, 1-2 minutes per side, until deep golden brown, turning carefully with a slotted spoon or chopsticks.",
            "Drain on paper towels for a minute to remove excess oil.",
            "While still warm, dip, glaze, fill or coat the donuts as the recipe describes, working quickly so the coating sets onto warm (not hot) donuts.",
        ]
    add(name, "Donuts", "1 hr 15 min", "12 donuts", "Intermediate", "donut", g, ing, steps,
        "Keep your frying oil at a steady 175°C (350°F) — too hot and the outside burns before the inside cooks, too cool and they turn greasy.")

# =========================================================
# 10. NO-BAKE & GLOBAL — in-depth method
# =========================================================
global_variants = [
    ("No-Bake Cheesecake", ["digestive biscuit crumbs", "melted butter", "cream cheese", "icing sugar", "double cream", "lemon juice"], [
        "Crush the digestive biscuits into fine, even crumbs using a food processor, or by placing them in a bag and crushing with a rolling pin.",
        "Mix the crumbs thoroughly with the melted butter until every crumb is evenly coated and the mixture looks like wet sand.",
        "Press the mixture firmly and evenly into the base of a lined springform tin, using the flat bottom of a glass to compact it into a smooth, even layer.",
        "Chill the base in the fridge for at least 20 minutes to firm up while you make the filling.",
        "Beat the cream cheese, icing sugar and lemon juice together in a bowl until completely smooth, with no lumps of cream cheese remaining.",
        "In a separate bowl, whip the double cream to soft peaks — it should hold its shape but still look soft and glossy, not stiff or grainy.",
        "Fold the whipped cream into the cream cheese mixture in two or three additions, using a large spatula and gentle folding motions to keep the mixture light and airy.",
        "Spread the filling evenly over the chilled biscuit base, smoothing the top with an offset spatula.",
        "Cover and refrigerate for at least 4 hours, ideally overnight, until fully set and firm to the touch.",
        "Run a thin knife around the edge before releasing the springform tin, and slice with a knife dipped in hot water for clean cuts.",
    ]),
    ("Tres Leches Cake", ["light sponge cake", "evaporated milk", "condensed milk", "double cream", "whipped cream topping"], [
        "Bake a simple vanilla sponge cake in a baking dish according to a basic recipe, then let it cool in the dish for about 15 minutes — it should still be slightly warm when you add the milk mixture.",
        "Whisk together the evaporated milk, condensed milk and a splash of double cream in a jug until fully combined.",
        "Poke holes all over the surface of the warm cake using a skewer or fork, spacing them about 2 cm apart so the milk mixture can soak in evenly.",
        "Pour the milk mixture slowly and evenly over the cake, starting around the edges and working inward, pausing occasionally to let it absorb before adding more.",
        "Cover and chill the soaked cake for at least 2 hours, or ideally overnight, so the milk fully penetrates every layer.",
        "Just before serving, whip fresh double cream to soft peaks and spread it generously over the top of the chilled cake.",
        "Slice and serve cold, straight from the fridge.",
    ]),
    ("Chewy Mochi", ["glutinous rice flour", "sugar", "water", "cornflour for dusting", "sweet filling of choice"], [
        "Whisk the glutinous rice flour, sugar and water together in a microwave-safe bowl until completely smooth, with no lumps of flour remaining.",
        "Cover the bowl loosely with clingfilm and microwave on high for 1 minute, then stir thoroughly.",
        "Microwave again in 30-second bursts, stirring well between each, until the mixture turns thick, glossy and translucent — this usually takes 2-3 minutes total.",
        "Dust a clean work surface generously with cornflour, then carefully turn the hot dough out onto it.",
        "Let the dough cool for a few minutes until it's safe to handle, dusting your hands with more cornflour to prevent sticking.",
        "Divide the dough into even pieces, flattening each one into a small disc in your palm.",
        "Place a small spoonful of your chosen sweet filling in the centre of each disc, then gather the edges up and over the filling, pinching firmly to seal into a smooth ball.",
        "Dust off any excess cornflour and serve at room temperature the same day for the best texture.",
    ]),
    ("Churro Cheesecake Bars", ["crescent or puff pastry sheets", "cream cheese", "sugar", "vanilla", "cinnamon sugar coating"], [
        "Preheat the oven to 175°C (350°F) and line a baking tin with parchment paper.",
        "Unroll one sheet of pastry and press it evenly into the base of the tin, patching any seams together with your fingers.",
        "Beat the cream cheese, sugar and vanilla together until completely smooth and lump-free.",
        "Spread the cream cheese mixture evenly over the pastry base, right to the edges.",
        "Unroll the second sheet of pastry and lay it on top, pressing gently to seal the edges where possible.",
        "Brush the top layer generously with melted butter, then sprinkle evenly and generously with cinnamon sugar.",
        "Bake for 25-30 minutes, until the top is puffed and deep golden brown.",
        "Cool completely in the tin, then chill for at least 1 hour so the filling firms up before slicing into bars.",
    ]),
    ("Oreo Truffles", ["chocolate sandwich cookies", "cream cheese", "melted chocolate for coating"], [
        "Crush the sandwich cookies into very fine crumbs using a food processor, pulsing until no large pieces remain.",
        "Add the softened cream cheese to the crumbs and mix, either in the food processor or by hand, until a thick, uniform, moldable dough forms.",
        "Scoop out tablespoon-sized portions and roll between your palms into smooth, even balls.",
        "Arrange the balls on a parchment-lined tray and chill in the fridge for at least 20 minutes, until firm — this makes them much easier to dip without falling apart.",
        "Melt the chocolate gently in short bursts in the microwave, or over a bain-marie, stirring until completely smooth.",
        "Using a fork, dip each chilled ball into the melted chocolate, tapping off the excess, then set it back on the parchment.",
        "While the chocolate is still wet, you can drizzle a contrasting colour of melted chocolate on top for decoration.",
        "Chill again for at least 20 minutes until the chocolate coating is fully set before serving.",
    ]),
    ("Rocky Road Bars", ["melted chocolate", "mini marshmallows", "chopped nuts", "crushed biscuits"], [
        "Line a baking tin with parchment paper, leaving an overhang on two sides for easy removal later.",
        "Melt the chocolate gently in a heatproof bowl set over a pan of barely simmering water, stirring occasionally until completely smooth.",
        "Remove the chocolate from the heat and let it cool slightly for 2-3 minutes so it won't melt the marshmallows on contact.",
        "Fold in the mini marshmallows, chopped nuts and crushed biscuits, stirring gently until every piece is coated in chocolate.",
        "Transfer the mixture to the prepared tin, pressing it into an even layer with the back of a spoon — don't press too firmly, or you'll lose the light, chunky texture.",
        "Chill in the fridge for at least 2 hours, until completely set and firm.",
        "Lift out using the parchment overhang and slice into bars or chunks with a sharp knife.",
    ]),
    ("Classic Chocolate Fudge", ["sweetened condensed milk", "chocolate chips", "butter", "vanilla extract"], [
        "Line a small tin with parchment paper, leaving an overhang for easy removal.",
        "Combine the chocolate chips, condensed milk and butter in a heavy-bottomed saucepan over low heat.",
        "Melt gently, stirring constantly with a spatula, until the mixture is completely smooth and glossy — keep the heat low throughout to avoid scorching the chocolate or milk.",
        "Remove from the heat and stir in the vanilla extract until fully incorporated.",
        "Pour the mixture into the prepared tin, using the spatula to spread it into an even layer right into the corners.",
        "Tap the tin gently on the counter to release any air bubbles, then smooth the top.",
        "Chill in the fridge for at least 3 hours, or until completely firm to the touch.",
        "Lift out using the parchment, then cut into small, neat squares with a sharp knife.",
    ]),
    ("Pistachio Baklava Rolls", ["filo pastry", "melted butter", "ground pistachios", "sugar", "honey syrup"], [
        "Preheat the oven to 160°C (325°F) and mix the ground pistachios with a little sugar in a bowl.",
        "Lay one sheet of filo pastry flat on your work surface and brush it thoroughly and evenly with melted butter.",
        "Scatter a thin, even line of the sugared pistachio mixture along one short edge of the sheet.",
        "Roll the filo up tightly from that edge into a long, thin log, keeping the roll snug throughout.",
        "Cut the long log into shorter pieces, about 6-8 cm each, and repeat with the remaining filo sheets and filling.",
        "Arrange the rolls seam-side down on a lined baking tray, spacing them slightly apart.",
        "Bake for 20-25 minutes, until golden brown and crisp all over.",
        "While the rolls bake, warm the honey syrup gently in a small saucepan until runny.",
        "As soon as the rolls come out of the oven, drizzle the warm syrup generously over them while both are still hot, so the syrup soaks in rather than just coating the surface.",
        "Let cool to room temperature before serving, so the layers have time to crisp back up.",
    ]),
    ("Mango Sticky Rice", ["glutinous sticky rice", "coconut milk", "sugar", "salt", "ripe mango, sliced"], [
        "Rinse the glutinous sticky rice thoroughly under cold water until the water runs clear, then soak it in fresh water for at least 4 hours, or overnight.",
        "Drain the soaked rice well, then transfer it to a steamer lined with muslin cloth or a banana leaf.",
        "Steam over simmering water for 25-30 minutes, until the rice is tender, glossy and sticky throughout, checking partway and adding more water to the steamer if needed.",
        "While the rice steams, warm the coconut milk with sugar and a pinch of salt in a small saucepan over low heat, stirring until the sugar fully dissolves — don't let it boil.",
        "Transfer the hot cooked rice to a bowl and pour over about three-quarters of the warm coconut milk mixture, stirring gently to coat every grain.",
        "Cover the bowl and let the rice sit for 10-15 minutes, allowing it to absorb the coconut milk and become even richer and stickier.",
        "Reserve the remaining coconut milk mixture as a sauce to drizzle at the end.",
        "Serve the warm rice alongside slices of ripe mango, drizzling the reserved coconut sauce generously over both just before eating.",
    ]),
    ("Sicilian Cannoli", ["cannoli shells", "ricotta", "icing sugar", "mini chocolate chips", "chopped pistachios"], [
        "Place the ricotta in a fine sieve lined with muslin or a clean tea towel, set it over a bowl, and let it drain in the fridge for at least 2 hours, or ideally overnight — this removes excess moisture so your filling isn't watery.",
        "Transfer the well-drained ricotta to a bowl and beat with the icing sugar until completely smooth and creamy, with no graininess remaining.",
        "Fold in the mini chocolate chips until evenly distributed throughout the filling.",
        "Spoon the filling into a piping bag fitted with a large round tip and chill until ready to serve.",
        "Just before serving, pipe the ricotta filling into both ends of each cannoli shell, working from each side towards the middle so it fills completely.",
        "Dip each filled end into chopped pistachios, pressing gently so they stick to the exposed filling.",
        "Serve immediately — filling the shells right before serving keeps them crisp, as they soften quickly once filled.",
    ]),
]
for name, ing_list, steps in global_variants:
    g = grad()
    ing = [{"item": i, "amount": "as needed"} for i in ing_list]
    add(name, "No-Bake & Global", "40 min (+ chilling/freezing)", "8-10 servings", "Easy", "global", g, ing, steps,
        "No oven, no problem — just give these enough time in the fridge or freezer to set properly before serving.")

# =========================================================
# 11. CHRISTMAS DESSERTS — in-depth method
# =========================================================
christmas_variants = [
    ("Classic Christmas Pudding", ["dried mixed fruit (raisins, currants, sultanas)", "mixed candied peel", "grated apple and orange zest", "breadcrumbs", "suet or cold grated butter", "dark brown sugar", "mixed spice, cinnamon and nutmeg", "eggs", "stout or ale and brandy", "brandy butter, to serve"], [
        "In a very large bowl, combine the dried fruit, candied peel, grated apple, orange zest, breadcrumbs, suet, sugar and spices, stirring well so every piece of fruit is coated.",
        "In a separate bowl or jug, whisk together the eggs, stout or ale and a good splash of brandy.",
        "Pour the wet ingredients into the dry mixture and stir thoroughly with a wooden spoon until fully combined — traditionally, everyone in the household gives it a stir and makes a wish.",
        "Cover the bowl and let the mixture rest overnight at room temperature, so the dried fruit can soak up the liquid and the flavours meld.",
        "The next day, grease a pudding basin generously with butter and spoon in the mixture, pressing down firmly to remove any air pockets.",
        "Cover the top with a double layer of baking paper and a layer of foil, pleated in the centre to allow for expansion, and tie securely with string, creating a handle to lift it out later.",
        "Place the basin on an upturned saucer or trivet inside a large pot, and pour in boiling water to come halfway up the sides of the basin.",
        "Cover the pot and steam over a gentle simmer for 6-7 hours, topping up the water regularly so it never boils dry — check every hour or so.",
        "Once steamed, remove the basin, let it cool completely, then re-cover with fresh paper and foil and store in a cool, dark place for up to 2-3 months, allowing the flavour to mature.",
        "On the day of serving, steam the pudding again for a further 2-3 hours to heat it through.",
        "Turn out onto a plate, warm a little brandy in a small pan, carefully ignite it, and pour it flaming over the pudding at the table for the classic presentation.",
        "Serve in slices with brandy butter, custard or cream.",
    ]),
    ("Chocolate Yule Log (Bûche de Noël)", ["eggs", "caster sugar", "all-purpose flour", "cocoa powder", "whipped cream or chocolate buttercream filling", "dark chocolate ganache for coating", "icing sugar, to dust"], [
        "Preheat the oven to 200°C (400°F) and line a shallow Swiss roll tin (around 33 x 23 cm) with parchment paper.",
        "Whisk the eggs and sugar together with an electric mixer for 5-8 minutes, until very pale, thick and roughly tripled in volume — the mixture should leave a ribbon trail when the beaters are lifted.",
        "Sift the flour and cocoa powder together, then fold gently into the whisked eggs in two or three additions, using a large spatula and a light folding motion to keep as much air in as possible.",
        "Pour the batter into the prepared tin and spread it evenly right to the edges and corners.",
        "Bake for 10-12 minutes, until the sponge springs back when lightly touched and just starts to pull away from the sides of the tin.",
        "While the sponge bakes, lay a clean tea towel on the counter and dust it generously with icing sugar.",
        "As soon as the sponge comes out of the oven, turn it out immediately onto the sugared tea towel and peel off the parchment paper.",
        "While still hot, roll the sponge up tightly from one short end, rolling the tea towel inside with it, then leave it to cool completely in this rolled shape — this trains the sponge to hold a curl without cracking later.",
        "Once fully cool, carefully unroll the sponge, spread the whipped cream or buttercream filling evenly over the surface, then re-roll it tightly without the tea towel this time.",
        "Trim a small diagonal slice off one end and attach it to the side of the log to look like a stubby branch, securing it with a little ganache.",
        "Cover the whole log with chocolate ganache, then drag a fork lengthways through the ganache to create a bark-like texture.",
        "Chill for at least 30 minutes to set, then dust with icing sugar to look like a dusting of snow before serving.",
    ]),
    ("Classic Mince Pies", ["sweet shortcrust pastry (flour, cold butter, icing sugar, egg)", "jarred or homemade fruit mincemeat", "a splash of brandy", "milk or egg wash, to glaze", "icing sugar, to dust"], [
        "Make the shortcrust pastry by rubbing cold butter into the flour and icing sugar until it resembles fine breadcrumbs, then bind with a beaten egg until it just comes together into a dough.",
        "Wrap the dough and chill in the fridge for at least 30 minutes.",
        "Stir a splash of brandy through the mincemeat to loosen it and add extra warmth, if you like.",
        "Preheat the oven to 200°C (400°F) and grease a 12-hole shallow muffin or tart tin.",
        "Roll out two-thirds of the chilled pastry thinly and cut out rounds slightly larger than the holes in the tin, pressing each one gently into place to line the base and sides.",
        "Spoon a generous teaspoon of the mincemeat into each lined pastry case — don't overfill, as it will bubble up during baking.",
        "Roll out the remaining pastry and cut out smaller rounds or festive shapes (such as stars) for the lids, pressing them gently onto the filled cases, or simply leave the stars sitting on top as decoration.",
        "If using solid lids, brush them lightly with milk or egg wash and cut a small slit in the top of each to let steam escape.",
        "Bake for 18-20 minutes, until the pastry is golden brown all over.",
        "Let the mince pies cool in the tin for 10 minutes before carefully transferring to a wire rack — the filling is extremely hot straight from the oven.",
        "Dust with icing sugar once cooled, and serve warm or at room temperature with brandy butter or cream.",
    ]),
    ("German Stollen", ["strong white flour", "yeast", "warm milk", "butter", "sugar", "mixed dried fruit and candied peel soaked in rum", "marzipan", "melted butter and icing sugar, to finish"], [
        "Soak the dried fruit and candied peel in rum (or orange juice for an alcohol-free version) for at least 2 hours, or overnight, so it plumps up and absorbs the flavour.",
        "Make an enriched yeasted dough with the flour, yeast, warm milk, butter and sugar, kneading for about 8-10 minutes until smooth and elastic.",
        "Drain the soaked fruit well and knead it into the dough along with the candied peel until evenly distributed throughout.",
        "Place the dough in a greased bowl, cover, and let it rise in a warm place for about 1-1.5 hours, until doubled in size.",
        "Punch down the dough and roll it out into an oval on a floured surface.",
        "Shape a log of marzipan slightly shorter than the dough and lay it along the centre, then fold one side of the dough over the marzipan and press the edges to seal, creating the traditional off-centre fold.",
        "Place the shaped stollen on a lined baking tray, cover loosely, and let it prove again for 30-45 minutes.",
        "Preheat the oven to 175°C (350°F) and bake the stollen for 45-55 minutes, covering loosely with foil after 25 minutes if it's browning too quickly, until deep golden and it sounds hollow when tapped on the base.",
        "While still warm, brush the stollen generously and repeatedly with melted butter, letting each layer soak in before adding more.",
        "Once fully cooled, dust thickly and evenly with icing sugar — this thick sugar coating is traditional and also helps preserve the loaf.",
        "Wrap well and store at room temperature for up to 2 weeks; the flavour improves after a few days as it matures.",
    ]),
    ("Italian Panettone", ["strong white flour", "fresh yeast", "eggs and egg yolks", "butter", "sugar", "candied orange and lemon peel", "raisins soaked in rum", "vanilla and orange zest"], [
        "Make a starter dough with a portion of the flour, yeast and warm water, and let it bubble and rise for about 1 hour until active and foamy.",
        "Soak the raisins in warm rum or orange juice while the starter rises.",
        "Beat the eggs, egg yolks and sugar together, then combine with the active starter, remaining flour, softened butter, vanilla and orange zest, kneading for 10-15 minutes until the dough is very smooth, soft and elastic — this enriched dough takes longer to come together than a plain bread dough.",
        "Knead in the drained raisins and candied peel until evenly distributed.",
        "Place the dough in a large greased bowl, cover, and let it rise in a warm place for 3-4 hours, until at least doubled — panettone dough rises slowly due to its high butter and egg content.",
        "Gently knock back the dough and shape it into a tight ball, then place it into a panettone paper mould or a deep, round cake tin lined with a tall paper collar.",
        "Cover loosely and let it prove again for 2-3 hours, until it has risen almost to the top of the mould.",
        "Preheat the oven to 170°C (340°F). Just before baking, cut a cross into the top of the dough and insert a small knob of butter into the slits.",
        "Bake for 45-55 minutes, covering loosely with foil if the top browns too quickly, until a skewer inserted deep into the centre comes out clean.",
        "Immediately after baking, skewer the base of the panettone with long knitting needles or skewers and hang it upside down for several hours — this stops the tall, delicate structure from collapsing as it cools.",
        "Once fully cooled, store wrapped at room temperature, and dust with icing sugar before serving in wedges.",
    ]),
    ("Eggnog Custard Pots", ["whole milk", "double cream", "egg yolks", "sugar", "freshly grated nutmeg", "a splash of brandy or rum", "vanilla extract"], [
        "Heat the milk and cream together in a saucepan over medium heat until just steaming, with small bubbles forming at the edge.",
        "Whisk the egg yolks and sugar together in a bowl until pale, then slowly pour in the hot milk mixture while whisking constantly to temper the eggs gently.",
        "Return the mixture to the pan and cook over low heat, stirring constantly with a spatula, until it thickens enough to coat the back of a spoon, about 5-6 minutes — do not let it boil, or it will curdle.",
        "Remove from the heat and stir in the vanilla, a generous grating of fresh nutmeg, and a splash of brandy or rum.",
        "Strain the custard through a fine sieve into a jug to ensure a silky-smooth texture.",
        "Divide the warm custard evenly among small serving pots or glasses.",
        "Cover and chill for at least 3 hours, until fully set and cold.",
        "Serve topped with a little whipped cream and an extra grating of nutmeg.",
    ]),
    ("Iced Gingerbread Cookies", ["all-purpose flour", "butter", "dark brown sugar", "golden syrup or molasses", "ground ginger, cinnamon and cloves", "an egg", "royal icing (icing sugar and egg white or meringue powder)"], [
        "Melt the butter with the brown sugar and golden syrup gently in a saucepan until smooth, then let it cool for 10 minutes.",
        "Whisk the flour, ginger, cinnamon, cloves and a pinch of salt together in a large bowl.",
        "Stir the cooled butter mixture and the egg into the dry ingredients until a smooth dough forms.",
        "Wrap the dough and chill for at least 1 hour, until firm enough to roll without sticking.",
        "Preheat the oven to 175°C (350°F) and line baking sheets with parchment paper.",
        "Roll the dough out on a floured surface to about 5 mm thick and cut out festive shapes using cookie cutters — gingerbread figures, stars, trees and bells all work well.",
        "Transfer the shapes to the prepared sheets, spacing them apart, and bake for 9-11 minutes, until just firm at the edges — they'll crisp further as they cool, so don't overbake.",
        "Cool completely on a wire rack before icing — warm cookies will melt the icing instantly.",
        "Make the royal icing by whisking icing sugar with egg white or meringue powder and a little water until thick and pipeable, and spoon it into a piping bag fitted with a very fine tip.",
        "Pipe outlines and decorative details onto the cooled cookies, letting each colour or layer firm up for a few minutes before adding the next on top.",
        "Let the iced cookies dry fully at room temperature for at least 2 hours before stacking or packaging.",
    ]),
    ("Cranberry & White Chocolate Blondies", ["unsalted butter", "light brown sugar", "eggs", "all-purpose flour", "white chocolate chips", "dried cranberries", "orange zest"], [
        "Preheat the oven to 175°C (350°F) and line a 23 cm (9 in) square tin with parchment paper.",
        "Melt the butter and whisk it with the brown sugar until smooth and glossy.",
        "Whisk in the eggs one at a time, then stir in the orange zest.",
        "Fold in the flour until just combined, then fold through the white chocolate chips and dried cranberries, reserving a small handful of each to scatter on top.",
        "Pour the batter into the prepared tin, spreading it evenly, and scatter the reserved chocolate chips and cranberries over the surface.",
        "Bake for 25-28 minutes, until the edges are golden and a skewer inserted in the centre comes out with a few moist crumbs.",
        "Cool completely in the tin before lifting out using the parchment and slicing into festive squares or bars.",
    ]),
    ("Candy Cane Peppermint Bark", ["good-quality dark chocolate, chopped", "good-quality white chocolate, chopped", "peppermint extract", "crushed candy canes or peppermint sweets"], [
        "Line a baking tray with parchment paper.",
        "Melt the dark chocolate gently in a heatproof bowl set over a pan of barely simmering water, stirring until completely smooth.",
        "Pour the melted dark chocolate onto the prepared tray and spread it into an even layer, about 5 mm thick, using an offset spatula.",
        "Chill the dark chocolate layer in the fridge for 10-15 minutes, until just set but not fully hardened.",
        "Melt the white chocolate the same way, then stir in a few drops of peppermint extract to taste.",
        "Pour the white chocolate over the set dark chocolate layer and spread it evenly to cover completely.",
        "While the white chocolate is still wet, scatter the crushed candy canes evenly over the top, pressing them down very lightly so they stick.",
        "Chill for at least 30 minutes, until completely firm, then break or cut into irregular shards to serve.",
    ]),
    ("Chocolate Orange Truffles", ["dark chocolate, finely chopped", "double cream", "orange zest and a little orange liqueur or extract", "cocoa powder or melted chocolate, for coating"], [
        "Place the finely chopped dark chocolate in a heatproof bowl.",
        "Heat the double cream in a small saucepan until just simmering, then pour it immediately over the chocolate.",
        "Let it sit undisturbed for 2 minutes to let the heat melt the chocolate, then stir gently from the centre outwards until completely smooth and glossy — this is a ganache.",
        "Stir in the orange zest and a splash of orange liqueur or a few drops of orange extract.",
        "Cover and chill the ganache for at least 2 hours, until firm enough to scoop and roll.",
        "Scoop out small portions with a melon baller or teaspoon and roll quickly between your palms into smooth balls — work fast, as the ganache softens quickly from the warmth of your hands.",
        "Roll each truffle in cocoa powder to coat, or dip in melted chocolate for a firmer shell, then place on a parchment-lined tray.",
        "Chill again for at least 20 minutes to firm up fully before serving or packaging as gifts.",
    ]),
]
for name, ing_list, steps in christmas_variants:
    g = grad()
    ing = [{"item": i, "amount": "as needed"} for i in ing_list]
    add(name, "Christmas Desserts", "2 hr (varies by recipe)", "8-12 servings", "Intermediate", "christmas", g, ing, steps,
        "Many Christmas bakes taste even better after a day or two resting, as the spices and dried fruit have time to mellow and deepen in flavour.")

print(f"Total recipes: {len(recipes)}")
avg_steps = sum(len(r["steps"]) for r in recipes) / len(recipes)
print(f"Average steps per recipe: {avg_steps:.1f}")
with open("recipes.json", "w") as f:
    json.dump(recipes, f, indent=0)
