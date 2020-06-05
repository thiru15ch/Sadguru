from flask import Flask, render_template, url_for, flash, redirect, request
from forms import AddItemForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os
from werkzeug import secure_filename
# from flask_uploads import IMAGES,UploadSet,configure_uploads,patch_request_class


# basedir = os.path.abspath(os.path.dirname(_file_))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f2867be10e229aa5596efe304903137'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sadguru'

picFolder = os.path.join('static','item_thumbnail')

app.config['UPLOAD_FOLDER'] = picFolder

# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir,'static/item_thumbnail')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app, None)

db = SQLAlchemy(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False, default = 0)
    status = db.Column(db.Integer)
    # thumbnail = db.Column(db.String(20),nullable=False, default = 'default.jpg')
    image_file = db.Column(db.String(150), nullable=False, default = 'default.jpg')
    
    def __repr__(self):
        return f"Items('{self.name}', '{self.description}', '{self.price}', '{self.status}', '{self.image_file}' )"


@app.route("/")
def home():
    # return f'Home page'
    return redirect('/additem')




@app.route("/additem", methods = ['GET', 'POST'])
def additem():   

    items = Items.query.filter(Items.status == 0).all()    
    form = AddItemForm()

    # if request.method == 'POST' and form.validate():
    image_file = None

    # if form.validate_on_submit():
    if request.method == 'POST':
        name = form.name.data
        description = form.description.data
        price = form.price.data
            # thumbnail = form.thumbnail.data

        f= request.files['file1']
        
        if f.filename != '':
            
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            # photos.save(request.files.get('image_file'))   

            image_file= os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        # print(thumbnail)
            print(image_file)

        else:
            image_file = None

        entry = Items(name = name, description = description, price = price, status = 0 , image_file= image_file)
        db.session.add(entry)
        db.session.commit()
        flash(f'New Item "{form.name.data}" Added succesfully!','success')
        return redirect('/additem')

    return render_template('additem.html',title='AddItem', form=form,items = items, image_file=image_file)



@app.route("/delete/<int:id>/<string:name>", methods = ['GET', 'POST'])
def delete(id,name):
    item = Items.query.filter_by(id=id).update(dict(status='1'))    
       
    # db.session.delete(item)
    db.session.commit()
    flash(f'Item "{name}" Deleted succesfully!','success')
    return redirect('/additem')



@app.route("/item/<int:id>", methods = ['GET', 'POST'])
def item(id):    
    item = Items.query.get(id)    
    return render_template('items.html',item = item)


if __name__ == '__main__':
    app.run(debug=True)



#     itemDetails = request.form
    #     name = itemDetails['name']
    #     description = itemDetails['description']
    #     price = itemDetails['price'] 
    #     cur = mysql.connection.curser()
    #     cur.execute("INSERT INTO items(name,description,price) VALUES(%s,%s,%d)", (name,description,price))
    #     mysql.connection.commit()
    #     cur.close()        
