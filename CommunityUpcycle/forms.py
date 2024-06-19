from django import forms
from .models import CommunityUpcycleListing

class CommunityUpcycleListingForm(forms.ModelForm):
  class Meta:
    model = CommunityUpcycleListing
    fields = ['title', 'description', 'category', 'image', 'location']  # Adjust fields as needed

  def clean_title(self):
    # Optional: Add validation logic for the title field (e.g., minimum length)
    title = self.cleaned_data['title']
    if len(title) < 5:
      raise forms.ValidationError('Title must be at least 5 characters long.')
    return title
