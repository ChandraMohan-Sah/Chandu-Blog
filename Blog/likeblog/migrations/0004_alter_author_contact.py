# Generated by Django 4.0.1 on 2022-01-15 14:02

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('likeblog', '0003_address_alter_blog_content_alter_author_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
