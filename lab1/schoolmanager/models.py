from schoolmanager import db, login_manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    message = db.Column(db.String(200))
    remark = db.Column(db.String(200))

    def __init__(self, name, message, remark ):
        self.name = name
        self.message = message
        self.remark = remark

    def __repr__(self):
        return '<Department %d %s>' % (self.id, self.name)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    sex = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(50))
    department_name = db.Column(db.String(100), db.ForeignKey('department.name'))

    def __init__(self, name, sex, age, grade, department_name):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade
        self.department_name = department_name

    def __repr__(self):
        return 'Student %s %s %d>' % (self.name, self.sex, self.age)


class Course(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    kind = db.Column(db.String(80))
    capacity = db.Column(db.Integer)
    grade = db.Column(db.Float)
    department_name = db.Column(db.String(100), db.ForeignKey('department.name'))

    def __init__(self, name, kind, capacity, grade, department_name):
        self.name = name
        self.kind = kind
        self.capacity = capacity
        self.grade = grade
        self.department_name = department_name

    def __repr__(self):
        return '<Course %d %s>' % (self.id, self.name)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    sex = db.Column(db.String(50))
    age = db.Column(db.Integer)
    identity = db.Column(db.String(80))
    department_name = db.Column(db.String(100), db.ForeignKey('department.name'))

    def __init__(self, name, sex, age, identity, department_name):
        self.name = name
        self.sex = sex
        self.age = age
        self.identity =identity
        self.department_name = department_name

    def __repr__(self):
        return '<Teacher %d %s>' % (self.id, self.name)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
