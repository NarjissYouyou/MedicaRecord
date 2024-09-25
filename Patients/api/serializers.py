#For converting to JSON compatible data
from rest_framework import serializers 
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'phone',
            'email',
            'street',
            'city',
            'state',
            'zip_code',
            'country',
            'age', 
            'address',
            'date_creation'
        ]