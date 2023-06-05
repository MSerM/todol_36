
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from core.serializers import UserSerializer
from goals.models import GoalCategory, Goal, GoalComment


class GoalCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user', 'is_deleted')


class GoalUserSerializer(GoalCategorySerializer):
    user = UserSerializer(read_only=True)


class GoalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user')

    def validate_category(self, value: GoalCategory) -> GoalCategory:
        if value.is_deleted:
            raise ValidationError("Category isn't found")
        if self.context['request'].user.id != value.user_id:
            raise PermissionDenied
        return value


class GoalWithUserSerializer(GoalSerializer):
    user = UserSerializer(read_only=True)


class GoalCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user')

    def validate_goal(self, value: Goal) -> Goal:
        if value.status == Goal.Status.archived:
            raise ValidationError("Goal isn't found")
        if self.context['request'].user.id != value.user_id:
            raise PermissionDenied
        return value


class GoalCommentWithUser(GoalCommentSerializer):
    user = UserSerializer(read_only=True)
    goal = serializers.PrimaryKeyRelatedField(read_only=True)


