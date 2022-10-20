from flask_wtf import FlaskForm
from wtforms import FloatField, HiddenField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def my_validacion(form, field):
    if field.data != form.hidden_from.data:
        raise ValidationError("Debes volver a calcular la equivalencia")

class MyForm(FlaskForm):
    from_Q = FloatField("Cantidad From", validators = [DataRequired(), my_validacion])

    hidden_from = HiddenField()

    hidden_to = HiddenField()

    calcular = SubmitField("Calcular")
    comprar = SubmitField("Comprar")
