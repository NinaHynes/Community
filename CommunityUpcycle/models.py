from django.db import models
from django.contrib.gis.db import models as gis_models



class CommunityUpcycleListing(models.Model):
  title = models.CharField(max_length=200)  # Title of the listing (item)
  description = models.TextField()  # Detailed description of the item
  category = models.CharField(max_length=100, blank=True)  # Optional category (e.g., clothes, furniture)
  image = models.ImageField(upload_to='communityupcycle_images/', blank=True)  # Optional image for the listing
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # User who created the listing
  created_date = models.DateTimeField(auto_now_add=True)  # Date the listing was created
  location = gis_models.PointField(blank=True, null=True)  # Optional location of the item (consider using a library like geodjango for advanced location features)

  def __str__(self):
    return self.title

