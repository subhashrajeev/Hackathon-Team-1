"""
Data generators for CityAssist dashboard demonstrations
Generates realistic synthetic data for various smart city scenarios
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_aqi_data(zone="Zone-A", days=7):
    """
    Generate Air Quality Index time-series data
    """
    np.random.seed(42)

    # Base pollution levels by zone
    zone_base = {
        "Zone-A": 80,  # Downtown - higher pollution
        "Zone-B": 120,  # Industrial - highest
        "Zone-C": 50,  # Residential - moderate
        "Zone-D": 30   # Suburban - lowest
    }

    base_level = zone_base.get(zone, 70)

    # Generate hourly data
    hours = days * 24
    timestamps = [datetime.now() - timedelta(hours=hours-i) for i in range(hours)]

    # Simulate daily patterns with noise
    hour_of_day = np.array([ts.hour for ts in timestamps])
    pm25 = base_level + 20 * np.sin(2 * np.pi * hour_of_day / 24) + np.random.normal(0, 10, hours)
    pm25 = np.maximum(pm25, 10)  # Ensure positive values

    pm10 = pm25 * 1.5 + np.random.normal(0, 5, hours)
    pm10 = np.maximum(pm10, 15)

    aqi_data = pd.DataFrame({
        'timestamp': timestamps,
        'pm25': pm25,
        'pm10': pm10,
        'zone': zone,
        'hour': hour_of_day
    })

    return aqi_data

def generate_outage_data(num_outages=15):
    """
    Generate utility outage records
    """
    np.random.seed(42)

    zones = ["Zone-A", "Zone-B", "Zone-C", "Zone-D"]
    causes = ["Equipment Failure", "Weather", "Overload", "Maintenance", "Unknown"]
    statuses = ["Active", "In Progress", "Resolved"]

    outages = []
    for i in range(num_outages):
        reported_time = datetime.now() - timedelta(hours=np.random.randint(1, 48))
        eta_hours = np.random.uniform(1, 12)

        outage = {
            'outage_id': f"OUT-{1000+i}",
            'zone': np.random.choice(zones),
            'cause': np.random.choice(causes, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
            'reported_time': reported_time.strftime("%Y-%m-%d %H:%M"),
            'predicted_eta': f"{eta_hours:.1f} hours",
            'status': np.random.choice(statuses, p=[0.4, 0.3, 0.3]),
            'affected_customers': np.random.randint(100, 5000)
        }
        outages.append(outage)

    return pd.DataFrame(outages)

def generate_traffic_data():
    """
    Generate traffic volume and congestion data
    """
    np.random.seed(42)

    routes = ["Route-1 (Main St)", "Route-2 (Highway)", "Route-3 (Downtown)", "Route-4 (Bypass)"]
    data = []

    for route in routes:
        for hour in range(24):
            # Simulate rush hour patterns
            base_congestion = 30
            if 7 <= hour <= 9 or 17 <= hour <= 19:  # Rush hours
                base_congestion = 70
            elif 10 <= hour <= 16:  # Mid-day
                base_congestion = 45

            congestion = base_congestion + np.random.normal(0, 10)
            congestion = np.clip(congestion, 0, 100)

            # Travel time based on congestion
            base_travel_time = 20 + (routes.index(route) * 5)
            travel_time = base_travel_time * (1 + congestion / 100)

            data.append({
                'route': route,
                'hour': hour,
                'congestion_level': round(congestion, 1),
                'travel_time': round(travel_time, 1),
                'volume': int(congestion * 100 + np.random.normal(0, 500))
            })

    return pd.DataFrame(data)

def generate_civic_reports(num_reports=100):
    """
    Generate civic report classification data
    """
    np.random.seed(42)

    categories = ["Pothole", "Garbage", "Tree Fall", "Streetlight", "Other"]
    zones = ["Zone-A", "Zone-B", "Zone-C", "Zone-D"]
    priorities = ["High", "Medium", "Low"]

    reports = []
    for i in range(num_reports):
        category = np.random.choice(categories, p=[0.35, 0.25, 0.15, 0.15, 0.10])
        confidence = np.random.uniform(0.75, 0.98)

        # Priority based on category
        if category in ["Pothole", "Tree Fall"]:
            priority = np.random.choice(priorities, p=[0.7, 0.2, 0.1])
        else:
            priority = np.random.choice(priorities, p=[0.2, 0.5, 0.3])

        report = {
            'report_id': f"RPT-{2000+i}",
            'category': category,
            'confidence': confidence,
            'priority': priority,
            'zone': np.random.choice(zones),
            'timestamp': (datetime.now() - timedelta(hours=np.random.randint(1, 168))).strftime("%Y-%m-%d %H:%M"),
            'status': np.random.choice(["Open", "In Progress", "Resolved"], p=[0.3, 0.4, 0.3])
        }
        reports.append(report)

    return pd.DataFrame(reports)
