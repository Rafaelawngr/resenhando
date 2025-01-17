# Generated by Django 4.0.6 on 2024-04-08 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=45)),
                ('autor', models.CharField(max_length=45)),
                ('ano', models.IntegerField()),
                ('genero', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Resenhas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data', models.DateField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resenhando.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resenhando.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacao', models.IntegerField()),
                ('comentario', models.TextField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resenhando.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resenhando.usuarios')),
            ],
        ),
    ]
