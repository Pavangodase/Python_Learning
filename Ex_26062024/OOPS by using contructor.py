class Dog:
    name = None
    id = None

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def sleep (self):
        print("Sleeping")


dog1 = Dog(name="Chaw", id="1")
dog2 = Dog(name="Maww", id="2")


print(f'{dog1.name} is having number {dog1.id}')
print(f'{dog2.name} is having number {dog2.id}')
dog1.sleep()

