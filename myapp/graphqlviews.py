# import graphene
# from .models import *
# from graphene_django.types import DjangoObjectType
# from myapp_dto.setting_dto import *



# class MessageMutation(graphene.Mutation):
#     class Arguments:
#         input = MessageInput(required=True)
        
#     message = graphene.Fiel(MessageOutput)
          
#     def mutate(self, info, input):
#         message = Message.objects.create(
#                 topic = input.topic,
#                 published_date = input.published_date,
#                 text = input.text
#             )
#         return MessageMutation(message=message)