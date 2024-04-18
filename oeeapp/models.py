from django.db import models

class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class ProductionLog(models.Model):
    cycle_no = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=50)
    material_name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()  # Duration in hours
    ideal_cycle_time = models.FloatField()  # Ideal cycle time in hours
    actual_output = models.IntegerField()   # Actual output
    good_products = models.IntegerField()   # Number of good products
    total_products = models.IntegerField()  # Total number of products produced

    def calculate_oee(self):
        # Availability calculation
        available_time = 24 * 3  # 3 shifts of 8 hours each
        available_operating_time = self.total_products * self.ideal_cycle_time
        unplanned_downtime = available_time - available_operating_time
        availability = (available_time - unplanned_downtime) / available_time

        # Performance calculation
        performance = (self.ideal_cycle_time * self.actual_output) / available_operating_time

        # Quality calculation
        quality = (self.good_products / self.total_products)

        # OEE calculation
        oee = availability * performance * quality * 100
        return oee
    def save(self, *args, **kwargs):
        self.oee = self.calculate_oee()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.cycle_no} - {self.material_name}"
