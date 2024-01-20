from rest_framework import serializers
from .models import Listing, Images


class ImagesSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image too large")
        if value.images.width > 4096:
            raise serializers.ValidationError("Image dimensions too large")
        if value.images.height > 4096:
            raise serializers.ValidationError("Image dimensions too large")
        return value

    class Meta:
        model = Images
        fields = ["id", "listing", "images"]


class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    images = ImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000, use_url=False, allow_empty_file=False
        ),
        write_only=True,
    )

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.owner

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        listing = Listing.objects.create(**validated_data)
        for uploaded_image in uploaded_images:
            Images.objects.create(listing=listing, images=uploaded_image)
        return listing

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        if uploaded_images:
            listing_image_model_instance = [
                Images(listing=instance, images=image) for image in uploaded_images
            ]
            Images.objects.bulk_create(listing_image_model_instance)
        return super().update(instance, validated_data)

    class Meta:
        model = Listing
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "is_owner",
            "profile_id",
            "sale_type",
            "type",
            "description",
            "address_number",
            "address_street",
            "postcode",
            "city",
            "price",
            "surface",
            "levels",
            "bedrooms",
            "floor",
            "kitchens",
            "bathrooms",
            "living_rooms",
            "heating_system",
            "energy_class",
            "construction_year",
            "availability",
            "images",
            "uploaded_images",
        ]