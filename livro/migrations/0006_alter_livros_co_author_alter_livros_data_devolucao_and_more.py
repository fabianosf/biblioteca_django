# Generated by Django 4.2.8 on 2023-12-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0005_alter_livros_data_cadastro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livros",
            name="co_author",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="data_devolucao",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="data_emprestimo",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="nome_emprestado",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="tempo_duracao",
            field=models.DateField(blank=True, null=True),
        ),
    ]
