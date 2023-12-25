class Button:
    def __init__(self, message: str):
        self.message = message
    
    def push(self):
        print(self.message)

bigRedButton = Button('Go to https://adventofcode.com/2023/day/25 and click [Push The Big Red Button]')

bigRedButton.push()