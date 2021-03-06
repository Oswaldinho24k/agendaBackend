# Generated by Django 2.0.1 on 2018-02-06 21:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_auto_20180124_1901'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meeting_date', models.DateTimeField(db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('participants', models.ManyToManyField(to='accounts.Profile')),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete='CASCADE', related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
