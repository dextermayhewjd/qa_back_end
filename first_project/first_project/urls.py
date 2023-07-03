"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp.views import ConversationAPIView, get_conversation_with_questions,get_more_conversation_with_questions,post_user_feedback_for_one_conversation,generate_unique_id,post_user_answer_for_question,post_user_background

urlpatterns = [
    # 其他URL模式
    path('api/conversations/', ConversationAPIView.as_view(), name='conversation_list'),
    path('api/conversations/<int:conversation_id>/', get_conversation_with_questions, name='conversation_detail'),
    path('api/conversations/eighitConversations/',get_more_conversation_with_questions,name='more_conversation_detail'),
    path('api/user_answer_for_question/',post_user_answer_for_question,name='post_user_answer'),
    path('api/user_feedback/',post_user_feedback_for_one_conversation,name='userfeedback'),
    path('api/user_background/',post_user_background,name='userbackground'),
    path('generate_unique_id/', generate_unique_id, name='generate_unique_id'),
]
