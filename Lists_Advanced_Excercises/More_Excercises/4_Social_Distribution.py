population = [int(i) for i in input().split(', ')]
minimum_wealth = int(input())
poor_population = [int(i) for i in population if i < minimum_wealth]
rich_population = [int(i) for i in population if i >= minimum_wealth]

if sum(population) / len(population) < minimum_wealth:
    print('No equal distribution possible')
else:
    while sum(poor_population) / len(poor_population) < minimum_wealth:
        for index, value in enumerate(poor_population):
            if value < minimum_wealth:
                wealth_needed = abs(minimum_wealth - value)
                wealth_available = max(rich_population) - minimum_wealth
                if wealth_available > wealth_needed:
                    poor_population[index] += wealth_needed
                    rich_population[rich_population.index(max(rich_population))] -= wealth_needed
                else:
                    poor_population[index] += wealth_available
                    rich_population[rich_population.index(max(rich_population))] -= wealth_available
    print(poor_population+rich_population)