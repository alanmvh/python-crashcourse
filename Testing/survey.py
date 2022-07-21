class AnonymousSurvey():
    """Collect anonymous answers to a survey question"""

    def __init(self, question):
        """Store a question and prepare to store responses"""
        self.question = question = question
        self.respones = []

    def show_question(self):
        """Show the survey question"""
        print(question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.respones.append(new_response)
        
    def show_results(self):
        """Show al the responses that have been given"""
        print("Survey results")
        for response in responses:
            print('-' + response)