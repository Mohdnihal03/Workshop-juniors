# from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     return render(request, 'home/index.html')

# def predict_view(request):
#     if request.method == 'POST':
#         # Extract data from form submission
#         airline = request.POST.get('airline')
#         flight = request.POST.get('flight')
#         source_city = request.POST.get('source_city')
#         departure_time = request.POST.get('departure_time')
#         stops = request.POST.get('stops')
#         arrival_time = request.POST.get('arrival_time')
#         destination_city = request.POST.get('destination_city')
#         flight_class = request.POST.get('class')
#         duration = request.POST.get('duration')
#         days_left = request.POST.get('days_left')
#         price = request.POST.get('price')
        
#         # Here, you would perform the prediction using the extracted data
#         # For demonstration, let's assume we have a dummy prediction function
#         prediction = dummy_predict(airline, flight, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left, price)
        
#         # Render the same page with the prediction result
#         return render(request, 'home/index.html', {'prediction': prediction})
#     else:
#         return HttpResponse(status=405)  # Method Not Allowed

# def dummy_predict(airline, flight, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left, price):
#     # Dummy prediction logic
#     return "Predicted Price: $300"



from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Load the ML model
MODEL_FILE_PATH = 'FlightPricePrediction/models/flight_model_decision_tree.joblib'  # Update this with the actual path
model = joblib.load(MODEL_FILE_PATH)

def home_view(request):
    return render(request, 'home/index.html')

def predict_view(request):
    if request.method == 'POST':
        # Extract form data
        airline = request.POST.get('airline')  # Assuming airline is a string
        flight = request.POST.get('flight')  # Assuming flight is a string
        source_city = request.POST.get('source_city')  # Assuming source_city is a string
        departure_time = float(request.POST.get('departure_time'))  # Assuming departure_time is a float
        stops = int(request.POST.get('stops'))  # Assuming stops is an integer
        arrival_time = float(request.POST.get('arrival_time'))  # Assuming arrival_time is a float
        destination_city = request.POST.get('destination_city')  # Assuming destination_city is a string
        flight_class = request.POST.get('class')  # Assuming class is a string
        duration = float(request.POST.get('duration'))  # Assuming duration is a float
        days_left = int(request.POST.get('days_left'))  # Assuming days_left is an integer
        # Example: create feature vector for prediction
        features = [airline, flight, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left]
        
        # Perform prediction
        predicted_price = model.predict([features])[0]

        # Render the same page with the prediction result
        return render(request, 'home/index.html', {'prediction': predicted_price})
    else:
        return HttpResponse(status=405)  # Method Not Allowed
