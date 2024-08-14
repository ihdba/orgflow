
# from the app.models import the models you will work with
from orm.models import Restaurant, Rating, Sale
# import user
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection # to print sql statements



def run():
    
    restaurant = Restaurant.objects.first()
    user = User.objects.first()
    
    
    Rating.objects.create(
        user=user, 
        restaurant=restaurant, 
        rating=3)
    
    
    
    
    # print the sql statements
    #print(connection.queries)