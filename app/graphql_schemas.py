import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from app.models import User 


class UserObject(SQLAlchemyObjectType):
    id = graphene.Int()
    email = graphene.String()
    class Meta:
        model = User

class UserAll(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
        
class UserConnection(relay.Connection):
    class Meta:
        node = UserAll

class Query(graphene.ObjectType):
    #node = relay.Node.Field()
    
    all_users = SQLAlchemyConnectionField(UserConnection)
    
    #all_users = graphene.List(UserObject)
    
    # def resolve_all_users(self,info,**kwargs):
    #     query = UserObject.get_query(info)
    #     return query.all()
        
    user = graphene.Field(UserObject,
        id=graphene.Int(),
        email=graphene.String())
    
    def resolve_user(self,info,*args,**kwargs):
        query = UserObject.get_query(info)
        query = query.filter_by(**kwargs)
        return query.first()

schema = graphene.Schema(query=Query)