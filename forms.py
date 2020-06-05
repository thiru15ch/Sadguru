from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,SubmitField	, IntegerField, validators, TextAreaField
from wtforms.validators import DataRequired, Length


class AddItemForm(FlaskForm):
	name = StringField('<b>Item Name</b>', validators=[DataRequired(), validators.Length(min=2, max=20)])
	description = TextAreaField('<b>Description</b>', validators=[DataRequired(), Length(min=2, max=100)])
	price = IntegerField('<b>Price (in Rs.)</b>', validators=[DataRequired(), validators.Length(min=1, max=4)])
	image_file = FileField('<b>Upload Image</b>', validators=[FileAllowed(['jpg', 'png'])])
	



