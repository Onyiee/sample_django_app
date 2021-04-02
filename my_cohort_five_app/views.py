from django.shortcuts import render


# Create your views here.

def display_image(request):
    return render(request, "index.html")


def more_images(request):
    context = {
        "img1": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt7KoLigUHqfXKVxdrQUi9dDtUZVqxyxEN-A&usqp=CAU",
        "img2": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvfD7XlM7k6b2h-yYwwvBImLpfYXD4Z5tMhA&usqp=CAU",
        "img3": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvYxLV9uIBI7GjLhZhzvL-LfidKyYfFeGA2g&usqp=CAU"
    }
    return render(request, "home.html", context)
