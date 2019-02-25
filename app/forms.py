from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField()