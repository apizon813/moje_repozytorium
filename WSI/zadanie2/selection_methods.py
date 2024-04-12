import random


def tournament_selection(population, pc):
    def tour(candidates):
        best_candidate = candidates[0]
        best_fit = best_candidate.fitness
        for candidate in candidates:
            fit = candidate.fitness
            if fit > best_fit:
                best_candidate = candidate
        return best_candidate

    pot_parents = population
    size = len(population)

    max_parents = round(size * pc)
    if max_parents % 2 == 1:
        max_parents += 1

    parents = []

    for i in range(max_parents):
        if len(pot_parents) > 1:
            candidates = random.sample(pot_parents, k=2)
        else:
            parents.append(pot_parents[0])
            break
        best_candidate = tour(candidates)
        parents.append(best_candidate)
        pot_parents.remove(best_candidate)

    random.shuffle(parents)
    return parents
