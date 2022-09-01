from flask import flash, make_response, redirect, render_template, url_for
from pydub import AudioSegment
from werkzeug.utils import secure_filename

from app import app
from app.forms import UploadForm


@app.route("/")
def index():
    """
    Serve the application home page
    """
    for upload_file in app.config["UPLOADS"].iterdir():
        upload_file.unlink()

    return render_template("index.html")


ALLOWED_EXTENSIONS = set(["wav", "mp3"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        for file in form.files.data:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = app.config["UPLOADS"] / filename
                file.save(filepath)
        flash("File(s) successfully uploaded")
        return redirect(url_for("rename"))

    return render_template("upload.html", form=form)


@app.route("/rename", methods=["GET", "POST"])
def rename():
    filenames = []
    for upload_file in app.config["UPLOADS"].iterdir():
        filename = upload_file.name
        filename_length = len(upload_file.stem)
        duration = audio_length(upload_file)
        filenames.append((filename, filename_length, duration))
    print(filenames)
    return render_template("rename.html", filenames=filenames)


# TODO: Format audio duration as MM:SS
# TODO: Support MP3 format via AudioSegment.from_file(p, ext)
def audio_length(filepath):
    audio = AudioSegment.from_wav(str(filepath))
    duration_minutes = int(audio.duration_seconds // 60)
    duration_seconds = round((audio.duration_seconds % 60), 3)
    return f"{duration_minutes}:{duration_seconds}"