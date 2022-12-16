from app import app
from flask import render_template

@app.route('/admin/')
def admin():
    return render_template("admin/admin.html")

@app.route('/admin/profile/')
def admin_profile():
    return "admin profile "

