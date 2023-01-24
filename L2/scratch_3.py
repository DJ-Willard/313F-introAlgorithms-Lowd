def __str__(self):
    #print the heap sperate root and children in printing
        p = self.heap
        n = self.length
        result = "["
        for i in n:
            result += "Parent : " + str(p[i]) + "\n"
            result += "Left Child : " + str(p[((2 * i) +1)]) + "\n"
            result += "Right Child : " + str(p[((2 * i) + 2)]) + "\n"
        return  result[:-2] + "]"