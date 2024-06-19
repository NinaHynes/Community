
from django.shortcuts import render, redirect, get_object_or_404
from .models import CommunityUpcycleListing
from .forms import CommunityUpcycleListingForm  
import requests

def communityupcycle_list(request):
  listings = CommunityUpcycleListing.objects.all().order_by('-created_date')  # Get all listings, order by newest first
  return render(request, 'communityupcycle/communityupcycle_list.html', {'listings': listings})

def communityupcycle_detail(request, pk):
  listing = get_object_or_404(CommunityUpcycleListing, pk=pk)  # Get specific listing by primary key (pk)
  return render(request, 'communityupcycle/communityupcycle_detail.html', {'listing': listing})

def communityupcycle_create(request):
  if request.method == 'POST':
    # Handle form submission for creating a new listing
    form = CommunityUpcycleListingForm(request.POST, request.FILES) 
    if form.is_valid():
      form.save()
      return redirect('communityupcycle_list')  # Redirect to listing list after successful creation
  else:
    # Render the form for creating a new listing
    form = CommunityUpcycleListingForm()
  return render(request, 'communityupcycle/communityupcycle_create.html', {'form': form})

# Additional views for editing and deleting listings can be added here

