# apps/images/serializers.py
from rest_framework import serializers
from .models import Images


class ImageCreateSerializer(serializers.ModelSerializer):
    """Serializer para CREATE - aceita arquivos"""

    class Meta:
        model = Images
        fields = ['id', 'title', 'image']

    def create(self, validated_data):
        # O Django vai salvar automaticamente com o storage configurado
        return super().create(validated_data)


class ImageSerializer(serializers.ModelSerializer):
    """Serializer para READ - formata URLs"""
    image = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ['id', 'title', 'image']

    def get_image(self, obj):
        print(f"🔍 DEBUG obj.image: {repr(obj.image)}")

        if obj.ie_origem == 'PRF':
                if obj.image:
                    image_str = str(obj.image)

                    if image_str.startswith('https://'):
                        return image_str
                    elif image_str.startswith('image/upload/'):
                        return f"https://res.cloudinary.com/dcezopogd/{image_str}"
                    else:
                        clean_path = image_str.lstrip('/')
                        return f"https://res.cloudinary.com/dcezopogd/image/upload/{clean_path}"

        return None