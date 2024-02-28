from contextlib import contextmanager


class UnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, type, value, traceback):
        if type is not None:
            self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    @contextmanager
    def start(self):
        if self.session is not None:
            raise RuntimeError("Session already started")
        self.session = self.session_factory()
        try:
            yield self.session
            self.commit()
        except Exception:
            self.rollback()
            raise
        finally:
            self.session.close()
            self.session = None
