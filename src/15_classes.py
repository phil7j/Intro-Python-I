# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon
# YOUR CODE HERE

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name=None):
        self.name = name
        super().__init__(self)

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint, LatLon):
    def __init__(self, difficulty, size):
        self.difficulty = difficulty
        self.size = size
        super().__init__(self)

    def __str__(self):
        return f"{self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}"
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
wp = Waypoint("Catacombs")
wp.lat = 41.70505
wp.lon = -121.51521
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(wp.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocaches = Geocache("1.5", "2")
geocaches.name = "Newberry Views"
geocaches.lat = 44.052137
geocaches.lon = -121.41556
# Print it--also make this print more nicely
print(geocaches.__str__())
