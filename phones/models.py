from django.db import models
from datetime import datetime, timedelta

class Phone(models.Model):
    PHONE_MODELS = (('9320', '9320'),
                    ('9720', '9720'),
                    ('9900', '9900'),
                    ('9790', '9790'),
                    ('9360', '9360'),
                    ('9105', '9105'),
    )
    BRANCH = (
        ('Ahmet', 'Ahmet'),
        ('Aki', 'Aki'),
        ('Amersfoort', 'Amersfoort'),
        ('Antwerp', 'Antwerp'),
        ('Arap Breda', 'Arap Breda'),
        ('Atilla', 'Atilla'),
        ('Barca', 'Barca'),
        ('Birdman', 'Birdman'),
        ('BTC', 'BTC'),
        ('buuf', 'Buuf'),
        ('Denmark', 'Denmark'),
        ('Den Bosch', 'Den Bosch'),
        ('Deniz', 'Deniz'),
        ('Devrim', 'Devrim'),
        ('Eindhoven', 'Eindhoven'),
        ('Enschede', 'Enschede'),
        ('eniste', 'Eniste'),
        ('Europa', 'Europa'),
        ('grow', 'Grow'),
        ('hille', 'Hille'),
        ('Hilversum', 'Hilversum'),
        ('Homer', 'Homer'),
        ('Hoorn', 'Hoorn'),
        ('Ierland', 'Ierland'),
        ('Kenan', 'Kenan'),
        ('kinker', 'Kinker'),
        ('Kleine', 'Kleine'),
        ('mand', 'Mand'),
        ('Office','Office'),
        ('Omer Den', 'Omer Den'),
        ('Omer Rot', 'Omer Rot'),
        ('plein', 'Plein'),
        ('Prince', 'Prince'),
        ('Rado', 'Rado'),
        ('senti', 'Senti'),
        ('ser-ist', 'Sin-ist'),
        ('Spain', 'Spain'),
        ('st-weg', 'St-weg'),
        ('Sufi', 'Sufi'),
        ('Tarlock', 'Tarlock'),
        ('tol', 'Tol'),
        ('uzun', 'Uzun'),
        ('v.Wou', 'v.Wou'),
        ('viji', 'Viji'),
        ('Zub', 'Zub'),
        ('Zwager', 'Zwager'),
        ('Zwolle', 'Zwolle'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    ACTIVATION = (('90', '3 maanden'),
        ('182', '6 maanden'),
        )
    email = models.EmailField(unique=True)
    imei = models.CharField(max_length=20, blank=True)
    pin = models.CharField(max_length=25, blank=True)
    key = models.CharField(max_length=50, blank=True)
    activation_date = models.DateField(blank=True, null=True)
    activation_choice = models.CharField(max_length=15, choices=ACTIVATION, blank=True)
    activation_enddate = models.DateField(blank=True, null=True) 
    phone_model = models.CharField(max_length=15, choices=PHONE_MODELS, blank=True)
    sim = models.CharField(max_length=25)
    secure_messaging = models.CharField(max_length=25, blank=True)
    branch =  models.CharField(max_length=15, choices=BRANCH, blank=True)
    comment = models.TextField(blank=True)


    def extend_dates(self):
        date_format = "%d/%m/%y"
        #edates_query = list(self.extenddate_set.order_by('date'))
        #return ', '.join(str(d.extend_enddate) for d in edates_query)
        dates = [d.date.strftime(date_format) + '->' + d.extend_enddate.strftime(date_format) for d in self.extenddate_set.order_by('date')]
        #return '{0[0]}'.format(*dates)
        #return dates
        return ' , '.join(str(d) for d in dates)
    extend_dates.admin_order_field = "extenddate__date"


    def email_history(self):
        email_query = list(self.emailhistory_set.order_by('date'))
        return ', '.join(str(d) for d in email_query)

    def sim_history(self):
        sim_query = list(self.simhistory_set.order_by('date'))
        return ', '.join(str(d) for d in sim_query)

    def activation_and_enddate(self):
        #return ', '.join(self.activation_date, self.activation_enddate)
        date_format = "%d/%m/%y"
        if self.activation_date and self.activation_enddate:
            adad = [self.activation_date.strftime(date_format), self.activation_enddate.strftime(date_format)]
            return '{0}, {1}'.format(*adad)
        else: 
            return ''
        #ada = self.activation_date.strftime(date_format)
        #return '{!s:%d-%m-%y}, {}'.format(self.activation_date, self.activation_enddate)
        #return ada
    activation_and_enddate.admin_order_field = "activation_date"

    def save(self, *args, **kwargs):
        # email_history = self.email_history()
        # sim_history = self.sim_history()
        self.email = self.email.upper()
        if self.activation_choice and self.activation_date:
            # p = Phone.objects.get(email=self.email)
            self.activation_enddate = self.activation_date + timedelta(days=int(self.activation_choice))
            # self.save(update_fields=['activation_enddate'])
        super(Phone, self).save(*args, **kwargs)
        # if self.extend_dates():
        # self.extenddate_set.order_by('date')[0].date + timedelta(days=int(self.))
        if not self.email_history() or self.email != self.emailhistory_set.order_by('-date')[0].email:
            newemail = EmailHistory(phone=self, email=self.email, date=datetime.now())
            newemail.save()
        if not self.sim_history() or self.sim != self.simhistory_set.order_by('-date')[0].sim:
            newsim = SimHistory(phone=self, sim=self.sim, date=datetime.now())
            newsim.save()
        


    def __str__(self):
        return self.email

class ExtendDate(models.Model):
    BRANCH = (
        ('Ahmet', 'Ahmet'),
        ('Aki', 'Aki'),
        ('Amersfoort', 'Amersfoort'),
        ('Antwerp', 'Antwerp'),
        ('Arap Breda', 'Arap Breda'),
        ('Atilla', 'Atilla'),
        ('Barca', 'Barca'),
        ('Birdman', 'Birdman'),
        ('BTC', 'BTC'),
        ('buuf', 'Buuf'),
        ('Denmark', 'Denmark'),
        ('Den Bosch', 'Den Bosch'),
        ('Deniz', 'Deniz'),
        ('Devrim', 'Devrim'),
        ('Eindhoven', 'Eindhoven'),
        ('Enschede', 'Enschede'),
        ('eniste', 'Eniste'),
        ('Europa', 'Europa'),
        ('grow', 'Grow'),
        ('hille', 'Hille'),
        ('Hilversum', 'Hilversum'),
        ('Homer', 'Homer'),
        ('Hoorn', 'Hoorn'),
        ('Ierland', 'Ierland'),
        ('Kenan', 'Kenan'),
        ('kinker', 'Kinker'),
        ('Kleine', 'Kleine'),
        ('mand', 'Mand'),
        ('Office','Office'),
        ('Omer Den', 'Omer Den'),
        ('Omer Rot', 'Omer Rot'),
        ('plein', 'Plein'),
        ('Prince', 'Prince'),
        ('Rado', 'Rado'),
        ('senti', 'Senti'),
        ('ser-ist', 'Sin-ist'),
        ('Spain', 'Spain'),
        ('st-weg', 'St-weg'),
        ('Sufi', 'Sufi'),
        ('Tarlock', 'Tarlock'),
        ('tol', 'Tol'),
        ('uzun', 'Uzun'),
        ('v.Wou', 'v.Wou'),
        ('viji', 'Viji'),
        ('Zub', 'Zub'),
        ('Zwager', 'Zwager'),
        ('Zwolle', 'Zwolle'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    PERIODS = (('91', '3 maanden'),
            ('180', '6 maanden'),
    )
    phone = models.ForeignKey(Phone)
    date = models.DateField('extend date', blank=True, null=True)
    extend_period = models.CharField(max_length=15, choices=PERIODS, blank=True)
    extend_enddate = models.DateField(blank=True, null=True)
    extend_branch =  models.CharField(max_length=25, choices=BRANCH, blank=True)

    def save(self, *args, **kwargs):
        if self.date and self.extend_period:
            self.extend_enddate = self.date + timedelta(days=int(self.extend_period))
        super(ExtendDate, self).save(*args, **kwargs)

    def __str__(self):
        return self.date.strftime("%d/%m/%y") #self.date

class EmailHistory(models.Model):
    phone = models.ForeignKey(Phone)
    email = models.EmailField('email history', blank=True)
    date = models.DateTimeField('email change date', blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.email, self.date)

class SimHistory(models.Model):
    phone = models.ForeignKey(Phone)
    sim = models.CharField('sim history', max_length=25, blank=True)
    date = models.DateTimeField('sim change date', blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.sim, self.date)