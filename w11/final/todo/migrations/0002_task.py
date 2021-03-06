# Generated by Django 2.2.1 on 2019-05-27 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('due_on', models.DateTimeField()),
                ('status', models.CharField(choices=[('D', 'DONE'), ('UD', 'UNDONE')], max_length=50)),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.TaskList')),
            ],
        ),
    ]
