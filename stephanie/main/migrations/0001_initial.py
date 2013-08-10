# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'main_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 10, 0, 0))),
        ))
        db.send_create_signal(u'main', ['Category'])

        # Adding model 'ArtGroup'
        db.create_table(u'main_artgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 10, 0, 0))),
        ))
        db.send_create_signal(u'main', ['ArtGroup'])

        # Adding model 'Artwork'
        db.create_table(u'main_artwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=65)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ArtGroup'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('commission', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('commission_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('size', self.gf('stephanie.main.models.CentimeterSizeField')(max_length=100, null=True, blank=True)),
            ('picture', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 10, 0, 0))),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 10, 0, 0))),
        ))
        db.send_create_signal(u'main', ['Artwork'])

        # Adding M2M table for field categories on 'Artwork'
        m2m_table_name = db.shorten_name(u'main_artwork_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artwork', models.ForeignKey(orm[u'main.artwork'], null=False)),
            ('category', models.ForeignKey(orm[u'main.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artwork_id', 'category_id'])

        # Adding model 'Contact'
        db.create_table(u'main_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 10, 0, 0))),
        ))
        db.send_create_signal(u'main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'main_category')

        # Deleting model 'ArtGroup'
        db.delete_table(u'main_artgroup')

        # Deleting model 'Artwork'
        db.delete_table(u'main_artwork')

        # Removing M2M table for field categories on 'Artwork'
        db.delete_table(db.shorten_name(u'main_artwork_categories'))

        # Deleting model 'Contact'
        db.delete_table(u'main_contact')


    models = {
        u'main.artgroup': {
            'Meta': {'object_name': 'ArtGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.artwork': {
            'Meta': {'object_name': 'Artwork'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'commission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commission_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.ArtGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'size': ('stephanie.main.models.CentimeterSizeField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '65'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'main.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['main']