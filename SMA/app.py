from flask import Flask,render_template,flash,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import RadioField,SubmitField,StringField
from my_validators import DataRequired,KeyRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

valid_keys = ['123','456']

app.config['SECRET_KEY'] = 'any secret string'

app.config['list_of_bands'] = ['Skyride',
 'Просто Гриша',
 'LYCØRIS',
 'Осколки зеркала культуры',
 'Shape of songs',
 'Roquette',
 'One Piece Band',
 'M.O.O.N.',
 'Всё никак']

class SMAForm(FlaskForm):
    band = RadioField('Label', choices=[(i,i) for i in app.config['list_of_bands']],default=app.config['list_of_bands'][0], validators=[DataRequired()])
    validation_key = StringField('Код',validators=[DataRequired(),KeyRequired(current_list=valid_keys)])
    submit = SubmitField('Проголосовать')

@app.route('/',methods=['GET','POST'])
def hello_world():
    sma_form = SMAForm()
    if sma_form.validate_on_submit():
        print(sma_form.band.data, sma_form.validation_key.data)
        return render_template('thanks.html')
    else:
        for error in sma_form.errors:
            print(error)
    return render_template('index.html', form = sma_form)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5050)
