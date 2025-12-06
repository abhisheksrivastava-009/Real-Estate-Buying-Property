from django.db import models

# Create your models here.

class EmployeeData(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_pwd = models.CharField(max_length=20)
    emp_email = models.EmailField(max_length=20)
    emp_mob = models.BigIntegerField()
    emp_dept=models.CharField(max_length=8 ,null=True)
    emp_dob= models.DateField(null=True)
    emp_img= models.ImageField(upload_to='uploadedFiles',null=True)



class EmployeeData2(models.Model):
    emp_first_name =models.CharField(max_length=20)
    emp_last_name =models.CharField(max_length=20)
    emp_email = models.EmailField(max_length=20)
    emp_mob = models.BigIntegerField(max_length=10)
    emp_queire =models.TextField(max_length=200)


# class ContactMessage(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name  = models.CharField(max_length=100, blank=True)
#     email      = models.EmailField()
#     phone      = models.CharField(max_length=20, blank=True)
#     message    = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} — {self.email}"


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    query = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"






