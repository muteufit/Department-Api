from __main__ import app, db, Sheets, Student
from flask import Flask, jsonify, request


@app.route('/students',methods=['GET'])
def students():
    students = Student.query.all()
    if len(students) > 0:
        studentList = []
        for student in students:
            studentList.append({'name': student.name, 'gender': student.gender,'id':student.id})
        return jsonify(studentList)
    else:
        return 'their\'s no Students'
# ===================================================

@app.route('/update_student/<int:id>',methods=['POST'])
def updateStudent(id):
    student = Student.query.get_or_404(id)

    student.name = request.json['name']
    student.gender = request.json['gender']

    try:
        db.session.commit()
        return 'Updated'
    except:
        return 'There was an issue updating Student'
# ===================================================
@app.route('/delete_student/<int:id>')
def deleteStudent(id):
    studentToDelete = Student.query.get_or_404(id)

    try:
        db.session.delete(studentToDelete)
        db.session.commit()
        return 'Deleted'
    except:
        return 'There was a problem deleting that Student'


# ===================================================

@app.route('/student',methods=['POST'])
def createStudent():
    jsonData = request.json
    try:
        student = Student(jsonData['name'],jsonData['gender'])
        db.session.add(student)
        db.session.commit()
        return 'created'
    except:
        return 'Error Has Occurd Check your json'
