# Generated by Django 4.0 on 2022-01-02 09:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('latte', '0006_alter_quest_category_alter_quest_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_quest', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='latte.category')),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='latte.school')),
            ],
        ),
        migrations.DeleteModel(
            name='Quest',
        ),
    ]
