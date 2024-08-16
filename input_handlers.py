from typing import Optional

import tcod.event
from tcod.event import T

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action]=None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT: #TODO: replace tcod.event.K_LEFT` should be replaced with tcod.event.KeySym
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action=EscapeAction()

        return action