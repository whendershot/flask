import inspect

from flask.sessions import SecureCookieSession

import game.commands

class VisitController():
    """"""

    def __init__(self) -> None:
        self.available_commands = {}

        for name, obj in inspect.getmembers(game.commands, lambda member : inspect.isclass(member) and member.__module__ == 'game.commands'):
            self.available_commands[name] = obj

        print(self.available_commands)

    def execute(self, command: str, target: SecureCookieSession) -> None:
        print(f'VisitController: target{target}')
        transaction = self.available_commands[command]()
        transaction.execute(target)

    def get_commands(self):
        result = []
        for k,v in self.available_commands.items():
            result.append(
                {
                    "name" : k, 
                    "description" : v.describe_string(),
                    "display_name" : v.display_name()
                }
            )
        return result

