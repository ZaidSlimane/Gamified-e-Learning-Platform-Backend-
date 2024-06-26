# Generated by Django 5.0.3 on 2024-04-14 23:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('courseSummary', models.TextField(max_length=100)),
                ('recompense', models.IntegerField()),
                ('terms', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('game_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('grade', models.CharField(max_length=50)),
                ('institute', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterName', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.student')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.chatroom')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField()),
                ('stars', models.IntegerField()),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.enrollments')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_content', models.TextField()),
                ('question_answer', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.chapter')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.teacher'),
        ),
        migrations.CreateModel(
            name='Chat_participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElearningPlatform.teacher')),
            ],
        ),
    ]
