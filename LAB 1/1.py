class Corona:

    def __init__(self, listt):

        self.listt = listt

        self.row = len(self.listt) #row

        self.column = len(self.listt[0]) #column

        self.stack = []

        self.count = []
        

    def dfs(self, size_1, size_2):

        if self.listt[size_1][size_2] == "Y":

            self.stack.append(1)

            self.listt[size_1][size_2] = "N"

            size_2+=1

            if size_2 < self.column:

                self.dfs(size_1, size_2)

        elif self.listt[size_1][size_2-1]:

            self.stack.append(1)

            self.listt[size_1][size_2-1] = "N"

            size_2+=1

            if size_2 < self.column:

                self.dfs(size_1, size_2)

        elif self.listt[size_1+1][size_2] == "Y":

            self.stack.append(1)

            self.listt[size_1+1][size_2] = "N"

            size_2+=1

            if size_2 < self.column:

                self.dfs(size_1, size_2)

        self.count.append(len(self.stack))

        self.stack = []

    def check(self):

        for i in range(self.row):

            for j in range(self.column):

                #count = 0

                if self.listt[i][j] == "Y":

                    self.stack.append(1)

                    self.listt[i][j] = "N"

                    j = j+1

                    self.dfs(i, j)

        resultt = max(self.count)

        return resultt
                    
fdata = open('input_1.txt')

fdata = fdata.read()

data = fdata.split('\n')

index = 0

listt = []

for i in data:
    
    value = data[index].split(" ")

    listt.append(value)

    index+=1

result = Corona(listt)

print(result.check())
                



            





