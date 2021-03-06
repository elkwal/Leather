# Generated by Django 2.0.9 on 2018-11-30 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leather', '0003_business_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('post', models.TextField(max_length=100)),
                ('postpic', models.ImageField(default=True, upload_to='picture/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('bio', models.TextField(blank=True, max_length=100)),
                ('profilepic', models.ImageField(default=True, upload_to='picture/')),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(blank=True, max_length=15)),
                ('townpin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('bio', models.CharField(default='', max_length=40)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administrate', to='Leather.User_profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='Leather.Town'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Leather.User_profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='town', to='Leather.Town'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leather.User_profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Leather.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leather.User_profile'),
        ),
    ]
