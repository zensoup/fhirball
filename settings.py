#
# Database
#
SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://CS_CARE3:CS_CARE3@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=192.168.1.96)(Port=1521))(CONNECT_DATA=(SID=orcl)))'

SQLALCHEMY_CONFIG = {
  'URI': 'oracle+cx_oracle://CS_CARE3:CS_CARE3@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=192.168.1.96)(Port=1521))(CONNECT_DATA=(SID=orcl)))',
  'BASE_CLASS': 'main.Base',
}

#
# Search
#
DEFAULT_BUNDLE_SIZE = 20
MAX_BUNDLE_SIZE = 100
