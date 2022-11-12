from django.forms import ModelForm
from lugares.models import Barrio
from lugares.models import EPS


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



class EPSForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = EPS
        exclude = ('estado',)

class EPSUpdateForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = EPS
        exclude = ('estado',)
