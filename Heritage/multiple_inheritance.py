# Parent 1
class Cat:
    def meow(self):
        print("Meow!")

# Parent 2
class Talker:
    def say(self, message):
        print(message)

# Child inheriting from BOTH parents
class TalkingCat(Cat, Talker):
    pass


# Instantiate a TalkingCat
salem = TalkingCat()

salem.meow()
salem.say("Hello!")