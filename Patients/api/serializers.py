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
            'country'
            'age',
            'address'
        ]
    
    def get_age(self, obj):
        return obj.get_age()

    def get_address(self, obj):
        return obj.get_address() 