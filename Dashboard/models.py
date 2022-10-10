from django.db import models

DB_TYPE = (
    ('oracle','Oracle'),
    ('sql', 'SQL'),
)

INSERT_TYPE = (
    ('single','Single'),
    ('multiple', 'Multiple'),
)


class Blog(models.Model):
    title= models.TextField()
    content = models.TextField(null=True,blank=True)

class Congif(models.Model):
    env= models.TextField();
    env_name = models.TextField(null=True);
    db_type = models.CharField(max_length=6, choices=DB_TYPE, default='oracle');
    user_name= models.TextField();
    password = models.TextField();
    dsn=models.TextField();
    port=models.TextField();

class Query_set(models.Model):
    table_name= models.TextField();
    db_type=models.CharField(max_length=6, choices=DB_TYPE, default='oracle');
    insert_type=models.CharField(max_length=10, choices=INSERT_TYPE, default='single');
    query=models.TextField();


# class test(models.Model):
#     color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green');
