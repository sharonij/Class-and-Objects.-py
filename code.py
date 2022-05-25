class Student:
    # [assignment] Skeleton class. Add your code here
    def change_name(self, namee):
        self.name = namee
        return self.name

    def change_age(self, age):
        self.age = age
        return self.age

    def change_tracks(self, tracks):
        self.tracks = tracks
        return self.tracks

    def change_score(self, score):
        self.score = score
        return self.score

    def __init__(self, name, age,tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        pass


# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score(50)
Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)
print(Bob.name)
print(Bob.change_name("peter"))

print(Bob.age)
print(Bob.change_age(34))

print(Bob.tracks)
print(Bob.change_tracks("UI/UX"))

print(Bob.score)
print(Bob.change_score(50))

