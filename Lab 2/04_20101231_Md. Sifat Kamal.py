import random

class Genetic:

    def __init__(self, listt, N, T):

        self.listt = listt
        
        self.N = int(N)

        self.T = int(T)

        self.listt_1 = [] #Player

        self.listt_2 = [] #Run

        for i in range(len(self.listt)):

            value_1, value_2 = self.listt[i].split(" ")

            self.listt_1.append(value_1)

            self.listt_2.append(int(value_2))

        # self.listt_2 = list(map(int, self.listt_2))

    def model(self):

        temp = []

        population = []

        # value = 2

        for i in range(2):

            for j in range(self.N):

                temp.append(random.randint(0, 1))

            population.append(temp)

            temp = []

        self.select(population)

    def select(self, population):

        for i in range(len(population)):

            self.fitness(population[i], population)

    def fitness(self, listt, population):

        count = 0

        for i in range(len(listt)):

            if listt[i] == 1:
                
                summ = self.listt_2[i] + count

                count = summ

        if summ == self.T:

            self.output(listt)

        else:

            a = random.choice(population)

            b = random.choice(population)

            self.crossover(a, b)

    def crossover(self, a, b):

        line = random.randint(0, len(a)-1)

        loopp = len(a)-line

        new_population = []

        for i in range(loopp):

            a[line], b[line] = b[line], a[line]

            line+=1

        new_population.append(a)

        new_population.append(b)

        self.mutation(new_population)

    def mutation(self, population):

        new_listt_1 = []

        new_listt_2 = []
        
        for i in population:

            for j in i:

                if j == 1:

                    new_listt_1.append(0)

                elif j == 0:

                    new_listt_1.append(1)

            new_listt_2.append(new_listt_1)

            new_listt_1 = []

        self.select(new_listt_2)

    def output(self, listt):

        listt_player = []

        index = 0

        for i in listt:

            if i == 1:

                listt_player.append(self.listt_1[index])

            else:

                continue



        for i in listt:

            print(i, end = " ")

        quit()

fdata = open('input_1.txt')

fdata = fdata.read()

data = fdata.split('\n')

N, T = data.pop(0).split(" ")

result = Genetic(data, N, T)

result.model()
