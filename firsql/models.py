from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class User(models.Model):
    login = models.CharField(max_length=200)
    money_amount = models.IntegerField(default=0)
    card_number = models.CharField(max_length=16)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "users"

class User_data(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    pwd = models.CharField(max_length=200)