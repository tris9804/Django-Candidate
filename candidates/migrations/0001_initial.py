# Generated by Django 2.1.7 on 2019-03-28 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('politics', models.TextField(verbose_name='政見')),
                ('photo', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='照片')),
                ('klass', models.CharField(max_length=20, verbose_name='班級')),
                ('count', models.IntegerField(default=0, verbose_name='得票數')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='投票時間')),
                ('is_valid', models.BooleanField(default=False, verbose_name='有效票')),
                ('tickets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_for', to='candidates.Candidate', verbose_name='得票數')),
                ('vote_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_to', to='candidates.Candidate', verbose_name='投票給')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='科系')),
            ],
        ),
        migrations.CreateModel(
            name='Votepool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='投票類別')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='Votepool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candidates.Votepool', verbose_name='參選類別'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candidates.Department', verbose_name='科系'),
        ),
    ]
