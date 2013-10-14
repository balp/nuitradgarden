#!/usr/bin/python
# vim: set fileencoding=utf-8 :
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from plants.models import Grupp, Sort, Plant

import datetime

class PlantListor(TestCase):
    
    def test_index_should_need_login(self):
        self.url = reverse("plants:index")
        page = self.client.get(self.url)
        self.assertRedirects(page, "accounts/login/?next=%s" % self.url)
        
class PlantListorLoggedIn(TestCase):
    def setUp(self):
        self.url = reverse("plants:index")
        user = User.objects.create_user("testuser", "test@example.com", "test")
        user.first_name = "Joe"
        user.last_name = "Tester"
        user.save()
        hh = Grupp.objects.create(name="Hösthallon", description="", grupp=None)
        ab = hh.sort_set.create(name="Rubus (Hösthallon) 'Autumn Bliss'", description="Rikligt med upprätta skott, svagt taggiga. 1-1,5 m höga. Stora mörkröda bär av god kvalitet. Mognar ända fram tills frosten kommer. Sol. Utmärkt äta direkt och bra att frysa.")
        hallon2 = hh.sort_set.create(name="Rubus (Hösthallon)", description="Hittad planta")
        hh.save()
        self.hallon_1 = Plant.objects.create(user=user, sort=ab,
                                     position="Nummer två i första raden hallon buskar.",
                                     planted=datetime.date(2013,9,15))
        self.hallon_1.save()
        plant = Plant.objects.create(user=user, sort=ab,
                                     position="Nummer ett i första raden hallon buskar.",
                                     planted=datetime.date(2013,9,16))
        plant.save()
        plant = Plant.objects.create(user=user, sort=hallon2,
                                     position="Nummer tre i första raden hallon buskar.",
                                     planted=datetime.date(2013,9,15))
        plant.save()
        tb = Grupp.objects.create(name="Träd och buskar")
        sl = tb.sort_set.create(name="Slånaronia",
                                 description="Medelstor buske med brett glest upprätt växtsätt. 2-3 m Vita blommor i maj-juni Svarta, vitaminrika bär i klasar, bra till saft, Starka höstfärger i rött och orange, Sol-halvskugga. Anspråkslösa jordkrav. Torktålig, Buskage, friväxande häck. Lätt beskärning de första åren. Kräver lätt beskärning de första åren för att få stadigare och tätare växt. Utmärkt till friväxande häck.")
        plant = Plant.objects.create(user=user, sort=sl,
                                     position="I gräsmattan, närmast björken",
                                     planted=datetime.date(2012,9,20) )
        plant.save()
        self.client.login(username="testuser", password="test")
        
    
    def test_index_shouls_have_name_of_rubus_plant(self):
        page = self.client.get(self.url)
        self.assertContains(page, "Rubus (Hösthallon) &#39;Autumn Bliss&#39;", count=2)

    def test_index_shouls_have_link_to_details(self):
        page = self.client.get(self.url)
        self.assertContains(page, "<a href=\"/plants/1/\">Rubus")
        
    def test_index_shouls_have_name_of_slanoria_plant(self):
        page = self.client.get(self.url)
        self.assertContains(page, "Slånaronia")
    def test_index_shouls_have_position_of_slanoria_plant(self):
        page = self.client.get(self.url)
        self.assertContains(page, "I gräsmattan, närmast björken")
    def test_index_shouls_have_year_of_slanoria_plant(self):
        page = self.client.get(self.url)
        self.assertContains(page, "2012")
        
    def test_view_detauls_of_rubus_have_name(self):
        details_url = reverse("plants:detail", kwargs={"pk":self.hallon_1.id})
        page = self.client.get(details_url)
        print page
        self.assertContains(page, "Rubus (Hösthallon) &#39;Autumn Bliss&#39;")
    def test_view_detauls_of_rubus_have_year(self):
        details_url = reverse("plants:detail", kwargs={"pk":self.hallon_1.id})
        page = self.client.get(details_url)
        self.assertContains(page, self.hallon_1.planted.year)
    def test_view_detauls_of_rubus_have_position(self):
        details_url = reverse("plants:detail", kwargs={"pk":self.hallon_1.id})
        page = self.client.get(details_url)
        self.assertContains(page, self.hallon_1.position)
    
    def test_view_detauls_of_rubus_have_desription(self):
        details_url = reverse("plants:detail", kwargs={"pk":self.hallon_1.id})
        page = self.client.get(details_url)
        self.assertContains(page, self.hallon_1.sort.description)
        
