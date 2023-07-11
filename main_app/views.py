from django.shortcuts import render

#baby step-usually on a model
finches = [
    {'name': 'House Finch', 'habitat': 'Live throughout most of the United States', 'description': 'Small-size bird, large beak, rosey red feathers with streaky brown backs', 'diet': 'Seeds, buds, berries'},
    {'name': 'American GoldFinch', 'habitat': 'Live mostly of Northern United States', 'description': 'Small bird with bright yellow plumage, a black forehead, and black wings', 'diet': 'Seeds and insects'},
    {'name': 'Black Rosy Finch', 'habitat': 'Live in the mountains of the western United States', 'description': 'Medium-size bird with black plumages and pink highlights', 'diet': 'Seeds and insects'},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
