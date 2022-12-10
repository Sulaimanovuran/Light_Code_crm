# from djoser.serializers import UserCreateSerializer
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Mentor, DIRECTION, TIME, Student, Leed, Score, RATE, create_activation_code


class RegisterMentorSerializer(serializers.Serializer):
    '''Регистрация ментора'''

    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(min_length=6)
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    direction = serializers.ChoiceField(choices=DIRECTION)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь уже существует!')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        validated_data['is_staff'] = True
        user = User.objects.create_user(**validated_data)
        Mentor.objects.create(user=user)
        return user

    def to_representation(self, instance):
        rep = {}
        fields = ('email', 'password', 'full_name', 'direction', 'phone_number', 'is_staff')
        for field in fields:
            rep[field] = getattr(instance, field)
        return rep

    # def update(self, instance, validated_data):
    #     direction = validated_data.pop('direction')
    #     print(instance, '!!!!!!!!!!!!!!!!!!!!!!11111')
    #     user = User.objects.create_user(**validated_data)
    #     is_mentor_xui = validated_data['is_mentor']
    #     if is_mentor_xui == True:
    #         Mentor.objects.create(user=user, direction=direction)
    #     return user


class RegisterStudentSerializer(serializers.Serializer):
    '''Регистрация студента'''

    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(min_length=6)
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    direction = serializers.ChoiceField(choices=DIRECTION)
    time = serializers.ChoiceField(choices=TIME)
    rate = serializers.ChoiceField(choices=RATE)
    payment = serializers.IntegerField()

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь уже существует!')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        time = validated_data.pop('time')
        rate = validated_data.pop('rate')
        payment = validated_data.pop('payment')
        validated_data['code'] = create_activation_code()
        code = validated_data['code']
        user = User.objects.create_user(**validated_data)
        student = Student.objects.create(user=user, time=time, rate=rate, payment=payment, code=code)
        return user

    def to_representation(self, instance):
        rep = {}
        fields = ('email', 'password', 'full_name', 'direction', 'phone_number',)
        for field in fields:
            rep[field] = getattr(instance, field)
        return rep


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегестрирован!')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Неправильный логин или пароль!")
            attrs['user'] = user
            return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'direction']
        ref_name = 'user'


class UserMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class LeedSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)

    def create(self, validated_data):
        leed = Leed.objects.create(**validated_data)
        return leed


class LeedMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leed
        fields = "__all__"
