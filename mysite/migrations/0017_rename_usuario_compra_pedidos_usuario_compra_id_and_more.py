# Generated by Django 4.1.8 on 2023-10-11 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_rename_vendedores_pedidos_ids_pedidos_vendedor_pedido_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='usuario_compra',
            new_name='usuario_compra_id',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='vendedor_pedido_id',
            field=models.ManyToManyField(related_name='vendedores_pedidos', through='mysite.VendedoresPedidosConexion', to='mysite.vendedores'),
        ),
    ]
