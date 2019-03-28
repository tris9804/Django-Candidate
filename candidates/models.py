from django.db import models


class Department(models.Model):
    name = models.CharField('科系', max_length=20)

    def __str__(self):
        return self.name

class Votepool(models.Model):
    name = models.CharField('投票類別', max_length=20)

    def __str__(self):
        return self.name





class Candidate(models.Model):
    name = models.CharField('姓名', max_length=20)
    Votepool = models.ForeignKey(Votepool, models.PROTECT, verbose_name='參選類別')
    politics = models.TextField('政見')
    photo = models.ImageField('照片', upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    department = models.ForeignKey(Department, models.PROTECT, verbose_name='科系')
    klass = models.CharField('班級', max_length=20)

    def __str__(self):
        return self.name


class Choice(models.Model):
    vote_to = models.ForeignKey(Candidate, models.CASCADE, verbose_name='投票給', related_name='vote_to')
    email = models.EmailField('Email', unique=True)
    create_at = models.DateTimeField('投票時間', auto_now_add=True)
    is_valid = models.BooleanField('有效票', default=True)

    def __str__(self):
        return 'vote to {}'.format(self.vote_to)



