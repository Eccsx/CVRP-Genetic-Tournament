from itertools import chain
from random import sample
from utils import change_position_array, distance


def fitness(chromosome, customers, COORDINATES_DEPOT):
    fitness = 0

    for i in range(len(chromosome)):
        routes = []

        # Add depot at route start
        routes.append(COORDINATES_DEPOT)

        # Retrieve routes customers
        for y in range(len(chromosome[i])):
            customer_coordinate = \
                customers[chromosome[i][y] - 1][:2]
            routes.append(customer_coordinate)

        # Add depot at route end
        routes.append(COORDINATES_DEPOT)

        # Calculate chromosome fitness
        for i in range(len(routes) - 1):
            fitness += distance(routes[i], routes[i + 1])

    return fitness


def obx(chromosome1, chromosome2, num_customers):
    # Define cut points
    positions = sample(range(0, num_customers), 2)
    positions.sort()
    i1, i2 = positions

    # Concat chromosomes
    concatenated_chromosome1 = list(chain.from_iterable(chromosome1))
    concatenated_chromosome2 = list(chain.from_iterable(chromosome2))

    # Create order list
    # l1 -> [2 1 8 9 3] -> p2 genes without p1 middle section genes
    # l2 -> [2 3 5 4 9] -> p1 genes without p2 middle section genes
    m_1 = concatenated_chromosome1[i1:i2]
    m_2 = concatenated_chromosome2[i1:i2]

    l_1 = [x for x in concatenated_chromosome1 if x not in m_2]
    l_2 = [x for x in concatenated_chromosome2 if x not in m_1]

    # Create new children
    # c1 -> clear outside middle section -> [. . . | 5 4 6 7 | . .]
    # -> fill with l2 [2 1 8 9 3] -> [2 1 8 | 5 4 6 7 | 9 3]
    # c2 -> clear outside middle section -> [. . . | 1 8 7 6 | . .]
    # -> fill with l1 [2 3 5 4 9] -> [3 5 4 | 1 8 7 6 | 9 2]
    c_1 = l_2[:i1] + m_1 + l_2[i1:]
    c_2 = l_1[:i1] + m_2 + l_1[i1:]

    return c_1, c_2


def pmx(chromosome1, chromosome2, num_customers):
    chromosomes_length = len(chromosome1)

    # get gene_size
    gene_size = int(num_customers / chromosomes_length)

    # get cut points
    cuts_points = sample(
        range(1, chromosomes_length * gene_size - 1),
        3
    )
    cuts_points.append(0)
    cuts_points.append(chromosomes_length * gene_size)
    cuts_points.sort()

    # Concat chromosomes
    concatenated_chromosome1 = list(chain.from_iterable(chromosome1))
    concatenated_chromosome2 = list(chain.from_iterable(chromosome2))

    # First child
    a = change_position_array(
        concatenated_chromosome1,
        concatenated_chromosome2,
        cuts_points
    )

    # Second child
    b = change_position_array(
        concatenated_chromosome2,
        concatenated_chromosome1,
        cuts_points
    )

    return a, b
