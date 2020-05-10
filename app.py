from flask import Flask,render_template, request,redirect,url_for
from flask_mail import Mail
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "shivamranaemailcheck@gmail.com",
    MAIL_PASSWORD=  "SalonEverywhere"
)
mail = Mail(app)
@app.route('/')
def main():
    return render_template("main.html")

@app.route('/getLink', methods = ['POST'])
def getLink():
    if request.method == 'POST':
        email = request.form['email']
        number = request.form['number']   

        mail.send_message('Message from SalonEverwhere' ,
                          sender="shivamranaemailcheck@gmail.com",
                          recipients = [email],
                          body = "Hello,Your phone number is "+number+
                          "please open this Link for question is: https://saloneverywhere.herokuapp.com/question"
                          )

        return redirect(url_for('main'))


@app.route('/question',methods=['GET','POST'])
def question():
    if request.method == 'POST':
       
        return redirect(url_for('main'))

    return render_template('question.html')

@app.route('/thankyou',methods=['GET','POST'])
def thankyou(): 
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)
