from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.boat import Boat
from flask_app.models.user import User


@app.route('/new/boat')

def new_boat():

    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        "id":session['user_id']
    }

    return render_template('add_product.html',user=User.get_by_id(data))


@app.route('/create/boat',methods=['POST'])
def create_boat():

    if 'user_id' not in session:
        return redirect('/logout')
    
    if not Boat.validate_boat(request.form):
        return redirect('/new/boat')
    
    data = {
        "name": request.form["name"],
        "serial_number": request.form["serial_number"],
        "content": request.form["content"],
        "purchase_date": request.form["purchase_date"],
        "user_id": session["user_id"]
    }

    Boat.save(data)

    return redirect('/dashboard')




@app.route('/edit/boat/<int:id>')

def edit_boat(id):

    if 'user_id' not in session:

        return redirect('/logout')
    
    data = {

        "id":id

    }

    user_data = {

        "id":session['user_id']

    }

    return render_template("edit_product.html",edit=Boat.get_one(data),user=User.get_by_id(user_data))



@app.route('/update/boat',methods=['POST'])

def update_boat():

    if 'user_id' not in session:

        return redirect('/logout')
    
    if not Boat.validate_boat(request.form):

        return redirect('/new/boat')
    
    data = {
        "name": request.form["name"],
        "serial_number": request.form["serial_number"],
        "content": request.form["content"],
        "purchase_date": request.form["purchase_date"],
        "id": request.form['id']
    }

    Boat.update(data)

    return redirect('/dashboard')




@app.route('/destroy/boat/<int:id>')

def destroy_boat(id):

    if 'user_id' not in session:

        return redirect('/logout')
    
    data = {
        "id":id
    }

    Boat.destroy(data)

    return redirect('/dashboard')