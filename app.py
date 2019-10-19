from flask import Flask, request, render_template, send_file
import os
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return "hello"



@app.route("/push", methods=['POST'])
def store():

    #TODO subject to change 
    
    filename = request.form.get("filename")
    course_id = request.form.get("course_id")
    z_id = request.form.get("z_id")

    print(filename)

 
    

    new_name = z_id + filename

    og_path = "./" + course_id + "/" + filename
    new_path = "./" + course_id + "/" + new_name
    os.rename(og_path, new_path)

    return "sucessfully uploaded"
  

@app.route("/pull", methods=['POST'])
def deliver():
    filename = ""
    course_id = request.form.get("course_id")
    z_id = request.form.get("z_id")
    path = "./" + course_id


    for file in os.listdir(path):
        if file.startswith(str(z_id)):
            filename += str(file)
            break
    
    path += "/" + filename


    return send_file(path, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document", attachment_filename=filename)


def save_link(book_link, book_name):
    the_book = requests.get(book_link, stream=True)
    with open(book_name, 'wb') as f:
      for chunk in the_book.iter_content(1024 * 1024 * 2):  # 2 MB chunks
        f.write(chunk)


    

if __name__ == "__main__":
    save_link("https://docs.google.com/document/d/1clwX6hstMzNE809UHVljWYKxA4BJY8jQV0BdgU8hH4s/edit?usp=sharing","./1531/ian.docx")
    app.run(debug=True)