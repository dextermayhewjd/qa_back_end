from django.shortcuts import render
from django.views.decorators.cache import cache_control

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from myapp.models import Conversations
from .models import UserAnswer,UserFeedback,Participant
from myapp.serializers import ConversationSerializer
from rest_framework.decorators import api_view
import random

from django.http import JsonResponse
import uuid


class ConversationAPIView(APIView):
    
    def get(self, request):
        conversations = Conversations.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)


#get one conversation with all the questions related with it    
@api_view(['GET'])
def get_conversation_with_questions(request, conversation_id):
    conversation = get_object_or_404(Conversations, id=conversation_id)
    serializer = ConversationSerializer(conversation)
    return Response(serializer.data)



# need to define an api that could get 8 conversation 
@api_view(['GET'])
def get_more_conversation_with_questions(request):
    
    qualifiedConversations = []
    def select_conversations(num_questions, min_word_count, max_word_count):
        count = Conversations.objects.filter(word_num__gte=min_word_count, word_num__lte=max_word_count).count()

        for _ in range(num_questions):
            random_index = random.randint(0, count - 1)
            conversation = Conversations.objects.filter(word_num__gte=min_word_count, word_num__lte=max_word_count)[random_index]
            qualifiedConversations.append(conversation)
    
    # 选择符合单词数量范围的对话
    select_conversations(2, 2, 50)
    select_conversations(2, 50, 100)     
    
    def select_conversations_with_fre(num_questions, min_word_count, max_word_count):
        conversations = Conversations.objects.filter(word_num__gte=min_word_count, word_num__lte=max_word_count)
        
        # 根据 fre 字段进行排序
        sorted_conversations = conversations.order_by('fre')
        count = len(sorted_conversations)
        
        middle_index = count // 2
        
        first_part = num_questions //2
        second_part = num_questions - first_part
        for _ in range(second_part):   
            random_index_up = random.randint(middle_index +1,count-1 )
            qualifiedConversations.append(sorted_conversations[random_index_up])
        for _ in range(first_part):
            random_index_down = random.randint(0, middle_index )
            qualifiedConversations.append(sorted_conversations[random_index_down])
    select_conversations_with_fre(2, 100, 200)
    select_conversations_with_fre(2, 200, 300) 
    select_conversations_with_fre(2, 200, 424) 
    serializer = ConversationSerializer(qualifiedConversations,many=True)    
    return Response(serializer.data)
    


# # post user answer for one question with its user_id to the database
@api_view(['POST'])
def post_user_answer_for_question(request):
    # 获取POST数据
    user_id = request.data.get('userid')
    questionId = request.data.get('questionId')
    answer = request.data.get('answer')
    real_answer = request.data.get('real_answer')
    conversation_id = request.data.get('conversation_id')
    
    user_answer = UserAnswer.objects.create(
        user_id=user_id,
        question_id=questionId,
        answer=answer,
        real_answer=real_answer,
        conversation_id=conversation_id
    )
    
    return Response({"message": "post_user_answer_for_question success"}, status=200)

    

# # post user feedback with its user_id to the database
@api_view(['POST'])
def post_user_feedback_for_one_conversation(request):
    # 获取POST数据
    user_id = request.data.get('user_id')
    conversation_id = request.data.get('conversation_id')
    feedback1 = request.data.get('feedback1')
    feedback2 = request.data.get('feedback2')
    
    # 创建 UserFeedback 对象并保存到数据库
    user_feedback = UserFeedback.objects.create(
        user_id=user_id,
        conversation_id=conversation_id,
        feedback1=feedback1,
        feedback2=feedback2
    )
    
    return Response({"message": "post_user_feedback_for_one_conversation"}, status=200)

@api_view(['POST'])
def post_user_background(request):
    # 获取POST数据
    user_id = request.data.get('user_id')
    background1 = request.data.get('background1')
    background2 = request.data.get('background2')
    background3 = request.data.get('background3')
    background4 = request.data.get('background4')
    background5 = request.data.get('background5')
    email       = request.data.get('email')
    elapsedSeconds = request.data.get('elapsedSeconds')
    totalPlayTime = request.data.get('totalPlayTime')
    isSerious     = request.data.get('isSerious')
    # 创建 UserFeedback 对象并保存到数据库
    participant = Participant.objects.create(
        user_id=user_id,
        background1=background1,
        background2=background2,
        background3=background3,
        background4=background4,
        background5=background5,
        email_address = email,
        elapsed_seconds = elapsedSeconds,
        total_play_time = totalPlayTime,
        is_serious     = isSerious
        )
    
    return Response({"message": "post_user_feedback_for_one_conversation"}, status=200)




@cache_control(no_cache=True, must_revalidate=True)
@api_view(['GET'])
def generate_unique_id(request):
    unique_id = str(uuid.uuid4())  # Generate unique ID
    return JsonResponse({'unique_id': unique_id})