# Generated by Django 3.0.3 on 2020-03-09 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification', '0001_initial'),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet'),
        ),
    ]