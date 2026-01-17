# from django import forms

# class ContactForm(forms.Form):
#     fname = forms.CharField(max_length=100,label="Fullname",help_text="Please Fill the fullname and allow only characters.",min_length=5,required=True,widget=forms.TextInput({'id':'fname','placeholder':'Enter Fullname..','class': 'form-control'}))
#     color = forms.CharField(widget=forms.TextInput({'type':'color', 'class': 'form-control form-control-color'}))
#     price = forms.CharField(widget=forms.TextInput(attrs={
#             'type': 'range',
#             'min': 100,
#             'max': 5000,
#             'class': 'form-range'
#         }))
#     choice=[
#         ('m','Male'),
#         ('f','Female'),
#         ('o','Other')
#     ]
#     gender = forms.CharField(widget=forms.RadioSelect(choices=choice))
#     choice1=[
#         ('a','A'),
#         ('b','B'),
#         ('c','C')
#     ]
#     hobbie = forms.MultipleChoiceField(choices=choice1,
#         widget=forms.CheckboxSelectMultiple,
#         label="Hobbie")
#     choice2=[
#         ('','--Select Country--'),
#         ('IND','India'),
#         ('PAK','Pakistan'),
#         ('US','USA')
#     ]
#     country = forms.ChoiceField(
#         choices=choice2,
#         label="Country",
#         widget=forms.Select({'class': 'form-control'})
#     )
#     choice3=[
#         ('P','PLANNING'),
#         ('Q','QUITE'),
#         ('R','RASOI')
#     ]
#     skills = forms.MultipleChoiceField(
#         choices=choice3,
#         label="Skills",
#         widget=forms.Select({'multiple':'true','class': 'form-control'})
#     )
#     password = forms.CharField(label="Password",widget=forms.PasswordInput({'placeholder':"*************",'class': 'form-control'}))



from django import forms
from django.utils.html import format_html
class ContactForm(forms.Form):
    fname = forms.CharField(
        max_length=100,
        label="Fullname",
        help_text="Please fill your full name (letters only).",
        min_length=5,
        required=True
    )

    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    price = forms.CharField(widget=forms.TextInput(attrs={'type': 'range', 'min': 100, 'max': 5000}))

    choice = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ]
    gender = forms.ChoiceField(choices=choice, widget=forms.RadioSelect, label="Gender")

    choice1 = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C')
    ]
    hobbie = forms.MultipleChoiceField(
        choices=choice1,
        widget=forms.CheckboxSelectMultiple,
        label="Hobbies"
    )

    choice2 = [
        ('', '--Select Country--'),
        ('IND', 'India'),
        ('PAK', 'Pakistan'),
        ('US', 'USA')
    ]
    country = forms.ChoiceField(choices=choice2, label="Country")

    choice3 = [
        ('P', 'PLANNING'),
        ('Q', 'QUITE'),
        ('R', 'RASOI')
    ]
    skills = forms.MultipleChoiceField(
        choices=choice3,
        label="Skills"
    )
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': '*************'})
    )

    # ✅ Apply Bootstrap classes automatically
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget

            # Text / select / password / color / range inputs
            if isinstance(widget, (forms.TextInput, forms.PasswordInput, forms.Select, forms.SelectMultiple)):
                widget.attrs.update({'class': 'form-control mb-3'})

            # Radio buttons & checkboxes
            # elif isinstance(widget, (forms.RadioSelect, forms.CheckboxSelectMultiple)):
            #     widget.attrs.update({'class': 'form-check-input'})

            # Range slider special class (Bootstrap 5)
            if widget.attrs.get('type') == 'range':
                widget.attrs['class'] = 'form-range mb-3'

            # Color picker special class
            if widget.attrs.get('type') == 'color':
                widget.attrs['class'] = 'form-control form-control-color mb-3'
    # def as_divs(self):
    #     html = ""
    #     for field in self:
    #         html += format_html(
    #             '<div class="mb-3">{}{}<div class="form-text">{}</div></div>',
    #             field.label_tag(attrs={'class': 'form-label'}),
    #             field,
    #             field.help_text or ""
    #         )
    #     print(html)
    #     return format_html(html)
    def as_divs(self):
        html = '<div class="row">'
        fields = list(self)

        # Loop through fields and place two per row
        for i, field in enumerate(fields):
            # Start new row every 2 fields
            if i % 2 == 0 and i != 0:
                html += '</div><div class="row">'

            html += format_html(
                '''
                <div class="col-md-6 mb-3">
                    <label class="form-label">{}</label>
                    {}
                    <div class="form-text">{}</div>
                </div>
                ''',
                field.label,
                field,
                field.help_text or ""
            )
        html += '</div>'
        return format_html(html)