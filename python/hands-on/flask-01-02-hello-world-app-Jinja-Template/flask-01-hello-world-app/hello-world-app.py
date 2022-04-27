from flask import Flask

app = Flask(__name__) #bir object olusturuyoruz

@app.route('/') #anasayfa/kokdizini DEKORETOR1 localhost:2000 
def hello():
    return "Hello World from Flask!!!"

@app.route('/second') #localhost:2000/second DEKORETOR2
def second():
    return 'Bize Her Yer Trabzon!!!!'

@app.route('/third/subthird') #localhost:2000/third/subthird DEKORETOR3
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')#localhost:2000/forth/6600777 DEKORETOR4
def forth(id):
    return f'Id number of this page is {id}'




if __name__ == '__main__': # kontrol mekanizmasini calistiriyoruz
    app.run(debug=True, port=2000)