from django.forms import ModelForm
from lugares.models import Barrio
class BarrioForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Barrio
        exclude = ('estado',)

class BarrioUpdateForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Barrio
        exclude = ('estado',)
