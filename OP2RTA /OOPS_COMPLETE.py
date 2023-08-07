from abc import ABC, abstractmethod
class LinearDataStructure:
    @abstractmethod
    def insert_at_start(self):
        pass
    @abstractmethod
    def insert_at_middle(self):
        pass
    @abstractmethod
    def insert_at_end(self):
        pass
    @abstractmethod
    def delete_at_start(self):
        pass
    @abstractmethod
    def delete_at_middle(self):
        pass
    @abstractmethod
    def delete_at_end(self):
        pass
    @abstractmethod
    def update_at_start(self):
        pass
    @abstractmethod
    def update_at_middle(self):
        pass
    @abstractmethod
    def update_at_end(self):
        pass
    @abstractmethod
    def traverse(self):
        pass

class Stacks(LinearDataStructure):
    def __init__(self):
        return self.items = []

    def insert_at_end(self, value):
        self.append(value)

    def delete_at_end(self):
        self.pop()


c = Stacks()

c.insert_at_end(1)
c.insert_at_end(2)
c.insert_at_end(3)
c.delete_at_end()

print(c)

#%%
