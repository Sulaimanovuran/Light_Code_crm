from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

DIRECTION = (
    ('python', 'Python'),
    ('js', 'JavaScript')
)

TIME = (
    ('morning', 'Morning'),
    ('evening', 'Evening')
)

RATE = (
    ('online', 'Online'),
    ('offline', 'Offline'),
    ('standart+', 'Standart+')
)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password=None, **extra):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email),
                          full_name=full_name, phone_number=phone_number, **extra)

        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra):
        if password is None:
            raise TypeError('Superusers must have a password.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, verbose_name='ФИО', null=True)
    phone_number = models.CharField(max_length=15, default='+996', null=True)
    is_active = models.BooleanField(default=True)
    username = None
    direction = models.CharField(max_length=50, choices=DIRECTION, null=True)
    is_staff = models.BooleanField(default=False)
    code = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f'{self.id}. {self.email}'


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor', editable=False)

    def __str__(self):
        return f'{self.id}. {self.user.full_name}'

    def save(self, *args, **kwargs):
        self.user.is_staff = True
        super(Mentor, self).save(*args, **kwargs)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    time = models.CharField(max_length=50, choices=TIME)
    code = models.CharField(max_length=50, null=True, blank=True)
    receipt_date = models.DateTimeField(auto_now=True)
    rate = models.CharField(max_length=20, choices=RATE)
    payment = models.IntegerField()
    remaining_amount = models.IntegerField(default=15000)
    end_date = models.CharField(max_length=50, null=True, blank=True)
    certificate = models.FileField(verbose_name='Сертификат', upload_to='Сетификаты/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.user.full_name}'

    def save(self, *args, **kwargs):
        self.remaining_amount -= self.payment
        super(Student, self).save(*args, **kwargs)


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    date = models.DateField(auto_now_add=True, verbose_name='Дата:')
    subject = models.CharField(max_length=50, verbose_name='Тема:')
    grade = models.IntegerField()
    oop = models.CharField(max_length=50, verbose_name='OOP')

    def __str__(self):
        return f'{self.id}. {self.student.user}'


class Leed(models.Model):
    full_name = models.CharField(max_length=100, default='+996', verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    enrolled = models.BooleanField(verbose_name='Записан', default=False)

    # date
    def __str__(self):
        return f'{self.id}. {self.full_name}'



def create_activation_code():
    import uuid
    code = str(uuid.uuid4())
    return code
