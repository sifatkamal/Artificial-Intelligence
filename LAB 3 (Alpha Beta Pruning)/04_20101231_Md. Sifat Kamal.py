import random

ID = "28181231"

class Game:

    def __init__(self, ID):

        self.minn = -1000

        self.maxx = 1000

        self.alpha = self.minn

        self.beta = self.maxx

        self.ID = list(ID)

        minimum = int(self.ID[4])

        temp = ID[-1]+ID[-2]

        temp = int(temp)

        maximum = int(temp*1.5)

        self.listt = []

        for i in range(8):

            self.listt.append(random.randint(minimum, maximum))

    def alpha_beta(self, level, index, verification):

        if level == 3:
            
            return self.listt[index]
            
        if verification == 1:
            
            result = self.minn

            for i in range(2):

                value = self.alpha_beta(level+1, index * 2 + i, 0)

                if result < value:

                    result = value

                if self.alpha < result:

                    self.alpha = result

                if self.beta <= self.alpha:

                    break
        
        else:

            result = self.maxx

            for i in range(2):
            
                value = self.alpha_beta(level + 1, index * 2 + i, 1)
                
                if result > value:
                    
                    result = value

                if self.beta > result:
                    
                    self.beta = result

                if self.beta <= self.alpha:

                    break
            
        return result

    # Task 1

    def task_1(self, result):

        points_to_win = self.ID[-1] + self.ID[-2]

        points_to_win = int(points_to_win)
        
        print("Generated 8 random points between the minimum and maximum point")
        
        print("limits:", self.listt)
        
        print("Total points to win:", points_to_win)
        
        print("Achieved point by applying alpha-beta pruning =", result)

        if result > points_to_win:

            print("The Winner is Optimus Prime")

        else:

            print("The Winner is Megatron")

    # Task 2

    def task_2(self):

        shf = int(self.ID[3])

        achieve = int(self.ID[4])

        output = []

        comparison = self.ID[-1]+self.ID[-2]

        comparison = int(comparison)

        for i in range(shf):

            random.shuffle(self.listt)

            result = randomm.alpha_beta(0, 0, 1)

            output.append(result)

        new_output = []

        for i in range(len(output)):

            if output[i] < comparison:

                continue

            else:

                new_output.append(output[i])
                
        print("After the shuffle:")
        
        print("List of all points values from each shuffle:", output)
        
        output.sort()
        
        print("The maximum value of all shuffles:", output[-1])
                
        print("Won", len(new_output), "times out of", len(output), "number of shuffles")


randomm = Game(ID)

result = randomm.alpha_beta(0, 0, 1)

randomm.task_1(result)

randomm.task_2()



