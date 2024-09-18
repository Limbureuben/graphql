import graphene
from myapp.models import *








# class EmploymentInputObject(graphene.InputObjectType):
#     job_title = graphene.String()
#     employ_status = graphene.String()
#     details_month = graphene.String()
#     employ_name = graphene.String()
    
# class EmploymentObject(graphene.ObjectType):
#     id = graphene.String()
#     unique_id = graphene.ID()
#     job_title = graphene.String()
#     employ_status = graphene.String()
#     details_month = graphene.String()
#     employ_name = graphene.String()
    

class EmploymentInputObject(graphene.InputObjectType):
    job_title = graphene.String()
    employ_status = graphene.String()
    details_month = graphene.String()
    employ_name = graphene.String()

class EmploymentObject(graphene.ObjectType):
    unique_id = graphene.UUID()  # Use ID for UUID fields
    job_title = graphene.String()
    employ_status = graphene.String()
    details_month = graphene.String()
    employ_name = graphene.String()
    is_active =graphene.Boolean()