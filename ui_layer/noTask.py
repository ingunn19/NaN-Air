from ui_layer.uiAPI import UI_API

SPACER = "_______________________________________________________________________________________________________________________________________________________________________________"

class NoTask:
    def __init__(self):
        self.__UI_API = UI_API()

    def no_task(self):
        task_day = input("Choose a day: yyyy-mm-dd \n")
        self.__UI_API.get_day_no_task(task_day)
        input()
        print(SPACER)
