# Generated by Django 4.0 on 2021-12-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('latte', '0004_rename_title_quest_todo_quest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='school',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='latte.school'),
        ),
    ]