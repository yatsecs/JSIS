import random
class question:
    def __init__ (self, cells):
        ans_list = [cells["correct"], cells["inc1"], cells["inc2"], cells["inc3"]]
        q = cells["question"]
    def randomiser(self):
        random.shuffle(self.ans_list)
    def ask(self):
        return
        
        