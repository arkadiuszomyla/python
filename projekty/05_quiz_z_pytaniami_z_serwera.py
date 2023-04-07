# https://opentdb.com/api_config.php
# https://the-trivia-api.com/docs/
import requests
import html


class Question:
    def __init__(self, category, quastionStr, correctAnswerFlag):
        self.category = category
        self.quastionStr = quastionStr
        self.correctAnswerFlag = correctAnswerFlag


class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))

        if response.ok:
            #{'response_code': 0, 'results': [{'category': 'Entertainment: Japanese Anime & Manga', 'type': 'boolean', 'difficulty': 'easy', 'question': 'In Kill La Kill, the weapon of the main protagonist is a katana. ', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy', 'question': 'In &quot;Sonic Adventure&quot;, you are able to transform into Super Sonic at will after completing the main story.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The Sun rises from the North.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Geography', 'type': 'boolean', 'difficulty': 'easy', 'question': 'There are no deserts in Europe.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Time on Computers is measured via the EPOX System.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Animals', 'type': 'boolean', 'difficulty': 'easy', 'question': 'A caterpillar has more muscles than humans do.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Sports', 'type': 'boolean', 'difficulty': 'easy', 'question': 'In association football, or soccer, a corner kick is when the game restarts after someone scores a goal.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Watch_Dogs 2 is a prequel.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Animals', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The Killer Whale is considered a type of dolphin.', 'correct_answer': 'True', 'incorrect_answers': ['False']}]}
            #print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                quastionStr = html.unescape(q["question"])
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1']

                qObj = Question(category, quastionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz")
        numCorrectUserAnswers = 0
        n = 0
        numQuestion = len(self.questionsList)

        while(n < numQuestion):
            q = self.questionsList[n]
            print("Question number " + str(n) + ": " + q.quastionStr)
            print("Answer flag: " + q.correctAnswerFlag)
            n += 1

            answer = input("Give correct answer True or False: ")
            answerBool = False
            if answer == "True":
                answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")

        print("Number of correct answers: " + numCorrectUserAnswers, + " from " + len(self.numQuestions))

quiz = Quiz(10)
quiz.startQuiz()