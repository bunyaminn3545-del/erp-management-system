from repositories.log_repository import LogRepository


class LogService:

    def __init__(self):

        self.repository = LogRepository()

    def write_log(

            self,

            username,

            action):

        self.repository.add_log(

            username,

            action

        )

    def get_logs(self):

        return self.repository.get_all_logs()

    def clear_logs(self):

        self.repository.delete_all_logs()

    def log_count(self):

        return self.repository.log_count()