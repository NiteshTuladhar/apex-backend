from rest_framework import serializers

from courses.models import Course, CourseCategory


class CourseCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating courses."""

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "link",
            "password",
            "status",
            "price",
            "category",
        )


class CourseRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving courses."""

    class Meta:

        model = Course
        fields = (
            "id",
            "name",
            "link",
            "password",
            "status",
            "price",
        )


class CourseUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating courses."""

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "link",
            "password",
            "status",
            "price",
        )


class CourseDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting courses."""

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "link",
            "password",
            "status",
            "price",
        )


class CourseCategoryCreateSerialilzer(serializers.ModelSerializer):
    """Serializer for creating course categories."""

    class Meta:
        model = CourseCategory
        fields = (
            "id",
            "name",
            "description",
        )


class CourseCategoryRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving course categories."""

    class Meta:
        model = CourseCategory
        fields = (
            "id",
            "name",
            "description",
        )


class CourseCategoryUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating course categories."""

    class Meta:
        model = CourseCategory
        fields = (
            "id",
            "name",
            "description",
        )


class CourseCategoryDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting course categories."""

    class Meta:
        model = CourseCategory
        fields = (
            "id",
            "name",
            "description",
        )