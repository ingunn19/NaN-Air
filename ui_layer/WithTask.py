from UI_API import UI_Api
SPACER = "_____________________________________________"
class WithTask:
    def __init__(self):
        self.__UI_API = UI_Api()
    def with_task(self):
        print("Choose a day: yyyy, mm, dd")
        task_day = input()
        print("Here we list all employees with task!")
        self.__UI_API.get_day_with_task(task_day)
        input()
        print(SPACER)