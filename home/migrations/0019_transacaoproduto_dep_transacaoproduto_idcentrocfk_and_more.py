# Generated by Django 4.0.3 on 2022-03-16 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_transacaoproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacaoproduto',
            name='dep',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacaoproduto',
            name='idCentroCFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.centrocusto'),
        ),
        migrations.AddField(
            model_name='transacaoproduto',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacaoproduto',
            name='umr',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transacaoproduto',
            name='idContaRazaoFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.contarazao'),
        ),
        migrations.AlterField(
            model_name='transacaoproduto',
            name='idProdutoFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.produto'),
        ),
        migrations.AlterField(
            model_name='transacaoproduto',
            name='idTipoMovimentoFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tipomovimento'),
        ),
    ]
