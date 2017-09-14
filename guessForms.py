from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Required, NumberRange
	
class PasswordGuesserForm(FlaskForm):
	add_component = StringField('add a component', validators= [DataRequired(message='it can not be empty'), 
														Length(1, 60)])
	add = SubmitField('Add Component')
	rm_component = StringField('remove a component', validators= [DataRequired(message='it can not be empty'), 
														Length(1, 60)])						
	# PIN = PasswordField('PIN', validators =[DataRequired(message='can not be empty')])
	remove = SubmitField('Remove Component')
	review = SubmitField('Review Component')
	generate = SubmitField('Generate new combination')
	correct = SubmitField('Mark Correct password')
	incorrect = SubmitField('Unmark Correct password')
	wrong = SubmitField('Wrong and Keep going')
	undo = SubmitField('undo')
	redo = SubmitField('Redo')