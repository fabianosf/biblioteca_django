# Generated by Django 4.2.8 on 2023-12-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0002_alter_livros_options_alter_livros_co_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livros",
            name="data_cadastro",
            field=models.DateField(auto_now=True),
        ),
    ]
