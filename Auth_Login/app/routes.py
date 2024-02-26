# Flask modules
from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required

# Local modules
from app.models import User
from app.extensions import db, bcrypt, login_manager
from app.forms import LoginForm, RegistrationForm

routes_bp = Blueprint('routes', __name__, url_prefix="/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@routes_bp.route("/")
@login_required
def home():
    return render_template('index.html')


@routes_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("routes.home"))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember_me.data

        user = User.query.filter_by(email=email).one_or_none()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember_me)
            flash(f"Logged in successfully as {user.name}", 'success')
            return redirect(url_for("routes.home"))
        else:
            flash("Invalid email or password", 'danger')

    return render_template('auth/login.html', form=form)


@routes_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("routes.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hashed_password = bcrypt.generate_password_hash(password)

        # Add user to database
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Login user
        login_user(new_user)

        flash(f'Account created successfully! You are now logged in as {new_user.name}.', 'success')
        return redirect(url_for("routes.home"))

    return render_template('auth/register.html', form=form)


@routes_bp.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("routes.login"))
