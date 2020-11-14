# from django.db.models.signals import post_save
# from django.contrib.auth.models import User, Group
# from .models import Profile
#
#
# def user_profile(sender, instance, created, **kwargs):
#     if created:
#         groups = Group.objects.get(name='customer')
#         instance.group.add(groups)
#
