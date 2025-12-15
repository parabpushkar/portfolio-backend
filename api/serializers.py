from rest_framework import serializers
from .models import Project
from .models import Contact

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'  

    def get_image(self, obj):
        # Try to return an absolute URL if request is available
        request = self.context.get('request')
        if obj.image:
            try:
                url = obj.image.url
            except ValueError:
                return None
            if request:
                return request.build_absolute_uri(url)
            return url
        return None
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
