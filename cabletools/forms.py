from wtforms import Form, validators, SelectField, StringField, IntegerField

# Form for Cable Calculator
class CalcForm(Form):
    footage = IntegerField('', validators=[validators.required()])
    cable = SelectField('Cable Type',
                        choices=[('P3_625', '625 P3'), ('P3_875', '875 P3'), ('P3_500', '500 P3'), ('RG6', 'RG6'),
                                 ('RG11', "RG11"), ('FLEX500', 'Flex 500'), ('540QR', '540 QR'), ('860QR', '860 QR'),
                                 ('500MC', '500 MC2'), ('750MC', '750 MC2')])

# For for Pathtrak Link Creator
class PathTrakForm(Form):
    node = StringField('', validators=[validators.required()])