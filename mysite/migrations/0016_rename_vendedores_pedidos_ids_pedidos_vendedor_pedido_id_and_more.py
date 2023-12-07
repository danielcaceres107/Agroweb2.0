# Generated by Django 4.1.8 on 2023-10-11 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_pedidos_vendedorespedidosconexion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='vendedores_pedidos_ids',
            new_name='vendedor_pedido_id',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='productos_pedidos',
            field=models.ManyToManyField(related_name='productos_pedidos', through='mysite.ProductosPedidosConexion', to='mysite.products'),
        ),
        migrations.AlterField(
            model_name='vendedorespedidosconexion',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_ids', to='mysite.pedidos'),
        ),
        migrations.AlterField(
            model_name='vendedorespedidosconexion',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_ids', to='mysite.vendedores'),
        ),
    ]
