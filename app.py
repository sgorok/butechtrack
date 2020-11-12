from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#@app.route("/home")
def home():
    html_template = 'site.html'
    return render_template(html_template)

@app.route("/contact")
def contact():
  return render_template("contact.html")


if __name__ == "__main__":
    app.run()

