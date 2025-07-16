# ~ Import Important Library
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user




# ~ set Flask ~
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE

class Base(DeclarativeBase):
    pass
    
app = database.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///users.db"
    
database = SQLAlchemy(model_class=Base)
database.init_app(app)


# ~ CREATE TABLE IN DATABASE ~

class User(database.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    database.create_all()



# ~ Customer/Users security libraries ~
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user



# ~ Use Flask-Login Package to make routes  only accessible if a user is authenticated. ~
login_manager = LoginManager()
login_manager.init_app(app)



# ~ Now I'm creating user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return database.get_or_404(User, user_id) # ~ Parameters (User - Which class you wanna use) (user_id - Which item you wanna get) ~


# CREATE TABLE IN DATABASE (UserMixin)
class User(UserMixin, database.model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True) # ~ Unique parameter will set 'email' key as unique value (Cannot be duplicated) ~
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.context(): # ~ Set changes ~
    database.create_all()




@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated) # ~ set logged_in so you can use it in .html (Passing either True or False if the user is authenticated) ~


@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST': 
        email = request.form.get('email')
        result = database.session.execute(database.select(User).where(User.email == email))
        # ~ Email in database have unique paramater so will only have one result. ~ 
        user = result.scalar()
        if user:
            # ~ If there is user who already exists ~ 
            flash("Feedback about signed up with that email, log in")
            return redirect(url_for('login'))

        
        hash_salted_password = generate_password_hash(
            request.form.get('password'), 
            method='pbkdf2:sha256', 
            salt_length=15,
        ) # ~ Hashing & Salting Password using Werkzeug for better customer security ~
        
        
        user = User(
            email = request.form.get['email'], # ~ request.form allow us to get email items from .html ~
            name = request.form.get['name'],
            password = hash_salted_password,
        )
        
        database.session.add(user)
        database.session.commit()

        login_user(user) # ~ Log in and authenticated user after updating database ~
        # ~ Redirect users to secrets page ~
        return redirect(url_for('secrets'))
                        
    return render_template('register.html', logged_in=current_user.is_authenticated)


    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST": # ~ If the user type/change smth on page ~
        email = request.form.get('email')
        password = request.form.get('pasword')

        # ~ Now we have to find user by email ~ 
        outcomes = database.session.execute(database.select(User).where(User.email == email)) # ~ Use database.select('Class') and .where( something is true or not - Almost like 'if' statement) ~
        user = outcomes.scallars() # ~ Get one item from database ~

        # ~ Set a feedback (use 'flash') if the email or password  incorrect ~

        if not user:
            flash('That email is incorrect or does not exist, try again')
        return redirect(url_for('login'))


        # ~ Now I'm checking stored hash password against entered password hashed, (use check_password_hash() function) ~
        elif not check_password_hash(user.password, password):
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
        
        else:
                login_user(user)  # ~ If successful then you can set user to authenticated ~
                return redirect(url_for('secrets')) # ~ redirect authenticated user to secrets page ~

        return render_template("login.html", logged_in=current_user.is_authenticated)  # ~ Otherwise user will stay in login page ~



@app.route('/secrets')
@login_required # ~ Only if user is authenticated / logged-in ~
def secrets():
    print(current_user.name) # ~ Greeting users by their own name ~
    return render_template('secrets.html', name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user() # ~ logout user ~
    return redirect(url_for('home'))
    
    
# ~ Only for authenticated customers / users ~
@app.route('/download', methods = ["POST"])
@login_required # ~ Only if user is authenticated / logged-in ~
def download():
    return send_from_directory(('static', path="files/cheat_sheet.pdf") # ~ Read more about send_from_directory (It will redirect us to file) ~
                               

# ~ OPTIONAL (You can add your port in app.run as parameter
if __name__ == "__main__":
    app.run(debug=True)
