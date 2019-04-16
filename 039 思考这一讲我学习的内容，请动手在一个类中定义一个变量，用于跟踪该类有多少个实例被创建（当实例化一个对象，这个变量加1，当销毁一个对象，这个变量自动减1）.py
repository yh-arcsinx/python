class Lala:
    count = 0
    def __init__(self):
        Lala.count += 1
    def __del__(self):
        Lala.count -= 1


        
