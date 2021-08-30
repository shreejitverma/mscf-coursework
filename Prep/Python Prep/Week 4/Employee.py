
# File: Employee2.py

class Employee:
    def __init__(self, name, id, rate):
        self._name = name
        self._id = id
        self._rate = rate
    def __str__(self):
        return ('id: ' + str(self._id) +
                ', name: ' + self._name +
                ', salary: ' +
                '{:.2f}'.format(self._rate))
    def give_raise(self, percent):
        self._rate *= 1.0 + percent / 100

if __name__ == '__main__':
    john = Employee('John', 1, 60.50)
    print(str(john))
    print(john)     # calls str(john) implicitly

    ed = Employee('Ed', 2, 72.25)
    print(ed)       # calls str(ed) implicitly
    ed.give_raise(10)
    print(ed)       # calls str(ed) implicitly

    # we are not respecting "privacy" here!
    if john._rate > ed._rate:
        print(john._name, 'makes more than',
              ed._name)
    else:
        print(john._name,
              'makes less than or equal to',
              ed._name)

