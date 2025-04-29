from rest_framework import serializers
from .models import ContactForm

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'phone', 'email', 'message']

    # Custom validation if needed
    def validate(self, data):
        # Example: Custom validation on phone number length
        if len(data['phone']) < 10:
            raise serializers.ValidationError("Phone number should be at least 10 digits.")
        return data
