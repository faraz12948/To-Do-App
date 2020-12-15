from rest_framwork import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerialize):
    class Meta:
        model=Todo
        fields= '__all__'
       
