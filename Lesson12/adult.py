from Lesson12.Person import Person


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height **2)

    def get_bmi_category(self):
        bmi = self.caclulate_bmi()
        if bmi <18.5:
            return "underweight"
        elif 18.5 <= bmi <24.9
            return "Normal weight"
        elif 25 <= bmi < 30
            return "overweight"
        else:
            return "obese"