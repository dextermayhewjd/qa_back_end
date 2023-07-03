# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)





class Conversations(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversation = models.TextField(blank=True, null=True)
    fre = models.FloatField(blank=True, null=True)
    fkgl = models.FloatField(blank=True, null=True)
    word_num = models.IntegerField(blank=True, null=True)
    questions_num = models.IntegerField(blank=True, null=True)
    unique_word_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversations'


class ConversationAudioUrl(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name='conversation_audio_url')
    file_name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversation_audio_url'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    answer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class UserAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Questions, models.DO_NOTHING, blank=True, null=True)
    answer = models.CharField(max_length=255, blank=True, null=True)
    real_answer = models.CharField(max_length=255, blank=True, null=True)
    conversation = models.ForeignKey(Conversations, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user_answer'


class UserFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversations, models.DO_NOTHING, blank=True, null=True)
    feedback1 = models.CharField(max_length=255, blank=True, null=True)
    feedback2 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'user_feedback'

class Participant(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    background1 = models.IntegerField()
    background2 = models.IntegerField()
    background3 = models.IntegerField()
    background4 = models.IntegerField()
    background5 = models.IntegerField()
    email_address = models.CharField(max_length=255)
    elapsed_seconds = models.IntegerField()
    total_play_time = models.IntegerField()
    is_serious = models.BooleanField()
    
    class Meta:
        managed = False
        db_table = 'participant'