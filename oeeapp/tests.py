from django.test import TestCase
from .models import ProductionLog

class OEECalculationTestCase(TestCase):
    def test_oee_calculation(self):
        production_log = ProductionLog.objects.create(
            cycle_no="CN001",
            unique_id="123456",
            material_name="Product X",
            machine=None,
            start_time="2024-04-18 08:00:00",
            end_time="2024-04-18 10:00:00",
            duration=2.0,
            ideal_cycle_time=0.0833,
            actual_output=100,
            good_products=90,
            total_products=110
        )

        # Calculate OEE
        oee = production_log.calculate_oee()

        # Check if OEE is within an acceptable range
        self.assertTrue(0 <= oee <= 100)  # Ensure OEE is between 0 and 100
