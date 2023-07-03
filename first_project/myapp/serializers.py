from rest_framework import serializers
from .models import Conversations, Questions, ConversationAudioUrl

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'



class ConversationAudioURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationAudioUrl
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    conversation_audio_url = ConversationAudioURLSerializer(many=True)
    class Meta:
        model = Conversations
        fields = ['id', 'conversation','fre', 'fkgl', 'word_num', 'questions_num', 'unique_word_num', 'questions', 'conversation_audio_url'] 
        # the name here have to be related with the things define in the model 
        # in the related name