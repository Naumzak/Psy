from .models import Results


class Counter:
    def __init__(self, data):
        self.data = data
        self.count = len(data) - 4

    def write_in_db(self):
        r = Results(answer1=self.data['answer1'],
                    answer2=self.data['answer2'],
                    answer3=self.data['answer3'],
                    answer4=self.data['answer4'],
                    answer5=self.data['answer5'],
                    answer6=self.data['answer6'],
                    answer7=self.data['answer7'],
                    answer8=self.data['answer8'],
                    answer9=self.data['answer9'],
                    answer10=self.data['answer10'],
                    answer11=self.data['answer11'],
                    answer12=self.data['answer12'],
                    answer13=self.data['answer13'],
                    answer14=self.data['answer14'],
                    answer15=self.data['answer15'],
                    answer16=self.data['answer16'],
                    sex=self.data['sex'],
                    age=self.data['age'],
                    education=self.data['education'],
                    work=self.data['work'],
                    )
        r.save()
