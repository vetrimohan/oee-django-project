
from .models import ProductionLog

def calculate_oee_for_machine(machine, available_time, unplanned_downtime, ideal_cycle_time, available_operating_time):
    production_logs = ProductionLog.objects.filter(machine=machine)
    total_good_products = sum(log.good_products for log in production_logs)
    total_bad_products = sum(log.total_products - log.good_products for log in production_logs)
    total_products = sum(log.total_products for log in production_logs)
    
    availability = (available_time - unplanned_downtime) / available_time  # Implement this calculation
    performance = (ideal_cycle_time * total_good_products) / available_operating_time  # Implement this calculation
    quality = total_good_products / total_products
    oee = availability * performance * quality * 100
    
    return oee
