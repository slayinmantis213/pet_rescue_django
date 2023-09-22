from django.db import models
from model_utils.managers import InheritanceManager
from users.models import User
import random, math
from datetime import datetime


class Pet(models.Model):
    user = models.ForeignKey(User, related_name="pets", on_delete= models.CASCADE, default= None)
    name = models.CharField(max_length=45, default="Edit to add name")
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    energy = models.IntegerField(default=1)
    happiness = models.IntegerField(default=1)
    max_health = models.IntegerField(default=1)
    max_energy = models.IntegerField(default=1)
    max_happiness = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InheritanceManager()

    
    @classmethod
    def build_pet(cls, data):
        pets = {
            Glorb : ['Glorb', random.randrange(4,8),random.randrange(3,5),random.randrange(4,8)],
            Snek : ['Snek', random.randrange(6,10), random.randrange(3,5), random.randrange(6,10)],
            GreenDragon :['Green Dragon', random.randrange(8,12), random.randrange(3,5), random.randrange(8,12)],
            Siren :['Cat-siren', random.randrange(3,13), random.randrange(4,6), random.randrange(3,13)],
            RedDragon : ['Red Dragon', random.randrange(10,14), random.randrange(5,7), random.randrange(10,14)],
            Moogle : ['Moogle', random.randrange(7,21), random.randrange(5,7), random.randrange(7,21)],
            Griffin : ['Griffin', random.randrange(15,20), random.randrange(6,8), random.randrange(15,20)],
            Kraken : ['Kraken', random.randrange(20,25), random.randrange(7,10), random.randrange(20,25)],
            Hydra : ['Hydra', random.randrange(20,50), random.randrange(9,12), random.randrange(20,50)],
            MythicGriffin : ['Mythic Griffin', random.randrange(95,121), random.randrange(13,16), random.randrange(95,121)],
            TartCat : ['Tart-cat', random.randrange(10,125), random.randrange(5,20), random.randrange(10,125)],
            Celestial : ['Celestial Dragon', random.randrange(123,130), random.randrange(15,26), random.randrange(123,130)]
        }
        user = User.objects.get(id = data['user'])
        for key in pets:
            if pets[key][0] == data['pet']:
                pet = key.objects.create(
                    user = user, 
                    max_health = pets[key][1],
                    health = round(pets[key][1]/2),
                    max_energy = pets[key][2],
                    energy = pets[key][2],
                    happiness = round(pets[key][3]/2),
                    max_happiness = pets[key][3],
                    )
                return pet

    @classmethod
    def stat_time(cls, id):
        data = cls.objects.filter(user_id = id)
        for i in range(len(data)):
            p = data[i]
            t = datetime.utcnow() - datetime.combine(p.updated_at.date(), p.updated_at.time())
            if math.floor(t.seconds/900) > 0:
                p.happiness -= 2
                if p.happiness < -4:
                    p.delete()
                p.energy = p.max_energy
                p.save()
        return True

    @staticmethod
    def levelup(data):
        data.level += 1
        if data.level > 10:
            data.level = 10
        data.xp_to_lvl += 6
        data.experience = 0
        data.max_health += 5
        data.health = data.max_health
        data.max_energy += 1
        data.energy = data.max_energy
        data.max_happiness += 1
        data.happiness = data.max_happiness
        data.save()
        return 'level'

    @classmethod
    def play(cls, id):
        pet = cls.objects.filter(id = id).select_subclasses()
        pet = pet[0]
        
        if pet.energy == 0:
            return False
        pet.experience += 1
        if pet.experience >= pet.xp_to_lvl:
            return cls.levelup(pet)
        pet.happiness += 1
        if pet.happiness > pet.max_happiness:
            pet.happiness = pet.max_happiness
        pet.health += 1
        if pet.health > pet.max_health:
            pet.health = pet.max_health
        if pet.energy > 0 :
            pet.energy -= 1
        else:
            pet.energy = 0
        pet.save()
        return True

    @classmethod
    def train(cls, id):
        pet = cls.objects.filter(id = id).select_subclasses()
        pet = pet[0]
        if pet.happiness < 1:
            return False
        if pet.energy == 0:
            return False
        if pet.health == 1:
            return False
        pet.experience += 3
        if pet.experience >= pet.xp_to_lvl:
            return cls.levelup(pet)
        pet.happiness -= 1
        pet.energy -= 1
        pet.health -= 1
        pet.save()
        return True
    
    @staticmethod
    def pet_randomizer():
        options = []
        for i in range (3):
            gen = random.randrange(1,201)
            if gen > 149:
                sel = random.randrange(0,2)
                if sel == 0:
                    options.append(['Glorb', 'pets/css/images/glorb-avatar.png'])
                else:
                    options.append(['Snek', 'pets/css/images/snek-avatar.png'])
            elif gen > 109:
                options.append(['Green Dragon', 'pets/css/images/green-dragon-avatar.png'])
            elif gen > 79:
                options.append(['Cat-siren', 'pets/css/images/cat-siren-avatar.png'])
            elif gen > 54:
                options.append(['Red Dragon', 'pets/css/images/red-dragon-avatar.png'])
            elif gen > 34:
                sel = random.randrange(0,2)
                if sel == 0:
                    options.append(['Moogle', 'pets/css/images/moogle-avatar.png'])
                else:
                    options.append(['Griffin', 'pets/css/images/griffin-avatar.png'])
            elif gen > 19:
                options.append(['Kraken', 'pets/css/images/kraken-avatar.png'])
            elif gen > 9:
                options.append(['Hydra', 'pets/css/images/hydra-avatar.png'])
            elif gen > 4:
                options.append(['Mythic Griffin', 'pets/css/images/mythic-griffin-avatar.png'])
            elif gen >= 2:
                options.append(['Tart-cat', 'pets/css/images/tart-cat-avatar.png'])
            elif gen == 1:
                options.append(['Celestial Dragon', 'pets/css/images/celestial-dragon-avatar.png'])
        return options

