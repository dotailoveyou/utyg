
class Button:
    a = 0
    def click(self):
        self.a = self.a + 1

    def click_count(self):
        print(self.a)

    def reset(self):
        self.a = 0

bu = Button()
bu.click()
bu.click_count()
bu.reset()