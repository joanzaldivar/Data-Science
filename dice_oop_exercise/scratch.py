class Dog:

    def __init__(self, given_name=None, age=0, favorite_bone=None):
        print("creating a dog instance with name {}...".format(given_name))
        self._remembered_name = given_name
        self._age = age
        self._favorite_bone = favorite_bone
        self._is_tired_of_repeating_things = False

    def bark_name(self):
        if self._remembered_name:
            print("Bark bark!  My name is {}".format(self._remembered_name))
        else:
            print("Alas, I have yet to be named")

    def repeat_after_me(self, phrase_to_repeat):
        self._is_tired_of_repeating_things = True
        print("{} says {}".format(self._remembered_name, phrase_to_repeat))

    def _internal_bookkeeping(self):
        print("ssssh, doing some bookkeeping")

    def set_name(self, name):
        self._remembered_name = name + 'ie'
        print("Gotcha, I'll remember my new name as {}".format(self._remembered_name))


if __name__ == '__main__':

    print("hello world!")

    d1 = Dog()
    d2 = Dog()

    d1.bark_name()
    d2.bark_name()

    d1.set_name("Bruce")
    d1.bark_name()

    d1.repeat_after_me("why hello there")
