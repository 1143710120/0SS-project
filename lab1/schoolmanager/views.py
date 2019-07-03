from schoolmanager import app, db
from flask import render_template, redirect, request, flash, get_flashed_messages, jsonify
from schoolmanager.models import Department, Student, Course, Teacher, User
from flask_login import login_user, logout_user, login_required, current_user
import hashlib


@app.route('/')
@login_required
def index():
    return render_template("index.html")


@app.route('/department/')
def department():
    departments = Department.query.all()
    return render_template('department.html',departments = departments)


@app.route('/student/')
def student():
    students = Student.query.all()
    return render_template('student.html',students =students)


@app.route('/course/')
def course():
    courses = Course.query.all()
    return render_template('course.html',courses = courses )


@app.route('/teacher/')
def teacher():
    teachers = Teacher.query.all()
    return render_template('teacher.html',teachers = teachers)


@app.route('/user/')
def user():
    users = User.query.all()
    return render_template('user.html',users = users)


@app.route('/updatePwd/')
def updatePwd():
    return render_template('updatePwd.html')


@app.route('/admin/')
@login_required
def admin():
    if current_user.username != 'admin':
        return render_template("index.html",msg = '您没有访问权限')
    return render_template('admin.html')


@app.route('/regloginpage/')
def regloginpage():
    msg = ''
    for m in get_flashed_messages(with_categories=False, category_filter=['reglogin']):
        msg = msg + m
    return render_template("login.html", msg=msg)


@app.route('/add_department/', methods={'get', 'post'})
def add_department():
    name = request.values.get('name').strip()
    message = request.values.get('message').strip()
    remark = request.values.get('remark').strip()
    db.session.add(Department(name, message, remark))
    db.session.commit()
    return redirect('/department/')


@app.route('/delete_department/', methods={'get', 'post'})
def delete_department():
    tid = request.form['id']
    Department.query.filter_by(id = tid).delete()
    db.session.commit()
    return jsonify({"msg": 'success' })


@app.route('/edit_department/', methods={'get', 'post'})
def edit_department():
    id = request.form['id']
    name = request.form['department_name']
    message = request.form['message']
    remark = request.form['remark']
    Department.query.filter_by(id=id).update({'name' : name, 'message' : message , 'remark': remark})
    db.session.commit()
    return jsonify({'msg' : 'OK'})

@app.route('/add_student/', methods={'get', 'post'})
def add_student():
    name = request.values.get('name').strip()
    sex = request.values.get('sex').strip()
    age = request.values.get('age').strip()
    grade = request.values.get('grade').strip()
    department_name = request.values.get('department_name').strip()
    if Department.query.filter_by(name=department_name).all() == []:
        return redirect('/student/')
    db.session.add(Student(name, sex, int(age), grade, department_name))
    db.session.commit()
    return redirect('/student/')

@app.route('/delete_student/', methods={'get', 'post'})
def delete_student():
    tid = request.form['id']
    Student.query.filter_by(id = tid).delete()
    db.session.commit()
    return jsonify({"msg": 'success' })

@app.route('/edit_student/', methods={'get', 'post'})
def edit_student():
    id = request.form['id']
    name = request.form['name']
    sex = request.form['sex']
    age = request.form['age']
    grade = request.form['grade']
    department_name = request.form['department_name']
    if Department.query.filter_by(name=department_name).all() == []:
        return jsonify({'msg' : 'wrong'})
    Student.query.filter_by(id=id).update({'name' : name, 'sex' :sex, 'age': int(age), 'grade' : grade, 'department_name' : department_name})
    db.session.commit()
    return jsonify({'msg' : 'OK'})

@app.route('/add_course/', methods={'get', 'post'})
def add_course():
    name = request.values.get('name').strip()
    kind = request.values.get('kind').strip()
    capacity = request.values.get('capacity').strip()
    grade = request.values.get('grade').strip()
    department_name = request.values.get('department_name').strip()
    if Department.query.filter_by(name=department_name).all() == []:
        return redirect('/course/')
    db.session.add(Course(name,kind, int(capacity), float(grade), department_name))
    db.session.commit()
    return redirect('/course/')

@app.route('/delete_course/', methods={'get', 'post'})
def delete_course():
    tid = request.form['id']
    Course.query.filter_by(id = tid).delete()
    db.session.commit()
    return jsonify({"msg": 'success' })

