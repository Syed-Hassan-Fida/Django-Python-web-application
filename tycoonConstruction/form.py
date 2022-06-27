from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def chech_value(value):
    if value <= 0:
        raise ValidationError(
            _('can not be zero or negative...'),
            params={'value': value},
        )

class CostForm(forms.Form):
    length = forms.IntegerField(
        label="Length (fts)", validators=[chech_value])
    width = forms.IntegerField(
        label="width of wall (inchs)", validators=[chech_value])
    height = forms.IntegerField(
        label="height (fts)", validators=[chech_value])
    no_of_walls = forms.IntegerField(
        label="no_of_walls", validators=[chech_value])


class Deduction(forms.Form):
    length = forms.IntegerField(label="Length (fts)", validators=[chech_value])
    width = forms.IntegerField(
        label="width of wall (inchs)", validators=[chech_value])
    height = forms.IntegerField(label="height (fts)", validators=[chech_value])
    no_of_walls = forms.IntegerField(
        label="no_of_walls", validators=[chech_value])
    total_meter_wall = forms.FloatField(
        label="total_meter_wall (meter cube (m^3))", validators=[chech_value])


class LabourCost(forms.Form):
    length = forms.FloatField(
        label="Total Length (fts)", validators=[chech_value])
    width = forms.FloatField(label="Total Width (fts)",
                            validators=[chech_value])
    no_days = forms.IntegerField(label="No of Days", validators=[chech_value])


class PillarCollumn(forms.Form):
    c_length = forms.IntegerField(
        label="Length (inchs)", validators=[chech_value])
    c_width = forms.IntegerField(
        label="width of wall (inchs)", validators=[chech_value])
    c_height = forms.IntegerField(
        label="height (fts)", validators=[chech_value])
    c_no_of_walls = forms.IntegerField(
        label="no_of_walls", validators=[chech_value])


class RccBeam(forms.Form):
    b_length = forms.IntegerField(
        label="Length (fts)", validators=[chech_value])
    b_width = forms.IntegerField(
        label="width of wall (inchs)", validators=[chech_value])
    b_height = forms.IntegerField(
        label="height (inchs)", validators=[chech_value])
    b_no_of_walls = forms.IntegerField(
        label="no_of_walls", validators=[chech_value])


class RccSlap(forms.Form):
    s_length = forms.FloatField(label="Length (fts)", validators=[chech_value])
    s_width = forms.IntegerField(
        label="width of wall (fts)", validators=[chech_value])
    s_height = forms.IntegerField(
        label="height (inchs)", validators=[chech_value])
    s_no_of_walls = forms.IntegerField(
        label="no_of_walls", validators=[chech_value])


class Vtoc_req(forms.Form):
    name = forms.CharField(label="Vendor Name", required=True)
    v_email= forms.EmailField(label="Email", max_length=100)
    year_of_experience = forms.IntegerField(
    label="year_of_experience", required=True)
    projects_done = forms.IntegerField(label="projects_done", required=True)
    rating = forms.IntegerField(label="rating", required=True)
    description = forms.CharField(label="Description", required=True)
    image = forms.ImageField(label="Your Image", required=True)
