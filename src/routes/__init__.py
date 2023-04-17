from . import lobbies, users, arsenal

__routes__ = (
    lobbies.router,
    users.router,
    arsenal.router
)