from database.db import db

from models.user import User


class UserRepository:

    def get_all_users(self):

        return User.query.order_by(

            User.user_id

        ).all()

    def get_user_by_username(

            self,

            username):

        return User.query.filter_by(

            username=username

        ).first()

    def add_user(

            self,

            user):

        db.session.add(

            user

        )

        db.session.commit()

    def update_user(self):

        db.session.commit()

    def delete_user(

            self,

            user):

        db.session.delete(

            user

        )

        db.session.commit()

    def username_exists(

            self,

            username):

        return self.get_user_by_username(

            username

        ) is not None

    def user_count(self):

        return User.query.count()