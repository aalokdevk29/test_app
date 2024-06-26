# Generated by Django 4.2.7 on 2023-12-20 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.image'),
        ),
    ]
