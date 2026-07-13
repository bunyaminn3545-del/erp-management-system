from models.user import User

from repositories.user_repository import UserRepository

from services.log_service import LogService


class AuthService:

    def __init__(self):

        self.repository = UserRepository()

        self.log_service = LogService()

    def login(

            self,

            username,

            password):

        user = self.repository.get_user_by_username(

            username

        )

        if user is None:

            return False, "User not found."

        if not user.check_password(

                password):

            return False, "Incorrect password."

        self.log_service.write_log(

            username,

            "User logged in."

        )

        return True, user

    def register(

            self,

            username,

            password):

        if self.repository.username_exists(

                username):

            return False, "Username already exists."

        user = User(

            username=username

        )

        user.set_password(

            password

        )

        self.repository.add_user(

            user

        )

        self.log_service.write_log(

            username,

            "User registered."

        )

        return True, "User registered successfully."

    def get_all_users(self):

        return self.repository.get_all_users()

    def get_user(

            self,

            username):

        return self.repository.get_user_by_username(

            username

        )

    def change_password(

            self,

            username,

            old_password,

            new_password):

        user = self.repository.get_user_by_username(

            username

        )

        if user is None:

            return False, "User not found."

        if not user.check_password(

                old_password):

            return False, "Current password is incorrect."

        user.set_password(

            new_password

        )

        self.repository.update_user()

        self.log_service.write_log(

            username,

            "Password changed."

        )

        return True, "Password updated successfully."

    def delete_user(

            self,

            username):

        user = self.repository.get_user_by_username(

            username

        )

        if user is None:

            return False, "User not found."

        self.repository.delete_user(

            user

        )

        self.log_service.write_log(

            username,

            "User deleted."

        )

        return True, "User deleted successfully."

    def user_count(self):

        return self.repository.user_count()