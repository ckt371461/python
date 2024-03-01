from flask import Flask,render_template,request
app=Flask(__name__)
#app=Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def home():
    thing=request.values.get('thing')
    height=request.values.get('height')
    color=request.values.get('color')
    # home.html 要放在同一層中的templates資料夾中，不然會出錯
    return render_template('home.html',thing=thing,height=height,color=color)
# 用 http讀取而不是https
app.run(port=5000,debug=True)

# http://localhost:5000/?thing=1&height=2&color=3