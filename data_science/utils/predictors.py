"""
ML Model predictors for CityAssist
Simplified prediction logic for demonstration purposes
"""

import numpy as np

class AQIPredictor:
    """
    Air Quality Index prediction and health impact assessment
    """

    def __init__(self):
        self.thresholds = {
            'GOOD': 50,
            'MODERATE': 100,
            'UNHEALTHY_SENSITIVE': 150,
            'UNHEALTHY': 200,
            'VERY_UNHEALTHY': 300
        }

    def predict(self, pm25_value, zone="Zone-A"):
        """
        Predict health risk and generate personalized alert
        """
        # Determine risk level
        if pm25_value <= self.thresholds['GOOD']:
            risk_level = "GOOD"
            priority = "Low"
            probability = 0.15
            reason = f"PM2.5 levels are within safe range. Air quality is satisfactory for {zone}."
        elif pm25_value <= self.thresholds['MODERATE']:
            risk_level = "MODERATE"
            priority = "Medium"
            probability = 0.45
            reason = f"PM2.5 levels moderately elevated. Sensitive groups should consider limiting prolonged outdoor exertion in {zone}."
        elif pm25_value <= self.thresholds['UNHEALTHY_SENSITIVE']:
            risk_level = "UNHEALTHY_SENSITIVE"
            priority = "High"
            probability = 0.70
            reason = f"PM2.5 levels unhealthy for sensitive groups. Children, elderly, and people with respiratory conditions should reduce outdoor activities in {zone}."
        else:
            risk_level = "HIGH"
            priority = "Critical"
            probability = 0.90
            reason = f"PM2.5 levels dangerously high. All residents in {zone} should avoid outdoor activities and use air purifiers indoors."

        return {
            'risk_level': risk_level,
            'priority': priority,
            'probability': probability,
            'reason': reason,
            'pm25': pm25_value,
            'model': 'XGBoost-Classifier-v1.2'
        }

class OutagePredictor:
    """
    Utility outage restoration time prediction
    """

    def __init__(self):
        # Base restoration times by cause (in hours)
        self.base_times = {
            'Equipment Failure': 4.5,
            'Weather': 6.0,
            'Overload': 3.0,
            'Maintenance': 2.5
        }

        # Zone complexity factors
        self.zone_factors = {
            'Zone-A': 1.3,  # Downtown - complex
            'Zone-B': 1.5,  # Industrial - very complex
            'Zone-C': 1.0,  # Residential - standard
            'Zone-D': 0.8   # Suburban - simpler
        }

        # Weather impact factors
        self.weather_factors = {
            'Clear': 0.0,
            'Rain': 0.5,
            'Storm': 1.5,
            'Snow': 2.0
        }

    def predict(self, cause, zone, weather="Clear"):
        """
        Predict restoration ETA based on outage characteristics
        """
        base_time = self.base_times.get(cause, 4.0)
        zone_factor = (self.zone_factors.get(zone, 1.0) - 1.0) * base_time
        weather_factor = self.weather_factors.get(weather, 0.0)

        eta_hours = base_time + zone_factor + weather_factor

        # Add some realistic variance
        eta_hours += np.random.uniform(-0.5, 0.5)
        eta_hours = max(eta_hours, 0.5)  # Minimum 30 minutes

        # Confidence based on cause predictability
        confidence = 0.85 if cause in self.base_times else 0.70

        return {
            'eta_hours': eta_hours,
            'confidence': confidence,
            'base_time': base_time,
            'zone_factor': zone_factor,
            'weather_factor': weather_factor,
            'model': 'LightGBM-Regressor-v2.0'
        }

class ImageClassifier:
    """
    Civic report image classification
    """

    def __init__(self):
        self.categories = ["Pothole", "Garbage", "Tree Fall", "Streetlight", "Water Leak"]
        self.actions = {
            "Pothole": "Dispatch road maintenance crew. Estimated fix time: 2-4 hours.",
            "Garbage": "Schedule waste collection pickup. Estimated response: 4-6 hours.",
            "Tree Fall": "Emergency tree removal required. Crew dispatched immediately.",
            "Streetlight": "Electrical team notified. Repair within 24 hours.",
            "Water Leak": "Plumbing emergency team dispatched. ETA: 1-2 hours."
        }

    def classify(self):
        """
        Classify uploaded civic report image
        In production, this would use a CNN model (MobileNetV2)
        """
        # Simulate classification result
        category = np.random.choice(self.categories, p=[0.4, 0.25, 0.15, 0.12, 0.08])
        confidence = np.random.uniform(0.85, 0.98)

        # Priority based on category
        if category in ["Pothole", "Tree Fall", "Water Leak"]:
            priority = "High"
        elif category == "Streetlight":
            priority = "Medium"
        else:
            priority = "Low"

        return {
            'label': category,
            'confidence': confidence,
            'priority': priority,
            'action': self.actions[category],
            'model': 'MobileNetV2-Fine-Tuned'
        }

class RouteOptimizer:
    """
    Traffic-aware route optimization
    """

    def __init__(self):
        self.routes_db = {
            ('Downtown', 'Airport'): [
                {'route': 'Main St → Highway 101 → Airport Rd', 'base_time': 32, 'distance': 25},
                {'route': 'Broadway → Ring Road → Airport Rd', 'base_time': 38, 'distance': 28},
                {'route': 'Downtown Direct', 'base_time': 35, 'distance': 22}
            ]
        }

    def get_best_route(self, origin, destination, time_of_day):
        """
        Return optimal route based on predicted traffic
        """
        routes = self.routes_db.get((origin, destination), [])

        if not routes:
            return None

        # Apply time-based traffic multiplier
        if 7 <= time_of_day <= 9 or 17 <= time_of_day <= 19:
            traffic_multiplier = 1.4
        else:
            traffic_multiplier = 1.1

        best_route = routes[0]
        best_route['adjusted_time'] = best_route['base_time'] * traffic_multiplier

        return best_route
