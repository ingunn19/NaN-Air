from UI_API import UI_Api
SPACER = "_____________________________________________"
class NoTask:
    def __init__(self):
        self.__UI_API = UI_Api()
    def no_task(self):
        task_day = input("Choose a day: ")
        print("Here we list all employees without a task!")
        self.__UI_API.get_day_no_task(task_day)
        input()
        print(SPACER)