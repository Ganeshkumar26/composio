from .action import Action
from typing import List


actions_require_workspace_factory = {"WorkspaceStatus": True,
                                     "SetupWorkspace": True,
                                     "CreateWorkspaceAction": True,
                                     "SetupGithubRepo": True,
                                     "GoToCmd": True,
                                     "CreateFileCmd": True,
                                     "OpenCmd": True,
                                     "EditFile": True,
                                     "RunCommandOnWorkspace": True,
                                     "ScrollDown": True,
                                     "ScrollUp": True,
                                     "SetCursors": True,
                                     "SearchDirCmd": True,
                                     "SearchFileCmd": True,
                                     "FindFileCmd": True}


class Tool():
    @property
    def tool_name(self) -> str:
        return self.__class__.__name__.lower()

    def actions(self) -> List[Action]:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def get_actions_dict(self) -> dict:
        action_objects_dict = {}

        for action_class in self.actions():
            action_instance = action_class(self.tool_name)
            if action_class.__name__ in actions_require_workspace_factory:
                action_instance.set_workspace_factory(self.get_workspace_factory())
            action_name = action_instance.get_tool_merged_action_name()

            action_objects_dict[action_name] = action_instance

        return action_objects_dict

    # def triggers(self) -> List[Trigger]:
    #     raise NotImplementedError("This method should be overridden by subclasses.")
