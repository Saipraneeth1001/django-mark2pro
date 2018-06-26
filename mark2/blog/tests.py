# from django.test import TestCase
# Create your tests here.


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['author'].queryset = User.objects.none()


def __init__(self, *args, **kwargs):
        super(Post, self).__init__(self, *args, **kwargs)
        self.user_name = self.author