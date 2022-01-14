# Generated by Django 4.0 on 2022-01-02 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('latte', '0006_alter_quest_category_alter_quest_school'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='college',
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='latte.school'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'I Prefer Not To Say')], max_length=1),
        ),
    ]
