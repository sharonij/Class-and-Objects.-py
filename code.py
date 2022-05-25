class Student:
    # [assignment] Skeleton class. Add your code here
    def change_name(self, namee):
        self.name = namee

    def change_age(self, age):
        self.age = int(age)

    def change_tracks(self, tracks):
        self.tracks = tracks

    def get_score(self):
        return self.score

    def __init__(self, name, age,tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = score

        pass


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
# Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)


