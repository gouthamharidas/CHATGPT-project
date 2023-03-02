from generate_cover_letter import generate_cover_letter
from generate_interview_questions import generate_interview_questions
from generate_resume1 import generate_resume_text
from analyze_job_fit import analyze_job_fit1
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session
from flask_migrate import Migrate


application = app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5433/flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = "12345"





class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), unique=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.Name


@app.route("/")
def home():
    return render_template("home.html")





@app.route('/home2')
def home2():
    return render_template('home2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        print("Form Email: ", email)
        print("Form password: ", password)

        # Fetch user from the database
        user = Users.query.filter_by(Email=email).first()
        print("User from database: ", user)

        # Check if user exists and the password is correct
        if user and bcrypt.verify(password, user.password):
            print("Password verified.")
            # Login the user by creating a session
            session['email'] = email

            # Redirect to a desired page
            return redirect(url_for('home2'))
        else:
            print("Login failed.")
            # Return error message
            return render_template('login.html', message="Login failed.")
    else:
        # Return the login page
        return render_template('login.html')





@app.route('/generate', methods=['GET','POST'])
def generate():
    if request.method == 'POST':
        job_requirements = request.form['job_requirements']
        resume_keywords = request.form['resume_keywords']       

        if not job_requirements or not resume_keywords:
            return 'Please enter job requirements and resume keywords'
        cover_letter = generate_cover_letter(job_requirements, resume_keywords)
        interview_questions = generate_interview_questions(job_requirements)
        

        return redirect(url_for('generate_letter', cover_letter=cover_letter, interview_questions=interview_questions ))
    return render_template("index.html")    





@app.route("/services", methods=['POST', 'GET'])
def services():
    if request.method == 'GET':
        return render_template("services.html")
    else:
        return 'Method Not Allowed', 405



@app.route("/analysis", methods=['POST', 'GET'])
def analysis():
    if request.method == 'GET':
        return render_template("analysis.html")
    else:
        return 'Method Not Allowed', 405





@app.route("/products", methods=['POST', 'GET'])
def products():
    
    return render_template("products.html") 


@app.route("/profile", methods=['POST', 'GET'])
def profile():
    
    return render_template("profile.html") 




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('Name')
        email = request.form.get('email')  # added this line
        password = request.form.get('password')
        hashed_password = bcrypt.hash(password)


        # Check if email already exists in the database
        existing_user = Users.query.filter_by(Email=email).first()
        if existing_user:
            return 'Error: Email already exists'
        # Create new user
        new_user = Users(Name=name, Email=email, password=hashed_password)
          # changed this line
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('signup.html')






@app.route('/signup_submit', methods=['POST'])
def signup_submit():
    name = request.form['Name']
    email = request.form['Email']
    password = request.form['password']
    user = Users(Name=name, Email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return 'User added successfully'
    

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    job_requirements = request.form['job_requirements']
    interview_questions = generate_interview_questions(job_requirements)
    return render_template('generate_questions.html', interview_questions=interview_questions)

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    job_requirements = request.form['job_requirements']
    Name = request.form['Name']
    Phone_number = request.form['Phone_number']
    Email_id = request.form['Email_id']
    Work_experience = request.form['Work_experience']
    Education = request.form['Education']
    resume = generate_resume_text(job_requirements, Name, Email_id, Work_experience, Education, Phone_number)
    return render_template('generate_resume_page.html', resume=resume)


@app.route('/generate_analysis', methods=['POST'])
def generate_analysis():
    job_requirements = request.form['job_requirements']
    resume_keywords = request.form['resume_keywords']
    work_experience = request.form['work_experience']
    analysis = analyze_job_fit1(job_requirements, resume_keywords, work_experience)
    return render_template('analysis_result.html', analysis=analysis)


 

@app.route('/generate_letter')
def generate_letter():
    cover_letter = request.args.get('cover_letter')
    return render_template('generate.html', cover_letter=cover_letter)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
