# Generated by Django 5.0.2 on 2024-02-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_saloon', '0012_rename_hotel_main_img_hotel_upload_image_here'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]