# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ArtGroup.slug'
        db.alter_column(u'main_artgroup', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=65))
        # Adding unique constraint on 'ArtGroup', fields ['slug']
        db.create_unique(u'main_artgroup', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'ArtGroup', fields ['slug']
        db.delete_unique(u'main_artgroup', ['slug'])


        # Changing field 'ArtGroup.slug'
        db.alter_column(u'main_artgroup', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=65, null=True))

    models = {
        u'main.artgroup': {
            'Meta': {'object_name': 'ArtGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 10, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '65'})
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