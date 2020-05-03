from ducks import Duck, Penguin, Flock, Mallard

flock = Flock()
donald = Duck()
daisy = Duck()
duck3 = Duck()
duck4 = Duck()
duck5 = Duck()
duck6 = Duck()
duck7 = Duck()
percy = Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(percy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
