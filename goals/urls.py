from django.urls import path

from goals.views.goal_category import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryDetailView
from goals.views.goals import GoalListView, GoalCreateView, GoalDetailView
from goals.views.goal_comment import GoalCommentListView, GoalCommentCreateView, GoalCommentDetailView


urlpatterns = [
    # Category urls
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='category_list'),
    path('goal_category/<pk>', GoalCategoryDetailView.as_view(), name='category_detail'),
    # Goal urls
    path('goal/create', GoalCreateView.as_view(), name='create_goal'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<pk>', GoalDetailView.as_view(), name='goal_detail'),
    # Comment urls
    path('goal_comment/create', GoalCommentCreateView.as_view(), name='create_comment'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='comment_list'),
    path('goal_comment/<pk>', GoalCommentDetailView.as_view(), name='comment_detail'),
]

