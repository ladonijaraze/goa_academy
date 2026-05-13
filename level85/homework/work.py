
# https://www.codewars.com/kata/55a144eff5124e546400005a/train/python

class BasicFunctionFixer:
    def add_five(self, num):
        return num + 5


fixer = BasicFunctionFixer()



# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python

class Frog:
    def mouth_size(self, animal):
        if animal.lower() == "alligator":
            return "small"
        return "wide"


frog = Frog()

# https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

class BMI:
    def bmi(self, weight, height):
        result = weight / (height ** 2)

        if result <= 18.5:
            return "Underweight"
        elif result <= 25.0:
            return "Normal"
        elif result <= 30.0:
            return "Overweight"
        else:
            return "Obese"


person = BMI()


# https://www.codewars.com/kata/54fe05c4762e2e3047000add/train/python

class Mystery:
    def mystery(self):
        results = {'sanity': 'Hello'}
        return results


obj = Mystery()



# https://www.codewars.com/kata/5cca28520cbae0002ba9f870/train/python

class Pillars:
    def pillars(self, num_pill, dist, width):
        if num_pill == 1:
            return 0

        distance = (num_pill - 1) * dist * 100
        widths = (num_pill - 2) * width

        return distance + widths


p = Pillars()
