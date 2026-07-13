from database.db import db

from models.log import Log


class LogRepository:

    def add_log(

            self,

            username,

            action):

        log = Log(

            username=username,

            action=action

        )

        db.session.add(

            log

        )

        db.session.commit()

    def get_all_logs(self):

        return Log.query.order_by(

            Log.created_at.desc()

        ).all()

    def delete_all_logs(self):

        Log.query.delete()

        db.session.commit()

    def log_count(self):

        return Log.query.count()