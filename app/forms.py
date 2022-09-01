from flask_wtf import FlaskForm
from wtforms import MultipleFileField


class UploadForm(FlaskForm):
    files = MultipleFileField("File(s) upload")