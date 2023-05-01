import requests

class DataGenerator:

    def __init__(self,no_of_questions,difficulty_level):
        self.question_data = []
        self.no_of_questions = no_of_questions
        self.difficulty_level = difficulty_level


    def generate_question_data_from_trivia(self):
        
        trivia_api_url = f"https://opentdb.com/api.php?amount={self.no_of_questions}&difficulty={self.difficulty_level.lower()}&type=boolean"
        trivia_api_response = requests.get(
            url= trivia_api_url,
            headers={'Content-Type': 'application/json'}
        )

        if int(trivia_api_response.status_code) == 200:
            response_json = trivia_api_response.json()
            results_list = response_json['results']

            for result in results_list:
                self.question_data.append({
                    "text": result["question"],
                    "answer": result["correct_answer"]
                })

            return self.question_data
        
        else:
            raise Exception('There is some error with API Response. Kindly debug!')