class RandomizedSet:

    def __init__(self):
        '''
        Initializes the RandomizedSet object.
        '''
        self.d = {}
        

    def insert(self, val: int) -> bool:
        '''
         Inserts an item val into the set if not present. 
         Returns true if the item was not present, false otherwise.
        '''
        if val in self.d:
            return False                
        self.d[val] = None
        return True            

    def remove(self, val: int) -> bool:
        '''
        Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise.
        '''
        if val not in self.d:
            return False        
        del self.d[val]
        return True
        

    def getRandom(self) -> int:
        '''
        Returns a random element from the current set of elements 
        (it's guaranteed that at least one element exists when this method is called). 
        Each element must have the same probability of being returned.
        '''
        return random.choice(list(self.d.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()