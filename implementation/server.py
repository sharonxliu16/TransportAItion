from flask import Flask, render_template
from AI.kmeans import main
import time
app = Flask(__name__)

# set up base page routing 
@app.route('/')
def index():
  return render_template('index.html')

#call kmeans algorithm and display result
@app.route('/my-link/')
def my_link():
  print("2")
  main()
  time.sleep(1)
  return render_template('imgdisplay.html')

if __name__ == '__main__':
  app.run(debug=True)