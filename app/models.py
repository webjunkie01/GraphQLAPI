from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    orm,
    MetaData,
    Table,
    DateTime,
    LargeBinary,
    ForeignKey,
    Table,
    Boolean,
    func,
    String,
    BigInteger,
    Numeric,
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.properties import ColumnProperty
import datetime
from sqlalchemy.dialects.postgresql import JSONB, DOUBLE_PRECISION, UUID
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    mapper,
    relation,
    backref,
    synonym,
    column_property,
    relationship
    )
from .meta import Base

from cryptacular import bcrypt


crypt = bcrypt.BCRYPTPasswordManager()

class CaseInsensitiveComparator(ColumnProperty.Comparator):
    "A case-insensitive SQLAlchemy comparator for unicode columns"

    def __eq__(self, other):
        "Return True if the lowercase of both columns are equal"
        return func.lower(self.__clause_element__()) == func.lower(other)


class BasicMixin(object):
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow, server_default="now")
    
class User(Base, BasicMixin):
    __tablename__ = "users"
    email = column_property(
        Column(Text, unique=True, nullable=False),
        comparator_factory=CaseInsensitiveComparator,
    )
    password_ = Column("password", LargeBinary(60), nullable=False)
    
    def check(self, password):
        "Return True if we have a matching password"
        # encoded_pwd = crypt.encode(self.password)
        # raise Exception(crypt.check(encoded_pwd, password), encoded_pwd, password)
        # return crypt.check(encoded_pwd, password)
        print("Password", self.password, password)
        return crypt.check(self.password.decode('utf-8'), password)
        
    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, password):
        self.password_ = bytes(crypt.encode(password), "utf-8")

    password = synonym("password_", descriptor=password)
    login_date = Column(
        DateTime, default=datetime.datetime.utcnow, server_default="now"
    )
    device_token = Column(Text)
    device_id = Column(Text)
    is_active = Column(Boolean, server_default="TRUE", default=True, nullable=False)

    

