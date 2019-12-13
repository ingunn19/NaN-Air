from ui_layer.uiAPI import UI_API

SPACER = "____________________________________________________________________________________________________________________________________________________________________________"

class WithTask:
    def __init__(self):
        self.__UI_API = UI_API()

    def with_task(self):
        print("Choose a day: yyyy-mm-dd")
        try:
            task_day = input()
            self.__UI_API.get_day_with_task(task_day)
        except ValueError:
            print("No tasks on this week")


        input()
        print(SPACER)
