from rest_framework import serializers
from restaurants.models import Restaurant, User, Item



class RestaurantUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]



class RestaurantItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
        'name',
        'description',
        'price',
        ]



class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    class Meta:

        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'detail',
            'update',
            'delete',
            ]

class RestaurantDetailSerializer(serializers.ModelSerializer):

    owner = RestaurantUserSerializer()
    items = serializers.SerializerMethodField()

    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'update',
            'delete',
            'owner',
            'items',
            ]

    def get_items(self, obj):
        items = Item.objects.filter(restaurant=obj)
        return RestaurantItemSerializer(items, many=True).data


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]

