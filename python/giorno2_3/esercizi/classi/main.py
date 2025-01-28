class Country:
      def __init__(self, name):
          self.name = name
          self.regions = []

      def add_region(self, region):
          self.regions.append(region)
      @property
      def pop(self):
          total_population = sum(region.pop for region in self.regions)
          return total_population
          """The total population of this country"""

      @property
      def most_populuous_city(self):
          most_populuous_city = None  # ancora non è un dato noto
          for region in self.regions:
              for city in region.cities:
                  if most_populuous_city is None or (city.pop and city.pop > most_populuous_city.pop):
                      most_populuous_city = city
          return most_populuous_city

italy = Country("Italy")
italy.name

class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    @property
    def pop(self):
        total_population = sum(city.pop for city in self.cities if city.pop)
        return total_population

sicily = Region("Sicily")
sicily.name
italy.add_region(sicily)

class City:
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop

catania = City("Catania", pop=300_000)
palermo = City("Palermo", pop=600_000)

sicily.add_city(catania)
sicily.add_city(palermo)

calabria = Region("Calabria")
calabria.name
italy.add_region(calabria)
reggio_calabria = City("Reggio Calabria", pop=170_000)
calabria.add_city(reggio_calabria)

