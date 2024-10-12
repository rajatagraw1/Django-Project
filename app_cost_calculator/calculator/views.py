from django.shortcuts import render
from django.http import JsonResponse

FEATURES = {
    'E-commerce': {'Product Listing': 30, 'Payment Integration': 25},
    'Social Media': {'User Profiles': 30, 'Chat System': 40},
    'Cloud Kitchen': {'Menu Display': 25, 'Online Ordering': 40},
}

def index(request):
    return render(request, 'index.html')

def calculate_cost(request):
    category = request.GET.get('category')
    selected_features = request.GET.getlist('features[]')

    if not category or not selected_features:
        return JsonResponse({'error': 'Please select a category and at least one feature.'}, status=400)

    total_hours = sum([FEATURES[category].get(feature, 0) for feature in selected_features])
    total_cost = total_hours * 10  # Hourly rate is $10

    return JsonResponse({'total_cost': total_cost})