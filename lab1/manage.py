

from schoolmanager import app, db
from flask_script import Manager
from schoolmanager.models import User, Department, Student, Course, Teacher

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 10):
        db.session.add(User('用户' + str(i), 'password' + str(i)))
    db.session.add(Department('学工处', '学生事务工作处', '全校区'))
    db.session.add(Department('计算机学院', '计算机学院和国家示范性软件学院', '一校区'))

    db.session.add(Student('耿志成', '男', 19, '大三', '计算机学院'))
    db.session.add(Student('张钰彬', '男', 20, '大三', '计算机学院'))

    db.session.add(Course('数据库系统', '必修', 200, 4.0, '计算机学院'))
    db.session.add(Course('大学生心理辅导', '选修', 100, 2.0, '学工处'))

    db.session.add(Teacher('李大锤', '男', 48, '教授', '计算机学院'))
    db.session.add(Teacher('王大炮', '男', 37, '教职工', '学工处'))

    db.session.commit()


if __name__ == '__main__':
    manager.run()
