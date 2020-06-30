from mycroft import MycroftSkill, intent_file_handler


class LightsChangeState(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('state.change.lights.intent')
    def handle_state_change_lights(self, message):
        self.speak_dialog('state.change.lights')


def create_skill():
    return LightsChangeState()

