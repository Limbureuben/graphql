import graphene
from myapp.models import *
from app_dtos.app import EmploymentObject





# class EmploymentBuilders:
#     def get_employment_data(id):
#         if (id):
#             employment = Employment.objects.filter(unique_id=id).first()
            
#             if employment:
#                 return EmploymentObject (
#                     id = employment.id,
#                     unique_id = employment.unique_id,
#                     job_title = employment.job_title,
#                     employ_status = employment.employ_status,
#                     details_month = employment.details_month,
#                     employ_name = employment.employ_name
#                 )
                
#             else:
#                 EmploymentObject()
            
#         else:
#             EmploymentObject()


class EmploymentBuilders:
    @staticmethod
    def get_employment_data(unique_id=None):
        if unique_id:
            employment = Employment.objects.filter(unique_id=unique_id).first()
            print(employment)
            
            if employment:
                return EmploymentObject(
                    unique_id=employment.unique_id,
                    job_title=employment.job_title,
                    employ_status=employment.employ_status,
                    details_month=employment.details_month,
                    employ_name=employment.employ_name
                )
                
        # Return None or raise an exception if employment is not found
            else:
                EmploymentObject()
        else:
            EmploymentObject()
