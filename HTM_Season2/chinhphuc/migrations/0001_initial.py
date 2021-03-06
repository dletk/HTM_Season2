# Generated by Django 2.2.3 on 2019-08-28 18:00

import chinhphuc.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChinhPhucQuestion',
            fields=[
                ('questionID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Câu hỏi số')),
                ('questionText', models.TextField(blank=True, verbose_name='Nội dung câu hỏi')),
                ('answer', models.CharField(max_length=256, verbose_name='Đáp án')),
                ('file', models.FileField(blank=True, upload_to=chinhphuc.models.questionDirectoryPath, verbose_name='File đính kèm')),
                ('fileType', models.CharField(blank=True, choices=[('sound', 'Âm thanh'), ('video', 'Video'), ('image', 'Hình ảnh')], max_length=10, verbose_name='Loại file')),
                ('difficulty', models.CharField(blank=True, choices=[('easy', 'Dễ'), ('medium', 'Trung bình'), ('hard', 'Khó')], max_length=10, verbose_name='Loại file')),
            ],
        ),
        migrations.CreateModel(
            name='ChinhPhucAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinhphuc.ChinhPhucQuestion')),
                ('thisinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
