from django.db import models

# Create your models here.

class users(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	phone=models.CharField(max_length=159);
	city=models.CharField(max_length=159);
	gender=models.CharField(max_length=159);
	age=models.CharField(max_length=159);


class q_a_dataset(models.Model):
    question = models.TextField();
    answer = models.TextField();
    subject = models.CharField(max_length=100);

class exam(models.Model):
    eid = models.CharField(max_length=159);
    name = models.CharField(max_length=159);
    email = models.CharField(max_length=159);
    subject = models.CharField(max_length=159);
    date_time = models.CharField(max_length=159);
    result = models.CharField(max_length=159);


class examdata(models.Model):
    eid = models.CharField(max_length=159);
    qid = models.CharField(max_length=159);
    question=models.TextField();
    faceexp = models.CharField(max_length=159);
    sc1 = models.CharField(max_length=159);  # face expression score
    answer = models.CharField(max_length=159);
    sc2_g = models.CharField(max_length=159);  # grammer score
    sc3_m = models.CharField(max_length=159);  # answer matching score
