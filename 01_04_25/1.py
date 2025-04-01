import sqlite3


class PasswordMan:
    _instances = {}

    def __new__(cls, account):
        if account not in cls._instances:
            cls._instances[account] = super().__new__(cls)
            cls._instances[account].account = account
            cls._instances[account].password = cls._load_password(account)
        return cls._instances[account]

    def __init__(self, account):
        self.password = None
        self.account = account
        self.connection = sqlite3.connect("db.sql")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        age INTEGER UNSIGNED
        )
        ''')
        self.connection.commit()

    @classmethod
    def _load_password(cls, account):
        connection = sqlite3.connect("db.sql")
        connection.cursor().execute(f'''
                SELECT password FROM USERS WHERE id = {account}
                ''')
        password = connection.cursor().fetchall()

        return password

    def set_password(self, password):
        self.password = password
        self._save_password()

    def _save_password(self, password):
        self.cursor.execute(f'''
                UPDATE Users SET password = {password} WHERE id = {self.account}
                ''')
        self.connection.commit()

    def get_password(self):
        return self.password

    def __del__(self):
        self.connection.close()