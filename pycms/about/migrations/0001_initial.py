# Generated by Django 2.2.3 on 2019-07-17 08:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', models.CharField(blank=True, max_length=100, null=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateField(verbose_name='Selected Date')),
                ('cover', models.TextField(blank=True, max_length=100, null=True)),
                ('left', models.CharField(blank=True, max_length=100, null=True)),
                ('right', models.CharField(blank=True, max_length=100, null=True)),
                ('main', models.CharField(blank=True, help_text='Some very useful text', max_length=100, null=True)),
                ('selection', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(label='Some cool heading')), ('structblock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('number', wagtail.core.blocks.IntegerBlock()), ('Choice', wagtail.core.blocks.ChoiceBlock(choices=[('tea', 'Tea'), ('coffee', 'Coffee')], icon='cup')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('url', wagtail.core.blocks.URLBlock()), ('date', wagtail.core.blocks.DateBlock()), ('time', wagtail.core.blocks.TimeBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True)),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='about.AboutPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
