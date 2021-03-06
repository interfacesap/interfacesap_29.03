# Generated by Django 4.0.1 on 2022-03-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_produto_partnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('idProdutoFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='home.produto')),
            ],
        ),
    ]
