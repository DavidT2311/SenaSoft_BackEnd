from app.core.database import async_session


class UnitOfWork:
    def __init__(self, session_factory=async_session):
        self.session_factory = session_factory
        self.session = None

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc:
            await self.session.rollback()
        else:
            await self.session.commit()
        await self.session.close()