class Glorb(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/glorb.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/glorb-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Glorb', editable=False)
    experience = models.IntegerField(default=5)
    xp_to_lvl = models.IntegerField(default=10)

class Snek(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/snek.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/snek-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Snek', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=10)

class GreenDragon(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/green-dragon.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/green-dragon-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Green Dragon', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=10)

class Siren(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/cat-siren.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/cat-siren-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Cat-siren', editable=False)
    experience = models.IntegerField(default=9)
    xp_to_lvl = models.IntegerField(default=10)

class RedDragon(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/red-dragon.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/red-dragon-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Red Dragon', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=10)

class Moogle(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/moogle.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/moogle-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Moogle', editable=False)
    experience = models.IntegerField(default=5)
    xp_to_lvl = models.IntegerField(default=12)

class Griffin(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/griffin.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/griffin-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Griffin', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=15)

class Kraken(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/kraken.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/kraken-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Kraken', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=25)

class Hydra(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/hydra.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/hydra-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Hydra', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=40)

class MythicGriffin(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/mythic-griffin.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/mythic-griffin-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Mythic Griffin', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=50)

class TartCat(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/tart-cat.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/tart-cat-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Tart-cat', editable=False)
    experience = models.IntegerField(default=9)
    xp_to_lvl = models.IntegerField(default=10)

class Celestial(Pet):
    image = models.CharField(max_length=150, default= 'pets/css/images/celestial-dragon.png', editable=False)
    avatar = models.CharField(max_length=150, default= 'pets/css/images/celestial-dragon-avatar.png', editable=False)
    pet_type = models.CharField(max_length=45, default='Celestial Dragon', editable=False)
    experience = models.IntegerField(default=0)
    xp_to_lvl = models.IntegerField(default=120)