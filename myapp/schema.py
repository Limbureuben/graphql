import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import graphql_jwt
from .models import *


############################GRAPHQL TYPES#########################
# Define GraphQL Types
class RegistrationType(DjangoObjectType):
    class Meta:
        model = Registration
        fields = ('id', 'username', 'email')

        
class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application
        fields = ('id', 'username', 'email', 'region', 'phone_number', 'application_date')
        
        
        
##############################INPUT TYPES FOR CREATING ENTINTIES#########################

class CreateRegistrationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UpdateRegistrationInput(graphene.InputObjectType):
     id = graphene.ID(required=True)
     username = graphene.String(required=True)
     email = graphene.String(required=True)
    
class CreateApplicationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    region = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    

# Input Type for Login
class LoginInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    
class AdminInput(graphene.InputObjectType):  # Fixed typo here
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    
class CreateEmployment(graphene.InputObjectType):
    job_title = graphene.String(required=True)
    employ_status = graphene.String(required=True)
    details_month = graphene.String(required=True)
    employ_name = graphene.String(required=True)
    
    
#####################################CREATE MUTATIONS###############################

class CreateRegistrationMutation(graphene.Mutation):
    class Arguments:
        input = CreateRegistrationInput(required=True)
        
    registration = graphene.Field(RegistrationType)
    
    def mutate(self, info, input):
        registration = Registration.objects.create(
            username=input.username,
            email=input.email,
            password=make_password(input.password)
        )
        return CreateRegistrationMutation(registration=registration)


class CreateApplicationMutation(graphene.Mutation):
    class Arguments:
        input = CreateApplicationInput(required=True)
        
    application = graphene.Field(ApplicationType)
        
    def mutate(self, info, input):
        application = Application.objects.create(
                username = input.username,
                email = input.email,
                region = input.region,
                phone_number = input.phone_number
            )
        return CreateApplicationMutation(application=application)


#########################UPDATE MUTATIONS ###############################

class UpdateRegistration(graphene.Mutation):
    class Arguments:
        input = UpdateRegistrationInput(required=True)
        
    success = graphene.Boolean()
    message = graphene.String()
    
    @staticmethod
    def mutate(root, info, input):
        registration = Registration.objects.get(username=input.username)
        
        if 'email' in input:
            registration.email = input.email
            
        registration.save()
        
        return UpdateRegistration(success=True, message="User update successfully!!")


# class UpdateRegistration(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         username = graphene.String()
#         email = graphene.String()
        
#     registration = graphene.Field(RegistrationType)
    
#     def mutate(self, info, id, username=None, email=None):
#         try:
#             registration = Registration.objects.get(pk=id)
            
#         except Registration.DoesNotExist:
#             raise Exception("User not found")
        
#         if username:
#             Registration.username = username
            
#         if email:
#             Registration.email = email
            
#         Registration.save()
#         return UpdateRegistration(registration=registration)
        
        
    
        


###########################DELETE MUTATIONS #############################

class DeleteRegistrationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        try:
            registration = Registration.objects.get(pk=id)
            registration.delete()
            return DeleteRegistrationMutation(success=True)
        except Registration.DoesNotExist:
            return DeleteRegistrationMutation(success=False)


#########################LOGIN MUTATIONS#######################

# Login Mutation here
class LoginMutation(graphene.Mutation):
    class Arguments:
        input = LoginInput(required=True)
        
    success = graphene.Boolean()
    user_id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, input):
        try:
            # Retrieve user from Registration model
            registration = Registration.objects.get(username=input.username)
        except Registration.DoesNotExist:
            return LoginMutation(success=False, user_id=None)

        # Verify password
        if not check_password(input.password, registration.password):
            return LoginMutation(success=False, user_id=None)

        # If authentication is successful
        # Store user_id in the session or token for further requests
        info.context.session['user_id'] = registration.id
        return LoginMutation(success=True, user_id=registration.id)
    
class AdminMutation(graphene.Mutation):
    class Arguments:
        input = AdminInput(required=True)
        
    success = graphene.Boolean()
    user_id = graphene.ID()
    
    @classmethod
    def mutate(cls, root, info, input):
        try:
            user = User.objects.get(username=input.username)
        except User.DoesNotExist:
            return AdminMutation(success=False, user_id=None)

        if not check_password(input.password, user.password):
            return AdminMutation(success=False, user_id=None)

        info.context.session['user_id'] = user.id
        return AdminMutation(success=True, user_id=user.id)



###############################QUERIES##########################
# Queries for Registration
class RegistrationQuery(graphene.ObjectType):
    all_registrations = graphene.List(RegistrationType)
    registration = graphene.Field(RegistrationType, id=graphene.Int(required=True))

    def resolve_all_registrations(self, info):
        return Registration.objects.all()
    
    def resolve_registration(self, info, id):
        return Registration.objects.get(pk=id)


# Mutation class for all mutations
class Mutation(graphene.ObjectType):
    create_registration = CreateRegistrationMutation.Field()
    delete_registration = DeleteRegistrationMutation.Field()
    create_application = CreateApplicationMutation.Field()
    update_registration=UpdateRegistration.Field()
    login = LoginMutation.Field()
    admin_login = AdminMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    

    

# Query class for all queries
class Query(RegistrationQuery,graphene.ObjectType):
    pass

# Define the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
