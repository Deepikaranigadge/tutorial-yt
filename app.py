from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        name = request.form['name']
        course = request.form['course']

        return render_template(
            'student.html',
            roll_no=roll_no,
            name=name,
            course=course
        )

    return render_template('student.html')


if __name__ == '__main__':
    app.run(debug=True)
