class BasicTask:

    def __init__(self, name, desc) -> None:
        self.name = name
        self.desc = desc

class TextTask(BasicTask): pass

class PhotoTask(BasicTask):

    def __init__(self, name, desc, count) -> None:
        super().__init__(name, desc)
        self.count = count

class MarketingTask(BasicTask): pass

class PublishingTask(BasicTask): pass



class Basic_Specialist:

    def __init__(self, name) -> None:
        self.name = name

    def get_tasks(self):
        return [BasicTask]

    def do_task(self, task):
        print(f"{task} - I'm working on it!")

class Photographer(Basic_Specialist):

    def __init__(self, name, camera) -> None:
        super().__init__(name)
        self.camera = camera

    def get_tasks(self):
        return super().get_tasks() + [PhotoTask, PublishingTask]

class Tech_Writer(Basic_Specialist):

    def get_tasks(self):
        return super().get_tasks() + [TextTask, PublishingTask]

class Marketing_Manager(Basic_Specialist):

    def get_tasks(self):
        return super().get_tasks() + [MarketingTask, PublishingTask]

class Editory_Team:

    def __init__(self, photo, tech, mm) -> None:
        self.photo = photo
        self.mm = mm
        self.tech = tech

class Chief_Editor(Basic_Specialist):

    def __init__(self, name, tasks:list, team:list) -> None:
        super().__init__(name)
        self.tasks = tasks
        self.team = team

    def process(self):
        for task in self.tasks:
            for s in self.team:
                if type(task) in s.get_tasks():
                    s.do_task(task)