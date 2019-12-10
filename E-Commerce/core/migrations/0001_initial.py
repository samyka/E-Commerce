# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import E-Commerce.core.models
import filer.fields.image
import filer.fields.file
import parler.models
import E-Commerce.core.models._attributes
import django.db.models.deletion
import E-Commerce.core.modules.interface
from decimal import Decimal
import E-Commerce.core.fields
import E-Commerce.core.models._shipments
import E-Commerce.utils.properties
from django.conf import settings
import django_countries.fields
import mptt.fields
import E-Commerce.core.pricing
import E-Commerce.core.utils.name_mixin
import E-Commerce.utils.analog
import E-Commerce.core.taxing
import timezone_field.fields
import E-Commerce.core.models._base
import E-Commerce.core.models._shops
import jsonfield.fields
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=False, editable=False, blank=False, max_length=64, unique=True)),
                ('searchable', models.BooleanField(default=True, verbose_name='searchable')),
                ('type', enumfields.fields.EnumIntegerField(default=20, verbose_name='type', enum=E-Commerce.core.models.AttributeType)),
                ('visibility_mode', enumfields.fields.EnumIntegerField(default=1, verbose_name='visibility mode', enum=E-Commerce.core.models.AttributeVisibility)),
            ],
            options={
                'verbose_name': 'attribute',
                'verbose_name_plural': 'attributes',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AttributeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.Attribute')),
            ],
            options={
                'db_table': 'E-Commerce_attribute_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'attribute Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('status', enumfields.fields.EnumIntegerField(default=0, enum=E-Commerce.core.models.CategoryStatus, verbose_name='status', db_index=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('visibility', enumfields.fields.EnumIntegerField(default=1, enum=E-Commerce.core.models.CategoryVisibility, verbose_name='visibility limitations', db_index=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='image', to='filer.Image')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', null=True, blank=True, verbose_name='parent category', to='E-Commerce.Category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('tree_id', 'lft'),
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(max_length=64, blank=True, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, verbose_name='extra data', null=True)),
                ('target', models.ForeignKey(related_name='log_entries', to='E-Commerce.Category', verbose_name='target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('slug', models.SlugField(blank=True, verbose_name='slug', null=True)),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.Category')),
            ],
            options={
                'db_table': 'E-Commerce_category_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'category Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ConfigurationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='key')),
                ('value', jsonfield.fields.JSONField(verbose_name='value')),
            ],
            options={
                'verbose_name': 'configuration item',
                'verbose_name_plural': 'configuration items',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active', db_index=True)),
                ('language', E-Commerce.core.fields.LanguageField(max_length=10, blank=True, verbose_name='language', choices=[('aa', 'aa'), ('ab', 'ab'), ('ace', 'ace'), ('ach', 'ach'), ('ada', 'ada'), ('ady', 'ady'), ('ae', 'ae'), ('aeb', 'aeb'), ('af', 'af'), ('afh', 'afh'), ('agq', 'agq'), ('ain', 'ain'), ('ak', 'ak'), ('akk', 'akk'), ('akz', 'akz'), ('ale', 'ale'), ('aln', 'aln'), ('alt', 'alt'), ('am', 'am'), ('an', 'an'), ('ang', 'ang'), ('anp', 'anp'), ('ar', 'ar'), ('ar_001', 'ar_001'), ('arc', 'arc'), ('arn', 'arn'), ('aro', 'aro'), ('arp', 'arp'), ('arq', 'arq'), ('arw', 'arw'), ('ary', 'ary'), ('arz', 'arz'), ('as', 'as'), ('asa', 'asa'), ('ase', 'ase'), ('ast', 'ast'), ('av', 'av'), ('avk', 'avk'), ('awa', 'awa'), ('ay', 'ay'), ('az', 'az'), ('ba', 'ba'), ('bal', 'bal'), ('ban', 'ban'), ('bar', 'bar'), ('bas', 'bas'), ('bax', 'bax'), ('bbc', 'bbc'), ('bbj', 'bbj'), ('be', 'be'), ('bej', 'bej'), ('bem', 'bem'), ('bew', 'bew'), ('bez', 'bez'), ('bfd', 'bfd'), ('bfq', 'bfq'), ('bg', 'bg'), ('bgn', 'bgn'), ('bho', 'bho'), ('bi', 'bi'), ('bik', 'bik'), ('bin', 'bin'), ('bjn', 'bjn'), ('bkm', 'bkm'), ('bla', 'bla'), ('bm', 'bm'), ('bn', 'bn'), ('bo', 'bo'), ('bpy', 'bpy'), ('bqi', 'bqi'), ('br', 'br'), ('bra', 'bra'), ('brh', 'brh'), ('brx', 'brx'), ('bs', 'bs'), ('bss', 'bss'), ('bua', 'bua'), ('bug', 'bug'), ('bum', 'bum'), ('byn', 'byn'), ('byv', 'byv'), ('ca', 'ca'), ('cad', 'cad'), ('car', 'car'), ('cay', 'cay'), ('cch', 'cch'), ('ce', 'ce'), ('ceb', 'ceb'), ('cgg', 'cgg'), ('ch', 'ch'), ('chb', 'chb'), ('chg', 'chg'), ('chk', 'chk'), ('chm', 'chm'), ('chn', 'chn'), ('cho', 'cho'), ('chp', 'chp'), ('chr', 'chr'), ('chy', 'chy'), ('ckb', 'ckb'), ('co', 'co'), ('cop', 'cop'), ('cps', 'cps'), ('cr', 'cr'), ('crh', 'crh'), ('cs', 'cs'), ('csb', 'csb'), ('cu', 'cu'), ('cv', 'cv'), ('cy', 'cy'), ('da', 'da'), ('dak', 'dak'), ('dar', 'dar'), ('dav', 'dav'), ('de', 'de'), ('de_AT', 'de_AT'), ('de_CH', 'de_CH'), ('del', 'del'), ('den', 'den'), ('dgr', 'dgr'), ('din', 'din'), ('dje', 'dje'), ('doi', 'doi'), ('dsb', 'dsb'), ('dtp', 'dtp'), ('dua', 'dua'), ('dum', 'dum'), ('dv', 'dv'), ('dyo', 'dyo'), ('dyu', 'dyu'), ('dz', 'dz'), ('dzg', 'dzg'), ('ebu', 'ebu'), ('ee', 'ee'), ('efi', 'efi'), ('egl', 'egl'), ('egy', 'egy'), ('eka', 'eka'), ('el', 'el'), ('elx', 'elx'), ('en', 'en'), ('en_AU', 'en_AU'), ('en_CA', 'en_CA'), ('en_GB', 'en_GB'), ('en_US', 'en_US'), ('enm', 'enm'), ('eo', 'eo'), ('es', 'es'), ('es_419', 'es_419'), ('es_ES', 'es_ES'), ('es_MX', 'es_MX'), ('esu', 'esu'), ('et', 'et'), ('eu', 'eu'), ('ewo', 'ewo'), ('ext', 'ext'), ('fa', 'fa'), ('fa_AF', 'fa_AF'), ('fan', 'fan'), ('fat', 'fat'), ('ff', 'ff'), ('fi', 'fi'), ('fil', 'fil'), ('fit', 'fit'), ('fj', 'fj'), ('fo', 'fo'), ('fon', 'fon'), ('fr', 'fr'), ('fr_CA', 'fr_CA'), ('fr_CH', 'fr_CH'), ('frc', 'frc'), ('frm', 'frm'), ('fro', 'fro'), ('frp', 'frp'), ('frr', 'frr'), ('frs', 'frs'), ('fur', 'fur'), ('fy', 'fy'), ('ga', 'ga'), ('gaa', 'gaa'), ('gag', 'gag'), ('gan', 'gan'), ('gay', 'gay'), ('gba', 'gba'), ('gbz', 'gbz'), ('gd', 'gd'), ('gez', 'gez'), ('gil', 'gil'), ('gl', 'gl'), ('glk', 'glk'), ('gmh', 'gmh'), ('gn', 'gn'), ('goh', 'goh'), ('gom', 'gom'), ('gon', 'gon'), ('gor', 'gor'), ('got', 'got'), ('grb', 'grb'), ('grc', 'grc'), ('gsw', 'gsw'), ('gu', 'gu'), ('guc', 'guc'), ('gur', 'gur'), ('guz', 'guz'), ('gv', 'gv'), ('gwi', 'gwi'), ('ha', 'ha'), ('hai', 'hai'), ('hak', 'hak'), ('haw', 'haw'), ('he', 'he'), ('hi', 'hi'), ('hif', 'hif'), ('hil', 'hil'), ('hit', 'hit'), ('hmn', 'hmn'), ('ho', 'ho'), ('hr', 'hr'), ('hsb', 'hsb'), ('hsn', 'hsn'), ('ht', 'ht'), ('hu', 'hu'), ('hup', 'hup'), ('hy', 'hy'), ('hz', 'hz'), ('ia', 'ia'), ('iba', 'iba'), ('ibb', 'ibb'), ('id', 'id'), ('ie', 'ie'), ('ig', 'ig'), ('ii', 'ii'), ('ik', 'ik'), ('ilo', 'ilo'), ('inh', 'inh'), ('io', 'io'), ('is', 'is'), ('it', 'it'), ('iu', 'iu'), ('izh', 'izh'), ('ja', 'ja'), ('jam', 'jam'), ('jbo', 'jbo'), ('jgo', 'jgo'), ('jmc', 'jmc'), ('jpr', 'jpr'), ('jrb', 'jrb'), ('jut', 'jut'), ('jv', 'jv'), ('ka', 'ka'), ('kaa', 'kaa'), ('kab', 'kab'), ('kac', 'kac'), ('kaj', 'kaj'), ('kam', 'kam'), ('kaw', 'kaw'), ('kbd', 'kbd'), ('kbl', 'kbl'), ('kcg', 'kcg'), ('kde', 'kde'), ('kea', 'kea'), ('ken', 'ken'), ('kfo', 'kfo'), ('kg', 'kg'), ('kgp', 'kgp'), ('kha', 'kha'), ('kho', 'kho'), ('khq', 'khq'), ('khw', 'khw'), ('ki', 'ki'), ('kiu', 'kiu'), ('kj', 'kj'), ('kk', 'kk'), ('kkj', 'kkj'), ('kl', 'kl'), ('kln', 'kln'), ('km', 'km'), ('kmb', 'kmb'), ('kn', 'kn'), ('ko', 'ko'), ('koi', 'koi'), ('kok', 'kok'), ('kos', 'kos'), ('kpe', 'kpe'), ('kr', 'kr'), ('krc', 'krc'), ('kri', 'kri'), ('krj', 'krj'), ('krl', 'krl'), ('kru', 'kru'), ('ks', 'ks'), ('ksb', 'ksb'), ('ksf', 'ksf'), ('ksh', 'ksh'), ('ku', 'ku'), ('kum', 'kum'), ('kut', 'kut'), ('kv', 'kv'), ('kw', 'kw'), ('ky', 'ky'), ('la', 'la'), ('lad', 'lad'), ('lag', 'lag'), ('lah', 'lah'), ('lam', 'lam'), ('lb', 'lb'), ('lez', 'lez'), ('lfn', 'lfn'), ('lg', 'lg'), ('li', 'li'), ('lij', 'lij'), ('liv', 'liv'), ('lkt', 'lkt'), ('lmo', 'lmo'), ('ln', 'ln'), ('lo', 'lo'), ('lol', 'lol'), ('loz', 'loz'), ('lrc', 'lrc'), ('lt', 'lt'), ('ltg', 'ltg'), ('lu', 'lu'), ('lua', 'lua'), ('lui', 'lui'), ('lun', 'lun'), ('luo', 'luo'), ('lus', 'lus'), ('luy', 'luy'), ('lv', 'lv'), ('lzh', 'lzh'), ('lzz', 'lzz'), ('mad', 'mad'), ('maf', 'maf'), ('mag', 'mag'), ('mai', 'mai'), ('mak', 'mak'), ('man', 'man'), ('mas', 'mas'), ('mde', 'mde'), ('mdf', 'mdf'), ('mdr', 'mdr'), ('men', 'men'), ('mer', 'mer'), ('mfe', 'mfe'), ('mg', 'mg'), ('mga', 'mga'), ('mgh', 'mgh'), ('mgo', 'mgo'), ('mh', 'mh'), ('mi', 'mi'), ('mic', 'mic'), ('min', 'min'), ('mk', 'mk'), ('ml', 'ml'), ('mn', 'mn'), ('mnc', 'mnc'), ('mni', 'mni'), ('moh', 'moh'), ('mos', 'mos'), ('mr', 'mr'), ('mrj', 'mrj'), ('ms', 'ms'), ('mt', 'mt'), ('mua', 'mua'), ('mul', 'mul'), ('mus', 'mus'), ('mwl', 'mwl'), ('mwr', 'mwr'), ('mwv', 'mwv'), ('my', 'my'), ('mye', 'mye'), ('myv', 'myv'), ('mzn', 'mzn'), ('na', 'na'), ('nan', 'nan'), ('nap', 'nap'), ('naq', 'naq'), ('nb', 'nb'), ('nd', 'nd'), ('nds', 'nds'), ('nds_NL', 'nds_NL'), ('ne', 'ne'), ('new', 'new'), ('ng', 'ng'), ('nia', 'nia'), ('niu', 'niu'), ('njo', 'njo'), ('nl', 'nl'), ('nl_BE', 'nl_BE'), ('nmg', 'nmg'), ('nn', 'nn'), ('nnh', 'nnh'), ('no', 'no'), ('nog', 'nog'), ('non', 'non'), ('nov', 'nov'), ('nqo', 'nqo'), ('nr', 'nr'), ('nso', 'nso'), ('nus', 'nus'), ('nv', 'nv'), ('nwc', 'nwc'), ('ny', 'ny'), ('nym', 'nym'), ('nyn', 'nyn'), ('nyo', 'nyo'), ('nzi', 'nzi'), ('oc', 'oc'), ('oj', 'oj'), ('om', 'om'), ('or', 'or'), ('os', 'os'), ('osa', 'osa'), ('ota', 'ota'), ('pa', 'pa'), ('pag', 'pag'), ('pal', 'pal'), ('pam', 'pam'), ('pap', 'pap'), ('pau', 'pau'), ('pcd', 'pcd'), ('pdc', 'pdc'), ('pdt', 'pdt'), ('peo', 'peo'), ('pfl', 'pfl'), ('phn', 'phn'), ('pi', 'pi'), ('pl', 'pl'), ('pms', 'pms'), ('pnt', 'pnt'), ('pon', 'pon'), ('prg', 'prg'), ('pro', 'pro'), ('ps', 'ps'), ('pt', 'pt'), ('pt_BR', 'pt_BR'), ('pt_PT', 'pt_PT'), ('qu', 'qu'), ('quc', 'quc'), ('qug', 'qug'), ('raj', 'raj'), ('rap', 'rap'), ('rar', 'rar'), ('rgn', 'rgn'), ('rif', 'rif'), ('rm', 'rm'), ('rn', 'rn'), ('ro', 'ro'), ('ro_MD', 'ro_MD'), ('rof', 'rof'), ('rom', 'rom'), ('root', 'root'), ('rtm', 'rtm'), ('ru', 'ru'), ('rue', 'rue'), ('rug', 'rug'), ('rup', 'rup'), ('rw', 'rw'), ('rwk', 'rwk'), ('sa', 'sa'), ('sad', 'sad'), ('sah', 'sah'), ('sam', 'sam'), ('saq', 'saq'), ('sas', 'sas'), ('sat', 'sat'), ('saz', 'saz'), ('sba', 'sba'), ('sbp', 'sbp'), ('sc', 'sc'), ('scn', 'scn'), ('sco', 'sco'), ('sd', 'sd'), ('sdc', 'sdc'), ('sdh', 'sdh'), ('se', 'se'), ('see', 'see'), ('seh', 'seh'), ('sei', 'sei'), ('sel', 'sel'), ('ses', 'ses'), ('sg', 'sg'), ('sga', 'sga'), ('sgs', 'sgs'), ('sh', 'sh'), ('shi', 'shi'), ('shn', 'shn'), ('shu', 'shu'), ('si', 'si'), ('sid', 'sid'), ('sk', 'sk'), ('sl', 'sl'), ('sli', 'sli'), ('sly', 'sly'), ('sm', 'sm'), ('sma', 'sma'), ('smj', 'smj'), ('smn', 'smn'), ('sms', 'sms'), ('sn', 'sn'), ('snk', 'snk'), ('so', 'so'), ('sog', 'sog'), ('sq', 'sq'), ('sr', 'sr'), ('srn', 'srn'), ('srr', 'srr'), ('ss', 'ss'), ('ssy', 'ssy'), ('st', 'st'), ('stq', 'stq'), ('su', 'su'), ('suk', 'suk'), ('sus', 'sus'), ('sux', 'sux'), ('sv', 'sv'), ('sw', 'sw'), ('swb', 'swb'), ('swc', 'swc'), ('syc', 'syc'), ('syr', 'syr'), ('szl', 'szl'), ('ta', 'ta'), ('tcy', 'tcy'), ('te', 'te'), ('tem', 'tem'), ('teo', 'teo'), ('ter', 'ter'), ('tet', 'tet'), ('tg', 'tg'), ('th', 'th'), ('ti', 'ti'), ('tig', 'tig'), ('tiv', 'tiv'), ('tk', 'tk'), ('tkl', 'tkl'), ('tkr', 'tkr'), ('tl', 'tl'), ('tlh', 'tlh'), ('tli', 'tli'), ('tly', 'tly'), ('tmh', 'tmh'), ('tn', 'tn'), ('to', 'to'), ('tog', 'tog'), ('tpi', 'tpi'), ('tr', 'tr'), ('tru', 'tru'), ('trv', 'trv'), ('ts', 'ts'), ('tsd', 'tsd'), ('tsi', 'tsi'), ('tt', 'tt'), ('ttt', 'ttt'), ('tum', 'tum'), ('tvl', 'tvl'), ('tw', 'tw'), ('twq', 'twq'), ('ty', 'ty'), ('tyv', 'tyv'), ('tzm', 'tzm'), ('udm', 'udm'), ('ug', 'ug'), ('uga', 'uga'), ('uk', 'uk'), ('umb', 'umb'), ('und', 'und'), ('ur', 'ur'), ('uz', 'uz'), ('vai', 'vai'), ('ve', 've'), ('vec', 'vec'), ('vep', 'vep'), ('vi', 'vi'), ('vls', 'vls'), ('vmf', 'vmf'), ('vo', 'vo'), ('vot', 'vot'), ('vro', 'vro'), ('vun', 'vun'), ('wa', 'wa'), ('wae', 'wae'), ('wal', 'wal'), ('war', 'war'), ('was', 'was'), ('wbp', 'wbp'), ('wo', 'wo'), ('wuu', 'wuu'), ('xal', 'xal'), ('xh', 'xh'), ('xmf', 'xmf'), ('xog', 'xog'), ('yao', 'yao'), ('yap', 'yap'), ('yav', 'yav'), ('ybb', 'ybb'), ('yi', 'yi'), ('yo', 'yo'), ('yrl', 'yrl'), ('yue', 'yue'), ('za', 'za'), ('zap', 'zap'), ('zbl', 'zbl'), ('zea', 'zea'), ('zen', 'zen'), ('zgh', 'zgh'), ('zh', 'zh'), ('zh_Hans', 'zh_Hans'), ('zh_Hant', 'zh_Hant'), ('zu', 'zu'), ('zun', 'zun'), ('zxx', 'zxx'), ('zza', 'zza')])),
                ('marketing_permission', models.BooleanField(default=True, verbose_name='marketing permission')),
                ('phone', models.CharField(max_length=64, blank=True, verbose_name='phone')),
                ('www', models.URLField(max_length=128, blank=True, verbose_name='web address')),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True, verbose_name='time zone', null=True)),
                ('prefix', models.CharField(max_length=64, blank=True, verbose_name='name prefix')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('suffix', models.CharField(max_length=64, blank=True, verbose_name='name suffix')),
                ('name_ext', models.CharField(max_length=256, blank=True, verbose_name='name extension')),
                ('email', models.EmailField(max_length=256, blank=True, verbose_name='email')),
                ('merchant_notes', models.TextField(blank=True, verbose_name='merchant notes')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('show_pricing', models.BooleanField(default=True, verbose_name='show as pricing option')),
                ('show_prices_including_taxes', models.NullBooleanField(default=None, verbose_name='show prices including taxes')),
                ('hide_prices', models.NullBooleanField(default=None, verbose_name='hide prices')),
            ],
            options={
                'verbose_name': 'contact group',
                'verbose_name_plural': 'contact groups',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ContactGroupTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ContactGroup')),
            ],
            options={
                'db_table': 'E-Commerce_contactgroup_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'contact group Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', enumfields.fields.EnumIntegerField(serialize=False, enum=E-Commerce.core.models.CounterType, verbose_name='identifier', primary_key=True)),
                ('value', models.IntegerField(default=0, verbose_name='value')),
            ],
            options={
                'verbose_name': 'counter',
                'verbose_name_plural': 'counters',
            },
        ),
        migrations.CreateModel(
            name='CustomerTaxGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'customer tax group',
                'verbose_name_plural': 'customer tax groups',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CustomerTaxGroupTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.CustomerTaxGroup')),
            ],
            options={
                'db_table': 'E-Commerce_customertaxgroup_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'customer tax group Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='FixedCostBehaviorComponentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('description', models.CharField(max_length=100, blank=True, verbose_name='description')),
            ],
            options={
                'db_table': 'E-Commerce_fixedcostbehaviorcomponent_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'fixed cost behavior component Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ImmutableAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('prefix', models.CharField(max_length=64, blank=True, verbose_name='name prefix')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('suffix', models.CharField(max_length=64, blank=True, verbose_name='name suffix')),
                ('name_ext', models.CharField(max_length=255, blank=True, verbose_name='name extension')),
                ('company_name', models.CharField(max_length=255, blank=True, verbose_name='company name')),
                ('tax_number', models.CharField(max_length=64, blank=True, verbose_name='tax number')),
                ('phone', models.CharField(max_length=64, blank=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=128, blank=True, verbose_name='email')),
                ('street', models.CharField(max_length=255, verbose_name='street')),
                ('street2', models.CharField(max_length=255, blank=True, verbose_name='street (2)')),
                ('street3', models.CharField(max_length=255, blank=True, verbose_name='street (3)')),
                ('postal_code', models.CharField(max_length=64, blank=True, verbose_name='postal code')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('region_code', models.CharField(max_length=16, blank=True, verbose_name='region code')),
                ('region', models.CharField(max_length=64, blank=True, verbose_name='region')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'abstract': False,
            },
            bases=(E-Commerce.core.models._base.ChangeProtected, E-Commerce.core.utils.name_mixin.NameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('url', models.CharField(max_length=128, blank=True, verbose_name='URL', null=True)),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='MutableAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('prefix', models.CharField(max_length=64, blank=True, verbose_name='name prefix')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('suffix', models.CharField(max_length=64, blank=True, verbose_name='name suffix')),
                ('name_ext', models.CharField(max_length=255, blank=True, verbose_name='name extension')),
                ('company_name', models.CharField(max_length=255, blank=True, verbose_name='company name')),
                ('tax_number', models.CharField(max_length=64, blank=True, verbose_name='tax number')),
                ('phone', models.CharField(max_length=64, blank=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=128, blank=True, verbose_name='email')),
                ('street', models.CharField(max_length=255, verbose_name='street')),
                ('street2', models.CharField(max_length=255, blank=True, verbose_name='street (2)')),
                ('street3', models.CharField(max_length=255, blank=True, verbose_name='street (3)')),
                ('postal_code', models.CharField(max_length=64, blank=True, verbose_name='postal code')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('region_code', models.CharField(max_length=16, blank=True, verbose_name='region code')),
                ('region', models.CharField(max_length=64, blank=True, verbose_name='region')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'abstract': False,
            },
            bases=(E-Commerce.core.utils.name_mixin.NameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now_add=True, verbose_name='modified on')),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True, db_index=True)),
                ('label', models.CharField(max_length=32, verbose_name='label', db_index=True)),
                ('key', models.CharField(max_length=32, unique=True, verbose_name='key')),
                ('reference_number', models.CharField(blank=True, null=True, max_length=64, unique=True, verbose_name='reference number', db_index=True)),
                ('tax_number', models.CharField(max_length=20, blank=True, verbose_name='tax number')),
                ('phone', models.CharField(max_length=64, blank=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=128, blank=True, verbose_name='email address')),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted', db_index=True)),
                ('payment_status', enumfields.fields.EnumIntegerField(default=0, enum=E-Commerce.core.models.PaymentStatus, verbose_name='payment status', db_index=True)),
                ('shipping_status', enumfields.fields.EnumIntegerField(default=0, enum=E-Commerce.core.models.ShippingStatus, verbose_name='shipping status', db_index=True)),
                ('payment_method_name', models.CharField(default='', max_length=100, blank=True, verbose_name='payment method name')),
                ('payment_data', jsonfield.fields.JSONField(blank=True, verbose_name='payment data', null=True)),
                ('shipping_method_name', models.CharField(default='', max_length=100, blank=True, verbose_name='shipping method name')),
                ('shipping_data', jsonfield.fields.JSONField(blank=True, verbose_name='shipping data', null=True)),
                ('extra_data', jsonfield.fields.JSONField(blank=True, verbose_name='extra data', null=True)),
                ('taxful_total_price_value', E-Commerce.core.fields.MoneyValueField(default=0, max_digits=36, verbose_name='grand total', decimal_places=9, editable=False)),
                ('taxless_total_price_value', E-Commerce.core.fields.MoneyValueField(default=0, max_digits=36, verbose_name='taxless total', decimal_places=9, editable=False)),
                ('currency', E-Commerce.core.fields.CurrencyField(max_length=4, verbose_name='currency')),
                ('prices_include_tax', models.BooleanField(verbose_name='prices include tax')),
                ('display_currency', E-Commerce.core.fields.CurrencyField(max_length=4, blank=True, verbose_name='display currency')),
                ('display_currency_rate', models.DecimalField(default=1, max_digits=36, verbose_name='display currency rate', decimal_places=9)),
                ('ip_address', models.GenericIPAddressField(blank=True, verbose_name='IP address', null=True)),
                ('order_date', models.DateTimeField(verbose_name='order date', editable=False)),
                ('payment_date', models.DateTimeField(verbose_name='payment date', null=True, editable=False)),
                ('language', E-Commerce.core.fields.LanguageField(max_length=10, blank=True, verbose_name='language', choices=[('aa', 'aa'), ('ab', 'ab'), ('ace', 'ace'), ('ach', 'ach'), ('ada', 'ada'), ('ady', 'ady'), ('ae', 'ae'), ('aeb', 'aeb'), ('af', 'af'), ('afh', 'afh'), ('agq', 'agq'), ('ain', 'ain'), ('ak', 'ak'), ('akk', 'akk'), ('akz', 'akz'), ('ale', 'ale'), ('aln', 'aln'), ('alt', 'alt'), ('am', 'am'), ('an', 'an'), ('ang', 'ang'), ('anp', 'anp'), ('ar', 'ar'), ('ar_001', 'ar_001'), ('arc', 'arc'), ('arn', 'arn'), ('aro', 'aro'), ('arp', 'arp'), ('arq', 'arq'), ('arw', 'arw'), ('ary', 'ary'), ('arz', 'arz'), ('as', 'as'), ('asa', 'asa'), ('ase', 'ase'), ('ast', 'ast'), ('av', 'av'), ('avk', 'avk'), ('awa', 'awa'), ('ay', 'ay'), ('az', 'az'), ('ba', 'ba'), ('bal', 'bal'), ('ban', 'ban'), ('bar', 'bar'), ('bas', 'bas'), ('bax', 'bax'), ('bbc', 'bbc'), ('bbj', 'bbj'), ('be', 'be'), ('bej', 'bej'), ('bem', 'bem'), ('bew', 'bew'), ('bez', 'bez'), ('bfd', 'bfd'), ('bfq', 'bfq'), ('bg', 'bg'), ('bgn', 'bgn'), ('bho', 'bho'), ('bi', 'bi'), ('bik', 'bik'), ('bin', 'bin'), ('bjn', 'bjn'), ('bkm', 'bkm'), ('bla', 'bla'), ('bm', 'bm'), ('bn', 'bn'), ('bo', 'bo'), ('bpy', 'bpy'), ('bqi', 'bqi'), ('br', 'br'), ('bra', 'bra'), ('brh', 'brh'), ('brx', 'brx'), ('bs', 'bs'), ('bss', 'bss'), ('bua', 'bua'), ('bug', 'bug'), ('bum', 'bum'), ('byn', 'byn'), ('byv', 'byv'), ('ca', 'ca'), ('cad', 'cad'), ('car', 'car'), ('cay', 'cay'), ('cch', 'cch'), ('ce', 'ce'), ('ceb', 'ceb'), ('cgg', 'cgg'), ('ch', 'ch'), ('chb', 'chb'), ('chg', 'chg'), ('chk', 'chk'), ('chm', 'chm'), ('chn', 'chn'), ('cho', 'cho'), ('chp', 'chp'), ('chr', 'chr'), ('chy', 'chy'), ('ckb', 'ckb'), ('co', 'co'), ('cop', 'cop'), ('cps', 'cps'), ('cr', 'cr'), ('crh', 'crh'), ('cs', 'cs'), ('csb', 'csb'), ('cu', 'cu'), ('cv', 'cv'), ('cy', 'cy'), ('da', 'da'), ('dak', 'dak'), ('dar', 'dar'), ('dav', 'dav'), ('de', 'de'), ('de_AT', 'de_AT'), ('de_CH', 'de_CH'), ('del', 'del'), ('den', 'den'), ('dgr', 'dgr'), ('din', 'din'), ('dje', 'dje'), ('doi', 'doi'), ('dsb', 'dsb'), ('dtp', 'dtp'), ('dua', 'dua'), ('dum', 'dum'), ('dv', 'dv'), ('dyo', 'dyo'), ('dyu', 'dyu'), ('dz', 'dz'), ('dzg', 'dzg'), ('ebu', 'ebu'), ('ee', 'ee'), ('efi', 'efi'), ('egl', 'egl'), ('egy', 'egy'), ('eka', 'eka'), ('el', 'el'), ('elx', 'elx'), ('en', 'en'), ('en_AU', 'en_AU'), ('en_CA', 'en_CA'), ('en_GB', 'en_GB'), ('en_US', 'en_US'), ('enm', 'enm'), ('eo', 'eo'), ('es', 'es'), ('es_419', 'es_419'), ('es_ES', 'es_ES'), ('es_MX', 'es_MX'), ('esu', 'esu'), ('et', 'et'), ('eu', 'eu'), ('ewo', 'ewo'), ('ext', 'ext'), ('fa', 'fa'), ('fa_AF', 'fa_AF'), ('fan', 'fan'), ('fat', 'fat'), ('ff', 'ff'), ('fi', 'fi'), ('fil', 'fil'), ('fit', 'fit'), ('fj', 'fj'), ('fo', 'fo'), ('fon', 'fon'), ('fr', 'fr'), ('fr_CA', 'fr_CA'), ('fr_CH', 'fr_CH'), ('frc', 'frc'), ('frm', 'frm'), ('fro', 'fro'), ('frp', 'frp'), ('frr', 'frr'), ('frs', 'frs'), ('fur', 'fur'), ('fy', 'fy'), ('ga', 'ga'), ('gaa', 'gaa'), ('gag', 'gag'), ('gan', 'gan'), ('gay', 'gay'), ('gba', 'gba'), ('gbz', 'gbz'), ('gd', 'gd'), ('gez', 'gez'), ('gil', 'gil'), ('gl', 'gl'), ('glk', 'glk'), ('gmh', 'gmh'), ('gn', 'gn'), ('goh', 'goh'), ('gom', 'gom'), ('gon', 'gon'), ('gor', 'gor'), ('got', 'got'), ('grb', 'grb'), ('grc', 'grc'), ('gsw', 'gsw'), ('gu', 'gu'), ('guc', 'guc'), ('gur', 'gur'), ('guz', 'guz'), ('gv', 'gv'), ('gwi', 'gwi'), ('ha', 'ha'), ('hai', 'hai'), ('hak', 'hak'), ('haw', 'haw'), ('he', 'he'), ('hi', 'hi'), ('hif', 'hif'), ('hil', 'hil'), ('hit', 'hit'), ('hmn', 'hmn'), ('ho', 'ho'), ('hr', 'hr'), ('hsb', 'hsb'), ('hsn', 'hsn'), ('ht', 'ht'), ('hu', 'hu'), ('hup', 'hup'), ('hy', 'hy'), ('hz', 'hz'), ('ia', 'ia'), ('iba', 'iba'), ('ibb', 'ibb'), ('id', 'id'), ('ie', 'ie'), ('ig', 'ig'), ('ii', 'ii'), ('ik', 'ik'), ('ilo', 'ilo'), ('inh', 'inh'), ('io', 'io'), ('is', 'is'), ('it', 'it'), ('iu', 'iu'), ('izh', 'izh'), ('ja', 'ja'), ('jam', 'jam'), ('jbo', 'jbo'), ('jgo', 'jgo'), ('jmc', 'jmc'), ('jpr', 'jpr'), ('jrb', 'jrb'), ('jut', 'jut'), ('jv', 'jv'), ('ka', 'ka'), ('kaa', 'kaa'), ('kab', 'kab'), ('kac', 'kac'), ('kaj', 'kaj'), ('kam', 'kam'), ('kaw', 'kaw'), ('kbd', 'kbd'), ('kbl', 'kbl'), ('kcg', 'kcg'), ('kde', 'kde'), ('kea', 'kea'), ('ken', 'ken'), ('kfo', 'kfo'), ('kg', 'kg'), ('kgp', 'kgp'), ('kha', 'kha'), ('kho', 'kho'), ('khq', 'khq'), ('khw', 'khw'), ('ki', 'ki'), ('kiu', 'kiu'), ('kj', 'kj'), ('kk', 'kk'), ('kkj', 'kkj'), ('kl', 'kl'), ('kln', 'kln'), ('km', 'km'), ('kmb', 'kmb'), ('kn', 'kn'), ('ko', 'ko'), ('koi', 'koi'), ('kok', 'kok'), ('kos', 'kos'), ('kpe', 'kpe'), ('kr', 'kr'), ('krc', 'krc'), ('kri', 'kri'), ('krj', 'krj'), ('krl', 'krl'), ('kru', 'kru'), ('ks', 'ks'), ('ksb', 'ksb'), ('ksf', 'ksf'), ('ksh', 'ksh'), ('ku', 'ku'), ('kum', 'kum'), ('kut', 'kut'), ('kv', 'kv'), ('kw', 'kw'), ('ky', 'ky'), ('la', 'la'), ('lad', 'lad'), ('lag', 'lag'), ('lah', 'lah'), ('lam', 'lam'), ('lb', 'lb'), ('lez', 'lez'), ('lfn', 'lfn'), ('lg', 'lg'), ('li', 'li'), ('lij', 'lij'), ('liv', 'liv'), ('lkt', 'lkt'), ('lmo', 'lmo'), ('ln', 'ln'), ('lo', 'lo'), ('lol', 'lol'), ('loz', 'loz'), ('lrc', 'lrc'), ('lt', 'lt'), ('ltg', 'ltg'), ('lu', 'lu'), ('lua', 'lua'), ('lui', 'lui'), ('lun', 'lun'), ('luo', 'luo'), ('lus', 'lus'), ('luy', 'luy'), ('lv', 'lv'), ('lzh', 'lzh'), ('lzz', 'lzz'), ('mad', 'mad'), ('maf', 'maf'), ('mag', 'mag'), ('mai', 'mai'), ('mak', 'mak'), ('man', 'man'), ('mas', 'mas'), ('mde', 'mde'), ('mdf', 'mdf'), ('mdr', 'mdr'), ('men', 'men'), ('mer', 'mer'), ('mfe', 'mfe'), ('mg', 'mg'), ('mga', 'mga'), ('mgh', 'mgh'), ('mgo', 'mgo'), ('mh', 'mh'), ('mi', 'mi'), ('mic', 'mic'), ('min', 'min'), ('mk', 'mk'), ('ml', 'ml'), ('mn', 'mn'), ('mnc', 'mnc'), ('mni', 'mni'), ('moh', 'moh'), ('mos', 'mos'), ('mr', 'mr'), ('mrj', 'mrj'), ('ms', 'ms'), ('mt', 'mt'), ('mua', 'mua'), ('mul', 'mul'), ('mus', 'mus'), ('mwl', 'mwl'), ('mwr', 'mwr'), ('mwv', 'mwv'), ('my', 'my'), ('mye', 'mye'), ('myv', 'myv'), ('mzn', 'mzn'), ('na', 'na'), ('nan', 'nan'), ('nap', 'nap'), ('naq', 'naq'), ('nb', 'nb'), ('nd', 'nd'), ('nds', 'nds'), ('nds_NL', 'nds_NL'), ('ne', 'ne'), ('new', 'new'), ('ng', 'ng'), ('nia', 'nia'), ('niu', 'niu'), ('njo', 'njo'), ('nl', 'nl'), ('nl_BE', 'nl_BE'), ('nmg', 'nmg'), ('nn', 'nn'), ('nnh', 'nnh'), ('no', 'no'), ('nog', 'nog'), ('non', 'non'), ('nov', 'nov'), ('nqo', 'nqo'), ('nr', 'nr'), ('nso', 'nso'), ('nus', 'nus'), ('nv', 'nv'), ('nwc', 'nwc'), ('ny', 'ny'), ('nym', 'nym'), ('nyn', 'nyn'), ('nyo', 'nyo'), ('nzi', 'nzi'), ('oc', 'oc'), ('oj', 'oj'), ('om', 'om'), ('or', 'or'), ('os', 'os'), ('osa', 'osa'), ('ota', 'ota'), ('pa', 'pa'), ('pag', 'pag'), ('pal', 'pal'), ('pam', 'pam'), ('pap', 'pap'), ('pau', 'pau'), ('pcd', 'pcd'), ('pdc', 'pdc'), ('pdt', 'pdt'), ('peo', 'peo'), ('pfl', 'pfl'), ('phn', 'phn'), ('pi', 'pi'), ('pl', 'pl'), ('pms', 'pms'), ('pnt', 'pnt'), ('pon', 'pon'), ('prg', 'prg'), ('pro', 'pro'), ('ps', 'ps'), ('pt', 'pt'), ('pt_BR', 'pt_BR'), ('pt_PT', 'pt_PT'), ('qu', 'qu'), ('quc', 'quc'), ('qug', 'qug'), ('raj', 'raj'), ('rap', 'rap'), ('rar', 'rar'), ('rgn', 'rgn'), ('rif', 'rif'), ('rm', 'rm'), ('rn', 'rn'), ('ro', 'ro'), ('ro_MD', 'ro_MD'), ('rof', 'rof'), ('rom', 'rom'), ('root', 'root'), ('rtm', 'rtm'), ('ru', 'ru'), ('rue', 'rue'), ('rug', 'rug'), ('rup', 'rup'), ('rw', 'rw'), ('rwk', 'rwk'), ('sa', 'sa'), ('sad', 'sad'), ('sah', 'sah'), ('sam', 'sam'), ('saq', 'saq'), ('sas', 'sas'), ('sat', 'sat'), ('saz', 'saz'), ('sba', 'sba'), ('sbp', 'sbp'), ('sc', 'sc'), ('scn', 'scn'), ('sco', 'sco'), ('sd', 'sd'), ('sdc', 'sdc'), ('sdh', 'sdh'), ('se', 'se'), ('see', 'see'), ('seh', 'seh'), ('sei', 'sei'), ('sel', 'sel'), ('ses', 'ses'), ('sg', 'sg'), ('sga', 'sga'), ('sgs', 'sgs'), ('sh', 'sh'), ('shi', 'shi'), ('shn', 'shn'), ('shu', 'shu'), ('si', 'si'), ('sid', 'sid'), ('sk', 'sk'), ('sl', 'sl'), ('sli', 'sli'), ('sly', 'sly'), ('sm', 'sm'), ('sma', 'sma'), ('smj', 'smj'), ('smn', 'smn'), ('sms', 'sms'), ('sn', 'sn'), ('snk', 'snk'), ('so', 'so'), ('sog', 'sog'), ('sq', 'sq'), ('sr', 'sr'), ('srn', 'srn'), ('srr', 'srr'), ('ss', 'ss'), ('ssy', 'ssy'), ('st', 'st'), ('stq', 'stq'), ('su', 'su'), ('suk', 'suk'), ('sus', 'sus'), ('sux', 'sux'), ('sv', 'sv'), ('sw', 'sw'), ('swb', 'swb'), ('swc', 'swc'), ('syc', 'syc'), ('syr', 'syr'), ('szl', 'szl'), ('ta', 'ta'), ('tcy', 'tcy'), ('te', 'te'), ('tem', 'tem'), ('teo', 'teo'), ('ter', 'ter'), ('tet', 'tet'), ('tg', 'tg'), ('th', 'th'), ('ti', 'ti'), ('tig', 'tig'), ('tiv', 'tiv'), ('tk', 'tk'), ('tkl', 'tkl'), ('tkr', 'tkr'), ('tl', 'tl'), ('tlh', 'tlh'), ('tli', 'tli'), ('tly', 'tly'), ('tmh', 'tmh'), ('tn', 'tn'), ('to', 'to'), ('tog', 'tog'), ('tpi', 'tpi'), ('tr', 'tr'), ('tru', 'tru'), ('trv', 'trv'), ('ts', 'ts'), ('tsd', 'tsd'), ('tsi', 'tsi'), ('tt', 'tt'), ('ttt', 'ttt'), ('tum', 'tum'), ('tvl', 'tvl'), ('tw', 'tw'), ('twq', 'twq'), ('ty', 'ty'), ('tyv', 'tyv'), ('tzm', 'tzm'), ('udm', 'udm'), ('ug', 'ug'), ('uga', 'uga'), ('uk', 'uk'), ('umb', 'umb'), ('und', 'und'), ('ur', 'ur'), ('uz', 'uz'), ('vai', 'vai'), ('ve', 've'), ('vec', 'vec'), ('vep', 'vep'), ('vi', 'vi'), ('vls', 'vls'), ('vmf', 'vmf'), ('vo', 'vo'), ('vot', 'vot'), ('vro', 'vro'), ('vun', 'vun'), ('wa', 'wa'), ('wae', 'wae'), ('wal', 'wal'), ('war', 'war'), ('was', 'was'), ('wbp', 'wbp'), ('wo', 'wo'), ('wuu', 'wuu'), ('xal', 'xal'), ('xh', 'xh'), ('xmf', 'xmf'), ('xog', 'xog'), ('yao', 'yao'), ('yap', 'yap'), ('yav', 'yav'), ('ybb', 'ybb'), ('yi', 'yi'), ('yo', 'yo'), ('yrl', 'yrl'), ('yue', 'yue'), ('za', 'za'), ('zap', 'zap'), ('zbl', 'zbl'), ('zea', 'zea'), ('zen', 'zen'), ('zgh', 'zgh'), ('zh', 'zh'), ('zh_Hans', 'zh_Hans'), ('zh_Hant', 'zh_Hant'), ('zu', 'zu'), ('zun', 'zun'), ('zxx', 'zxx'), ('zza', 'zza')])),
                ('customer_comment', models.TextField(blank=True, verbose_name='customer comment')),
                ('admin_comment', models.TextField(blank=True, verbose_name='admin comment/notes')),
                ('require_verification', models.BooleanField(default=False, verbose_name='requires verification')),
                ('all_verified', models.BooleanField(default=False, verbose_name='all lines verified')),
                ('marketing_permission', models.BooleanField(default=True, verbose_name='marketing permission')),
                ('_codes', jsonfield.fields.JSONField(blank=True, verbose_name='codes', null=True)),
                ('billing_address', models.ForeignKey(related_name='billing_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='billing address', to='E-Commerce.ImmutableAddress')),
                ('creator', E-Commerce.core.fields.UnsavedForeignKey(related_name='orders_created', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='creating user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ('-id',),
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model),
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('type', enumfields.fields.EnumIntegerField(default=1, verbose_name='line type', enum=E-Commerce.core.models.OrderLineType)),
                ('sku', models.CharField(max_length=48, blank=True, verbose_name='line SKU')),
                ('text', models.CharField(max_length=256, verbose_name='line text')),
                ('accounting_identifier', models.CharField(max_length=32, blank=True, verbose_name='accounting identifier')),
                ('require_verification', models.BooleanField(default=False, verbose_name='require verification')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('extra_data', jsonfield.fields.JSONField(blank=True, verbose_name='extra data', null=True)),
                ('quantity', E-Commerce.core.fields.QuantityField(default=1, max_digits=36, verbose_name='quantity', decimal_places=9)),
                ('base_unit_price_value', E-Commerce.core.fields.MoneyValueField(default=0, max_digits=36, verbose_name='unit price amount (undiscounted)', decimal_places=9)),
                ('discount_amount_value', E-Commerce.core.fields.MoneyValueField(default=0, max_digits=36, verbose_name='total amount of discount', decimal_places=9)),
                ('order', E-Commerce.core.fields.UnsavedForeignKey(related_name='lines', to='E-Commerce.Order', on_delete=django.db.models.deletion.PROTECT, verbose_name='order')),
                ('parent_line', E-Commerce.core.fields.UnsavedForeignKey(related_name='child_lines', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='parent line', to='E-Commerce.OrderLine')),
            ],
            options={
                'verbose_name': 'order line',
                'verbose_name_plural': 'order lines',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model, E-Commerce.core.pricing.Priceful),
        ),
        migrations.CreateModel(
            name='OrderLineTax',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='tax name')),
                ('amount_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, verbose_name='tax amount', decimal_places=9)),
                ('base_amount_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, help_text='Amount that this tax is calculated from', verbose_name='base amount', decimal_places=9)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('order_line', models.ForeignKey(related_name='taxes', to='E-Commerce.OrderLine', on_delete=django.db.models.deletion.PROTECT, verbose_name='order line')),
            ],
            options={
                'ordering': ['ordering'],
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model, E-Commerce.core.taxing.LineTax),
        ),
        migrations.CreateModel(
            name='OrderLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(max_length=64, blank=True, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, verbose_name='extra data', null=True)),
                ('target', models.ForeignKey(related_name='log_entries', to='E-Commerce.Order', verbose_name='target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=False, editable=False, blank=False, max_length=64, unique=True, db_index=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering', db_index=True)),
                ('role', enumfields.fields.EnumIntegerField(default=0, enum=E-Commerce.core.models.OrderStatusRole, verbose_name='role', db_index=True)),
                ('default', models.BooleanField(default=False, verbose_name='default', db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrderStatusTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.OrderStatus')),
            ],
            options={
                'db_table': 'E-Commerce_orderstatus_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'order status Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('gateway_id', models.CharField(max_length=32, verbose_name='gateway ID')),
                ('payment_identifier', models.CharField(max_length=96, unique=True, verbose_name='identifier')),
                ('amount_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, verbose_name='amount', decimal_places=9)),
                ('foreign_amount_value', E-Commerce.core.fields.MoneyValueField(default=None, null=True, max_digits=36, blank=True, verbose_name='foreign amount', decimal_places=9)),
                ('foreign_currency', E-Commerce.core.fields.CurrencyField(default=None, max_length=4, blank=True, verbose_name='foreign amount currency', null=True)),
                ('description', models.CharField(max_length=256, blank=True, verbose_name='description')),
                ('order', models.ForeignKey(related_name='payments', to='E-Commerce.Order', on_delete=django.db.models.deletion.PROTECT, verbose_name='order')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model),
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
                ('choice_identifier', models.CharField(max_length=64, blank=True, verbose_name='choice identifier')),
                ('old_module_identifier', models.CharField(max_length=64, blank=True)),
                ('old_module_data', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'payment method',
                'verbose_name_plural': 'payment methods',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaymentMethodTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=500, blank=True, verbose_name='description')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.PaymentMethod')),
            ],
            options={
                'db_table': 'E-Commerce_paymentmethod_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'payment method Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PersistentCacheEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('module', models.CharField(max_length=64, verbose_name='module')),
                ('key', models.CharField(max_length=64, verbose_name='key')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='time')),
                ('data', jsonfield.fields.JSONField(verbose_name='data')),
            ],
            options={
                'verbose_name': 'cache entry',
                'verbose_name_plural': 'cache entries',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='modified on')),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted', db_index=True, editable=False)),
                ('mode', enumfields.fields.EnumIntegerField(default=0, verbose_name='mode', enum=E-Commerce.core.models.ProductMode)),
                ('stock_behavior', enumfields.fields.EnumIntegerField(default=0, verbose_name='stock', enum=E-Commerce.core.models.StockBehavior)),
                ('shipping_mode', enumfields.fields.EnumIntegerField(default=0, verbose_name='shipping mode', enum=E-Commerce.core.models.ShippingMode)),
                ('sku', models.CharField(max_length=128, unique=True, verbose_name='SKU', db_index=True)),
                ('gtin', models.CharField(max_length=40, blank=True, verbose_name='GTIN', help_text='Global Trade Item Number')),
                ('barcode', models.CharField(max_length=40, blank=True, verbose_name='barcode')),
                ('accounting_identifier', models.CharField(max_length=32, blank=True, verbose_name='bookkeeping account')),
                ('profit_center', models.CharField(max_length=32, blank=True, verbose_name='profit center')),
                ('cost_center', models.CharField(max_length=32, blank=True, verbose_name='cost center')),
                ('width', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='width (mm)', decimal_places=9, unit='mm')),
                ('height', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='height (mm)', decimal_places=9, unit='mm')),
                ('depth', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='depth (mm)', decimal_places=9, unit='mm')),
                ('net_weight', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='net weight (g)', decimal_places=9, unit='g')),
                ('gross_weight', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='gross weight (g)', decimal_places=9, unit='g')),
                ('category', models.ForeignKey(related_name='primary_products', help_text='only used for administration and reporting', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='primary category', to='E-Commerce.Category')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='manufacturer', to='E-Commerce.Manufacturer')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('-id',),
            },
            bases=(E-Commerce.core.taxing.TaxableItem, E-Commerce.core.models._attributes.AttributableMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('numeric_value', models.DecimalField(max_digits=36, blank=True, verbose_name='numeric value', null=True, decimal_places=9)),
                ('datetime_value', models.DateTimeField(blank=True, verbose_name='datetime value', null=True)),
                ('untranslated_string_value', models.TextField(blank=True, verbose_name='untranslated value')),
                ('attribute', models.ForeignKey(verbose_name='attribute', to='E-Commerce.Attribute')),
                ('product', models.ForeignKey(related_name='attributes', to='E-Commerce.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product attribute',
                'verbose_name_plural': 'product attributes',
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductAttributeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('translated_string_value', models.TextField(blank=True, verbose_name='translated value')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ProductAttribute')),
            ],
            options={
                'db_table': 'E-Commerce_productattribute_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'product attribute Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductCrossSell',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name='weight')),
                ('type', enumfields.fields.EnumIntegerField(verbose_name='type', enum=E-Commerce.core.models.ProductCrossSellType)),
                ('product1', models.ForeignKey(related_name='cross_sell_1', to='E-Commerce.Product', verbose_name='primary product')),
                ('product2', models.ForeignKey(related_name='cross_sell_2', to='E-Commerce.Product', verbose_name='secondary product')),
            ],
            options={
                'verbose_name': 'cross sell link',
                'verbose_name_plural': 'cross sell links',
            },
        ),
        migrations.CreateModel(
            name='ProductLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(max_length=64, blank=True, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, verbose_name='extra data', null=True)),
                ('target', models.ForeignKey(related_name='log_entries', to='E-Commerce.Product', verbose_name='target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('kind', enumfields.fields.EnumIntegerField(default=1, enum=E-Commerce.core.models.ProductMediaKind, verbose_name='kind', db_index=True)),
                ('external_url', models.URLField(blank=True, verbose_name='URL', null=True, help_text="Enter URL to external file. If this field is filled, the selected media doesn't apply.")),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled', db_index=True)),
                ('public', models.BooleanField(default=True, verbose_name='public (shown on product page)')),
                ('purchased', models.BooleanField(default=False, verbose_name='purchased (shown for finished purchases)')),
                ('file', filer.fields.file.FilerFileField(null=True, blank=True, verbose_name='file', to='filer.File')),
                ('product', models.ForeignKey(related_name='media', to='E-Commerce.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product attachment',
                'verbose_name_plural': 'product attachments',
                'ordering': ['ordering'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductMediaTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=128, blank=True, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ProductMedia')),
            ],
            options={
                'db_table': 'E-Commerce_productmedia_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'product attachment Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductPackageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('quantity', E-Commerce.core.fields.QuantityField(default=1, max_digits=36, verbose_name='quantity', decimal_places=9)),
                ('child', models.ForeignKey(related_name='+', to='E-Commerce.Product', verbose_name='child product')),
                ('parent', models.ForeignKey(related_name='+', to='E-Commerce.Product', verbose_name='parent product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug', null=True)),
                ('keywords', models.TextField(blank=True, verbose_name='keywords')),
                ('status_text', models.CharField(max_length=128, blank=True, verbose_name='status text', help_text='This text will be shown alongside the product in the shop. (Ex.: "Available in a month")')),
                ('variation_name', models.CharField(max_length=128, blank=True, verbose_name='variation name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.Product')),
            ],
            options={
                'db_table': 'E-Commerce_product_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'product Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('attributes', models.ManyToManyField(related_name='product_types', blank=True, verbose_name='attributes', to='E-Commerce.Attribute')),
            ],
            options={
                'verbose_name': 'product type',
                'verbose_name_plural': 'product types',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductTypeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ProductType')),
            ],
            options={
                'db_table': 'E-Commerce_producttype_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'product type Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductVariationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('combination_hash', models.CharField(max_length=40, unique=True, verbose_name='combination hash', db_index=True)),
                ('status', enumfields.fields.EnumIntegerField(default=1, enum=E-Commerce.core.models.ProductVariationLinkStatus, verbose_name='status', db_index=True)),
                ('product', models.ForeignKey(related_name='variation_result_supers', to='E-Commerce.Product', verbose_name='product')),
                ('result', models.ForeignKey(related_name='variation_result_subs', to='E-Commerce.Product', verbose_name='result')),
            ],
            options={
                'verbose_name': 'variation result',
                'verbose_name_plural': 'variation results',
            },
        ),
        migrations.CreateModel(
            name='ProductVariationVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=False)),
                ('product', models.ForeignKey(related_name='variation_variables', to='E-Commerce.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'variation variable',
                'verbose_name_plural': 'variation variables',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductVariationVariableTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ProductVariationVariable')),
            ],
            options={
                'db_table': 'E-Commerce_productvariationvariable_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'variation variable Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductVariationVariableValue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=False)),
                ('variable', models.ForeignKey(related_name='values', to='E-Commerce.ProductVariationVariable', verbose_name='variation variable')),
            ],
            options={
                'verbose_name': 'variation value',
                'verbose_name_plural': 'variation values',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductVariationVariableValueTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('value', models.CharField(max_length=128, verbose_name='value')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ProductVariationVariableValue')),
            ],
            options={
                'db_table': 'E-Commerce_productvariationvariablevalue_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'variation value Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SalesUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('decimals', models.PositiveSmallIntegerField(default=0, verbose_name='allowed decimals')),
            ],
            options={
                'verbose_name': 'sales unit',
                'verbose_name_plural': 'sales units',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SalesUnitTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('short_name', models.CharField(max_length=128, verbose_name='short name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.SalesUnit')),
            ],
            options={
                'db_table': 'E-Commerce_salesunit_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'sales unit Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SavedAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('role', enumfields.fields.EnumIntegerField(default=1, verbose_name='role', enum=E-Commerce.core.models.SavedAddressRole)),
                ('status', enumfields.fields.EnumIntegerField(default=1, verbose_name='status', enum=E-Commerce.core.models.SavedAddressStatus)),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='title')),
                ('address', models.ForeignKey(related_name='saved_addresses', to='E-Commerce.MutableAddress', verbose_name='address')),
            ],
            options={
                'verbose_name': 'saved address',
                'verbose_name_plural': 'saved addresses',
                'ordering': ('owner_id', 'role', 'title'),
            },
        ),
        migrations.CreateModel(
            name='ServiceBehaviorComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServiceProviderTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'db_table': 'E-Commerce_serviceprovider_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'service provider Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('status', enumfields.fields.EnumIntegerField(default=0, verbose_name='status', enum=E-Commerce.core.models._shipments.ShipmentStatus)),
                ('tracking_code', models.CharField(max_length=64, blank=True, verbose_name='tracking code')),
                ('description', models.CharField(max_length=255, blank=True, verbose_name='description')),
                ('volume', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='volume', decimal_places=9, unit='m3')),
                ('weight', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='weight', decimal_places=9, unit='kg')),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('order', models.ForeignKey(related_name='shipments', to='E-Commerce.Order', on_delete=django.db.models.deletion.PROTECT, verbose_name='order')),
            ],
            options={
                'verbose_name': 'shipment',
                'verbose_name_plural': 'shipments',
            },
        ),
        migrations.CreateModel(
            name='ShipmentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('quantity', E-Commerce.core.fields.QuantityField(default=0, max_digits=36, verbose_name='quantity', decimal_places=9)),
                ('unit_volume', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='unit volume', decimal_places=9, unit='m3')),
                ('unit_weight', E-Commerce.core.fields.MeasurementField(default=0, max_digits=36, verbose_name='unit weight', decimal_places=9, unit='g')),
                ('product', models.ForeignKey(related_name='shipments', to='E-Commerce.Product', verbose_name='product')),
                ('shipment', models.ForeignKey(related_name='products', to='E-Commerce.Shipment', on_delete=django.db.models.deletion.PROTECT, verbose_name='shipment')),
            ],
            options={
                'verbose_name': 'sent product',
                'verbose_name_plural': 'sent products',
            },
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
                ('choice_identifier', models.CharField(max_length=64, blank=True, verbose_name='choice identifier')),
                ('old_module_identifier', models.CharField(max_length=64, blank=True)),
                ('old_module_data', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'shipping method',
                'verbose_name_plural': 'shipping methods',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ShippingMethodTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=500, blank=True, verbose_name='description')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.ShippingMethod')),
            ],
            options={
                'db_table': 'E-Commerce_shippingmethod_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'shipping method Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('domain', models.CharField(unique=True, max_length=128, blank=True, verbose_name='domain', null=True)),
                ('status', enumfields.fields.EnumIntegerField(default=0, verbose_name='status', enum=E-Commerce.core.models.ShopStatus)),
                ('options', jsonfield.fields.JSONField(blank=True, verbose_name='options', null=True)),
                ('currency', E-Commerce.core.fields.CurrencyField(default=E-Commerce.core.models._shops._get_default_currency, max_length=4, verbose_name='currency')),
                ('prices_include_tax', models.BooleanField(default=True, verbose_name='prices include tax')),
                ('maintenance_mode', models.BooleanField(default=False, verbose_name='maintenance mode')),
                ('contact_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='contact address', to='E-Commerce.MutableAddress')),
                ('logo', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='logo', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(E-Commerce.core.models._base.ChangeProtected, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('visible', models.BooleanField(default=True, verbose_name='visible', db_index=True)),
                ('listed', models.BooleanField(default=True, verbose_name='listed', db_index=True)),
                ('purchasable', models.BooleanField(default=True, verbose_name='purchasable', db_index=True)),
                ('searchable', models.BooleanField(default=True, verbose_name='searchable', db_index=True)),
                ('visibility_limit', enumfields.fields.EnumIntegerField(default=1, enum=E-Commerce.core.models.ProductVisibility, verbose_name='visibility limitations', db_index=True)),
                ('purchase_multiple', E-Commerce.core.fields.QuantityField(default=0, max_digits=36, verbose_name='purchase multiple', decimal_places=9)),
                ('minimum_purchase_quantity', E-Commerce.core.fields.QuantityField(default=1, max_digits=36, verbose_name='minimum purchase', decimal_places=9)),
                ('limit_shipping_methods', models.BooleanField(default=False, verbose_name='limited for shipping methods')),
                ('limit_payment_methods', models.BooleanField(default=False, verbose_name='limited for payment methods')),
                ('default_price_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, blank=True, verbose_name='default price', null=True, decimal_places=9)),
                ('minimum_price_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, blank=True, verbose_name='minimum price', null=True, decimal_places=9)),
                ('categories', models.ManyToManyField(related_name='shop_products', blank=True, verbose_name='categories', to='E-Commerce.Category')),
                ('payment_methods', models.ManyToManyField(related_name='payment_products', blank=True, verbose_name='payment methods', to='E-Commerce.PaymentMethod')),
                ('primary_category', models.ForeignKey(related_name='primary_shop_products', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='primary category', to='E-Commerce.Category')),
                ('product', E-Commerce.core.fields.UnsavedForeignKey(related_name='shop_products', to='E-Commerce.Product', verbose_name='product')),
                ('shipping_methods', models.ManyToManyField(related_name='shipping_products', blank=True, verbose_name='shipping methods', to='E-Commerce.ShippingMethod')),
                ('shop', models.ForeignKey(related_name='shop_products', to='E-Commerce.Shop', verbose_name='shop')),
                ('shop_primary_image', models.ForeignKey(related_name='primary_image_for_shop_products', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='primary image', to='E-Commerce.ProductMedia')),
            ],
            bases=(E-Commerce.utils.properties.MoneyPropped, models.Model),
        ),
        migrations.CreateModel(
            name='ShopTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('public_name', models.CharField(max_length=64, verbose_name='public name')),
                ('maintenance_message', models.CharField(max_length=300, blank=True, verbose_name='maintenance message')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.Shop')),
            ],
            options={
                'db_table': 'E-Commerce_shop_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'shop Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SuppliedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sku', models.CharField(max_length=128, verbose_name='SKU', db_index=True)),
                ('alert_limit', models.IntegerField(default=0, verbose_name='alert limit')),
                ('physical_count', E-Commerce.core.fields.QuantityField(default=0, max_digits=36, verbose_name='physical stock count', decimal_places=9, editable=False)),
                ('logical_count', E-Commerce.core.fields.QuantityField(default=0, max_digits=36, verbose_name='logical stock count', decimal_places=9, editable=False)),
                ('product', models.ForeignKey(verbose_name='product', to='E-Commerce.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('type', enumfields.fields.EnumIntegerField(default=1, verbose_name='supplier type', enum=E-Commerce.core.models.SupplierType)),
                ('stock_managed', models.BooleanField(default=False, verbose_name='stock managed')),
                ('module_identifier', models.CharField(max_length=64, blank=True, verbose_name='module')),
                ('module_data', jsonfield.fields.JSONField(blank=True, verbose_name='module data', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(E-Commerce.core.modules.interface.ModuleInterface, models.Model),
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('rate', models.DecimalField(help_text='The percentage rate of the tax.', null=True, max_digits=6, blank=True, verbose_name='tax rate', decimal_places=5)),
                ('amount_value', E-Commerce.core.fields.MoneyValueField(default=None, help_text='The flat amount of the tax. Mutually exclusive with percentage rates.', null=True, max_digits=36, blank=True, verbose_name='tax amount value', decimal_places=9)),
                ('currency', E-Commerce.core.fields.CurrencyField(default=None, max_length=4, blank=True, verbose_name='currency of tax amount', null=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'tax',
                'verbose_name_plural': 'taxes',
            },
            bases=(E-Commerce.utils.properties.MoneyPropped, E-Commerce.core.models._base.ChangeProtected, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TaxClass',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(null=True, editable=False, max_length=64, blank=True, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'tax class',
                'verbose_name_plural': 'tax classes',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TaxClassTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.TaxClass')),
            ],
            options={
                'db_table': 'E-Commerce_taxclass_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'tax class Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.Tax')),
            ],
            options={
                'db_table': 'E-Commerce_tax_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'tax Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WaivingCostBehaviorComponentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('description', models.CharField(max_length=100, blank=True, verbose_name='description')),
            ],
            options={
                'db_table': 'E-Commerce_waivingcostbehaviorcomponent_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'waiving cost behavior component Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WeightBasedPriceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('min_value', E-Commerce.core.fields.MeasurementField(default=0, null=True, max_digits=36, blank=True, verbose_name='min weight', decimal_places=9, unit='g')),
                ('max_value', E-Commerce.core.fields.MeasurementField(default=0, null=True, max_digits=36, blank=True, verbose_name='max weight', decimal_places=9, unit='g')),
                ('price_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='WeightBasedPriceRangeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('description', models.CharField(max_length=100, blank=True, verbose_name='description')),
                ('master', models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.WeightBasedPriceRange')),
            ],
            options={
                'db_table': 'E-Commerce_weightbasedpricerange_translation',
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'weight based price range Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AnonymousContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.Contact')),
            ],
            options={
                'managed': False,
            },
            bases=('E-Commerce.contact',),
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('serviceprovider_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceProvider')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.serviceprovider',),
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.Contact')),
                ('tax_number', models.CharField(max_length=32, blank=True, verbose_name='tax number', help_text='e.g. EIN in US or VAT code in Europe')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
            bases=('E-Commerce.contact',),
        ),
        migrations.CreateModel(
            name='FixedCostBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
                ('price_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent', parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GroupAvailabilityBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
        migrations.CreateModel(
            name='PaymentProcessor',
            fields=[
                ('serviceprovider_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceProvider')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.serviceprovider',),
        ),
        migrations.CreateModel(
            name='PersonContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.Contact')),
                ('gender', enumfields.fields.EnumField(default='u', max_length=4, verbose_name='gender', enum=E-Commerce.core.models.Gender)),
                ('birth_date', models.DateField(blank=True, verbose_name='birth date', null=True)),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, blank=True, verbose_name='last name')),
                ('user', models.OneToOneField(related_name='contact', blank=True, null=True, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=('E-Commerce.contact',),
        ),
        migrations.CreateModel(
            name='RoundingBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
                ('quant', models.DecimalField(default=Decimal('0.05'), max_digits=36, verbose_name='rounding quant', decimal_places=9)),
                ('mode', enumfields.fields.EnumField(default='ROUND_HALF_UP', max_length=50, verbose_name='rounding mode', enum=E-Commerce.core.models.RoundingMode)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
        migrations.CreateModel(
            name='StaffOnlyBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
        migrations.CreateModel(
            name='WaivingCostBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
                ('price_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
                ('waive_limit_value', E-Commerce.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent', parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='WeightBasedPricingBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
        migrations.CreateModel(
            name='WeightLimitsBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.ServiceBehaviorComponent')),
                ('min_weight', models.DecimalField(max_digits=36, blank=True, verbose_name='minimum weight', null=True, decimal_places=6)),
                ('max_weight', models.DecimalField(max_digits=36, blank=True, verbose_name='maximum weight', null=True, decimal_places=6)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
        migrations.AddField(
            model_name='suppliedproduct',
            name='supplier',
            field=models.ForeignKey(verbose_name='supplier', to='E-Commerce.Supplier'),
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='suppliers',
            field=models.ManyToManyField(related_name='shop_products', blank=True, verbose_name='suppliers', to='E-Commerce.Supplier'),
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='visibility_groups',
            field=models.ManyToManyField(related_name='visible_products', blank=True, verbose_name='visible for groups', to='E-Commerce.ContactGroup'),
        ),
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='contact', to='E-Commerce.Contact'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='behavior_components',
            field=models.ManyToManyField(verbose_name='behavior components', to='E-Commerce.ServiceBehaviorComponent'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='logo',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='logo', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='shop',
            field=models.ForeignKey(verbose_name='shop', to='E-Commerce.Shop'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='tax_class',
            field=models.ForeignKey(to='E-Commerce.TaxClass', verbose_name='tax class', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='shipment',
            name='supplier',
            field=models.ForeignKey(related_name='shipments', to='E-Commerce.Supplier', on_delete=django.db.models.deletion.PROTECT, verbose_name='supplier'),
        ),
        migrations.AddField(
            model_name='serviceprovidertranslation',
            name='master',
            field=models.ForeignKey(related_name='base_translations', null=True, editable=False, to='E-Commerce.ServiceProvider'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='logo',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='logo', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_E-Commerce.serviceprovider_set+', null=True, editable=False, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='servicebehaviorcomponent',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_E-Commerce.servicebehaviorcomponent_set+', null=True, editable=False, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='savedaddress',
            name='owner',
            field=models.ForeignKey(verbose_name='owner', to='E-Commerce.Contact'),
        ),
        migrations.AddField(
            model_name='productmedia',
            name='shops',
            field=models.ManyToManyField(related_name='product_media', verbose_name='shops', to='E-Commerce.Shop'),
        ),
        migrations.AddField(
            model_name='product',
            name='primary_image',
            field=models.ForeignKey(related_name='primary_image_for_products', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='primary image', to='E-Commerce.ProductMedia'),
        ),
        migrations.AddField(
            model_name='product',
            name='sales_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='unit', to='E-Commerce.SalesUnit'),
        ),
        migrations.AddField(
            model_name='product',
            name='tax_class',
            field=models.ForeignKey(to='E-Commerce.TaxClass', verbose_name='tax class', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(related_name='products', to='E-Commerce.ProductType', on_delete=django.db.models.deletion.PROTECT, verbose_name='product type'),
        ),
        migrations.AddField(
            model_name='product',
            name='variation_parent',
            field=models.ForeignKey(related_name='variation_children', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='variation parent', to='E-Commerce.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='persistentcacheentry',
            unique_together=set([('module', 'key')]),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='behavior_components',
            field=models.ManyToManyField(verbose_name='behavior components', to='E-Commerce.ServiceBehaviorComponent'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='logo',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='logo', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='shop',
            field=models.ForeignKey(verbose_name='shop', to='E-Commerce.Shop'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='tax_class',
            field=models.ForeignKey(to='E-Commerce.TaxClass', verbose_name='tax class', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='orderlinetax',
            name='tax',
            field=models.ForeignKey(related_name='order_line_taxes', to='E-Commerce.Tax', on_delete=django.db.models.deletion.PROTECT, verbose_name='tax'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=E-Commerce.core.fields.UnsavedForeignKey(related_name='order_lines', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='product', to='E-Commerce.Product'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='supplier',
            field=E-Commerce.core.fields.UnsavedForeignKey(related_name='order_lines', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='supplier', to='E-Commerce.Supplier'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=E-Commerce.core.fields.UnsavedForeignKey(related_name='customer_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='customer', to='E-Commerce.Contact'),
        ),
        migrations.AddField(
            model_name='order',
            name='modified_by',
            field=E-Commerce.core.fields.UnsavedForeignKey(related_name='orders_modified', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='modifier user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=E-Commerce.core.fields.UnsavedForeignKey(default=None, related_name='payment_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='payment method', to='E-Commerce.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='shipping address', to='E-Commerce.ImmutableAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=E-Commerce.core.fields.UnsavedForeignKey(default=None, related_name='shipping_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='shipping method', to='E-Commerce.ShippingMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=E-Commerce.core.fields.UnsavedForeignKey(to='E-Commerce.Shop', verbose_name='shop', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=E-Commerce.core.fields.UnsavedForeignKey(to='E-Commerce.OrderStatus', verbose_name='status', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='contactgroup',
            name='members',
            field=models.ManyToManyField(related_name='groups', blank=True, verbose_name='members', to='E-Commerce.Contact'),
        ),
        migrations.AddField(
            model_name='contact',
            name='default_billing_address',
            field=models.ForeignKey(related_name='+', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='billing address', to='E-Commerce.MutableAddress'),
        ),
        migrations.AddField(
            model_name='contact',
            name='default_payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='default payment method', to='E-Commerce.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='contact',
            name='default_shipping_address',
            field=models.ForeignKey(related_name='+', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='shipping address', to='E-Commerce.MutableAddress'),
        ),
        migrations.AddField(
            model_name='contact',
            name='default_shipping_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='default shipping method', to='E-Commerce.ShippingMethod'),
        ),
        migrations.AddField(
            model_name='contact',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_E-Commerce.contact_set+', null=True, editable=False, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tax_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='tax group', to='E-Commerce.CustomerTaxGroup'),
        ),
        migrations.AddField(
            model_name='configurationitem',
            name='shop',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='shop', to='E-Commerce.Shop'),
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(related_name='categories', blank=True, verbose_name='shops', to='E-Commerce.Shop'),
        ),
        migrations.AddField(
            model_name='category',
            name='visibility_groups',
            field=models.ManyToManyField(related_name='visible_categories', blank=True, verbose_name='visible for groups', to='E-Commerce.ContactGroup'),
        ),
        migrations.CreateModel(
            name='CustomCarrier',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.Carrier')),
            ],
            options={
                'verbose_name': 'custom carrier',
                'verbose_name_plural': 'custom carriers',
            },
            bases=('E-Commerce.carrier',),
        ),
        migrations.CreateModel(
            name='CustomPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='E-Commerce.PaymentProcessor')),
            ],
            options={
                'verbose_name': 'custom payment processor',
                'verbose_name_plural': 'custom payment processors',
            },
            bases=('E-Commerce.paymentprocessor',),
        ),
        migrations.AlterUniqueTogether(
            name='weightbasedpricerangetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='weightbasedpricerange',
            name='component',
            field=models.ForeignKey(related_name='ranges', to='E-Commerce.WeightBasedPricingBehaviorComponent'),
        ),
        migrations.AddField(
            model_name='waivingcostbehaviorcomponenttranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.WaivingCostBehaviorComponent'),
        ),
        migrations.AlterUniqueTogether(
            name='taxtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='taxclasstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='suppliedproduct',
            unique_together=set([('supplier', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='shoptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='shopproduct',
            unique_together=set([('shop', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='shippingmethodtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='carrier', to='E-Commerce.Carrier'),
        ),
        migrations.AlterUniqueTogether(
            name='serviceprovidertranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='salesunittranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='productvariationvariablevaluetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='productvariationvariablevalue',
            unique_together=set([('variable', 'identifier')]),
        ),
        migrations.AlterUniqueTogether(
            name='productvariationvariabletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='productvariationvariable',
            unique_together=set([('product', 'identifier')]),
        ),
        migrations.AlterUniqueTogether(
            name='producttypetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='productpackagelink',
            unique_together=set([('parent', 'child')]),
        ),
        migrations.AlterUniqueTogether(
            name='productmediatranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='productattributetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='paymentmethodtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='payment_processor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='payment processor', to='E-Commerce.PaymentProcessor'),
        ),
        migrations.AlterUniqueTogether(
            name='orderstatustranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='order',
            name='orderer',
            field=E-Commerce.core.fields.UnsavedForeignKey(related_name='orderer_orders', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, verbose_name='orderer', to='E-Commerce.PersonContact'),
        ),
        migrations.AddField(
            model_name='groupavailabilitybehaviorcomponent',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', to='E-Commerce.ContactGroup'),
        ),
        migrations.AddField(
            model_name='fixedcostbehaviorcomponenttranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', null=True, editable=False, to='E-Commerce.FixedCostBehaviorComponent'),
        ),
        migrations.AlterUniqueTogether(
            name='customertaxgrouptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='contactgrouptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='contact',
            name='account_manager',
            field=models.ForeignKey(null=True, blank=True, verbose_name='account manager', to='E-Commerce.PersonContact'),
        ),
        migrations.AlterUniqueTogether(
            name='configurationitem',
            unique_together=set([('shop', 'key')]),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='members',
            field=models.ManyToManyField(related_name='company_memberships', blank=True, verbose_name='members', to='E-Commerce.Contact'),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='attributetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='waivingcostbehaviorcomponenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='fixedcostbehaviorcomponenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
