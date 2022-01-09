# factfulness questions and answers
fact_data = [
    {"question": "現今全世界的低所得國家裡，多少女孩會讀完小學？"
                 "（A）20％（B）40％（C）60％", "answer": "C"},
    {"question": "世界上的多數人是生活在哪裡？"
                 "（A）低所得國家（B）中所得國家（C）高所得國家", "answer": "B"},
    {"question": "在過去20年，全球赤貧人口占總人口的比例是⋯⋯"
                 "（A）幾乎翻倍（B）大致不變（C）幾乎減半", "answer": "C"},
    {"question": "現今全球的平均壽命是多少？"
                 "（A）50歲（B）60歲（C）70歲", "answer": "C"},
    {"question": "現今全球有20億個兒童，年齡介於0到15歲之間。根據聯合國的估算，到了2100年全球會有多少個兒童？"
                 "（A）40億（B）30億（C）20億", "answer": "C"},
    {"question": "根據聯合國的估算，到了2100年全球會再增加40億人，而主要原因是什麼？"
                 "（A）兒童人口增加（不到15歲）（B）成年人口增加（15歲到74歲）（C）老年人口增加（75歲以上）", "answer": "B"},
    {"question": "過去100年間，全球死於天災的人數是如何變化？"
                 "（A）幾乎翻倍（B）大致不變（C）幾乎減半", "answer": "C"},
    {"question": "現今全球多少2歲兒童有接種疫苗？"
                 "（A）20％（B）50％（C）80％", "answer": "C"},
    {"question": "全球30歲的男性平均接受過10年的學校教育，而同齡的女性平均接受過幾年的學校教育？"
                 "（A）9年（B）6年（C）3年", "answer": "A"},
    {"question": "1996年，老虎、熊貓和黑犀牛都列為瀕危動物。現在這3種動物裡，哪幾種面臨更迫切的危機？"
                 "（A）2種（B）1種（C）0種", "answer": "C"},
    {"question": "全球多少人口享有電力？"
                 "（A）20％（B）50％（C）80％", "answer": "C"},
    {"question": "全球氣象專家認為接下來一百年裡平均氣溫會⋯⋯"
                 "（A）更暖（B）一樣（C）更冷", "answer": "A"}
]

class CreateTestPool:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class TestGenerator:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def is_last_questions(self):
        return self.question_number < len(self.question_list)

    def generate_next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.question} (A/B/C)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\t 答案正確！")
        else:
            print("\t 答案錯誤！")
        print(f"\t 正確答案是 {correct_answer}.")
        print(f"\t 你的分數: {self.score}/{self.question_number}.")

    def get_score(self):
        return self.score

# create a test pool
test_pool = []
for fact in fact_data:
    fact_obj = CreateTestPool(fact["question"], fact["answer"])
    test_pool.append(fact_obj)

# do fact test
fact_test = TestGenerator(test_pool)

while fact_test.is_last_questions():
    fact_test.generate_next_question()

# comments
print(f"你的總分: {fact_test.score}/{fact_test.question_number}.")

if fact_test.get_score() > 4:
    print("恭喜你答得比黑猩猩好！")
elif fact_test.get_score() == 4:
    print("黑猩猩4ni?")
else:
    print("趕快買本書來看吧！")
