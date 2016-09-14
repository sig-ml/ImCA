import numpy as np
from genetic import genetic_search

IMAGE_PIXEL_VALUES = 2
NEIGHBOURHOOD_SIZE = 9

class Cellular:
    def __init__(self, ident=None):
        self.ident = ident
        self.data = np.random.random(IMAGE_PIXEL_VALUES ** NEIGHBOURHOOD_SIZE) < 0.5

    def mutate(self, mutate_rate):
        new_data = []
        for i in self.data:
            if np.random.random() < mutate_rate:
                i = np.random.random() < 0.5
            new_data.append(i)
        self.data = np.array(new_data)

    def crossover(self, other, crossover_rate):
        new1, new2 = [], []
        for i, j in zip(self.data, other.data):
            if np.random.random() < crossover_rate:
                i, j = j, i
            new1.append(i)
            new2.append(j)
        c1, c2 = Cellular(), Cellular()
        c1.data, c2.data =  np.array(new1), np.array(new2)
        return c1, c2

    def fitness(self):
        # TODO: figure a way to incorporate the image DB into this
        return 1

    def run(self, iterations):
        # TODO:
        pass


if __name__ == '__main__':
    kwargs = {"individual_class": Cellular,
              "mutate_rate": 0.01,
              "crossover_rate": 0.7,
              "population_size": 10000,
              "epochs": -1}
    genetic_search(**kwargs)