@app.route('/edit_course/', methods={'get', 'post'})
def edit_course():
    id = request.form['id']
    name = request.form['name']
    kind = request.form['kind']
    capacity = request.form['capacity']
    grade = request.form['grade']
    department_name = request.form['department_name']
    if Department.query.filter_by(name=department_name).all() == []:
        return jsonify({'msg' : 'wrong'})
    Course.query.filter_by(id=id).update({'name': name, 'kind': kind, 'capacity': int(capacity), 'grade': float(grade), 'department_name': department_name})
    db.session.commit()
    return jsonify({'msg' : 'OK'})

@app.route('/add_teacher/', methods={'get', 'post'})
def add_teacher():
    name = request.values.get('name').strip()
    sex = request.values.get('sex').strip()
    age = request.values.get('age').strip()
    identity = request.values.get('identity').strip()
    department_name = request.values.get('department_name').strip()
    if Department.query.filter_by(name=department_name).all() == []:
        return redirect('/teacher/')
    db.session.add(Teacher(name, sex, int(age), identity, department_name))
    db.session.commit()
    return redirect('/teacher/')

@app.route('/delete_teacher/', methods={'get', 'post'})
def delete_teacher():
    tid = request.form['id']
    Teacher.query.filter_by(id = tid).delete()
    db.session.commit()
    return jsonify({"msg": 'success' })

@app.route('/edit_teacher/', methods={'get', 'post'})
def edit_teacher():
    id = request.form['id']
    name = request.form['name']
    sex = request.form['sex']
    age = request.form['age']
    identity = request.form['identity']
    department_name = request.form[' department_name']
    if Department.query.filter_by(name=department_name).all() == []:
        return jsonify({'msg': 'wrong'})
    Teacher.query.filter_by(id=id).update({'name': name, 'sex': sex, 'age': int(age), 'identity': identity, 'department_name': department_name})
    db.session.commit()
    return jsonify({'msg' : 'OK'})

@app.route('/adduser/', methods={'get', 'post'})
def adduser():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    m = hashlib.md5()
    m.update(password.encode("utf8"))
    password = m.hexdigest()
    db.session.add(User(username, password))
    db.session.commit()
    return redirect('/user/')

@app.route('/delete_user/', methods={'get', 'post'})
def delete_user():
    tid = request.form['id']
    User.query.filter_by(id = tid).delete()
    db.session.commit()
    return jsonify({"msg": 'success' })

@app.route('/edit_user/', methods={'get', 'post'})
def edit_user():
    id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    User.query.filter_by(id=id).update({'username' : username, 'password' : password})
    db.session.commit()
    return jsonify({'msg' : 'OK'})



@app.route('/changepassword/', methods={'get', 'post'})
def changepassword():
    password1 = request.values.get('password1').strip()
    password2 = request.values.get('password2').strip()
    m = hashlib.md5()
    m.update(password1.encode("utf8"))
    password1 = m.hexdigest()
    n = hashlib.md5()
    n.update(password2.encode("utf8"))
    password2 = n.hexdigest()
    if User.query.filter_by(id=current_user.id).all()[0].password == password1 :
        User.query.filter_by(id=current_user.id).update({'password' : password2})
    db.session.commit()
    return redirect('/updatePwd/')


@app.route('/reg/', methods={'get', 'post'})
def reg():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    user = User.query.filter_by(username=username).first()
    if username == '' or password == '':
        flash('用户名和密码不能为空', 'reglogin')
        return redirect('/regloginpage/')
    if user != None:
        flash('用户名已经存在', 'reglogin')
        return redirect('/regloginpage/')

    m = hashlib.md5()
    m.update(password.encode("utf8"))
    password = m.hexdigest()
    user = User(username, password)
    db.session.add(user)
    db.session.commit()

    login_user(user)
    if user.username == 'admin':
        return redirect('/admin/')
    return redirect('/')


@app.route('/logout/')
def logout():
    logout_user()
    return redirect('/')


@app.route('/login/', methods={'get', 'post'})
def login():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()
    user = User.query.filter_by(username=username).first()
    if username == '' or password == '':
        flash('用户名和密码不能为空', 'reglogin')
        return redirect('/regloginpage/')
    if user == None:
        flash('该用户不存在', 'reglogin')
        return redirect('/regloginpage/')
    m = hashlib.md5()
    m.update(password.encode("utf8"))
    password = m.hexdigest()
    if password == user.password:
        login_user(user)
        if user.username == 'admin':
            return redirect('/admin/')
        return redirect('/')
    else:
        flash('密码错误，请重新输入', 'reglogin')
        return redirect('/regloginpage/')
