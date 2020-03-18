from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


# 权限判定
# 读
READ = 1
# 赞
PRAISE = 2
# 写
WRITE = 4

class User(BaseModel, db.Model):
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(32), unique=True)
    _u_password = db.Column(db.String(256))
    is_delete = db.Column(db.Boolean, default=False)
    u_permission = db.Column(db.Integer, default=0)

    # ************ 密码安全 方式三 最优秀设计方法 *************** 4  最终选择
    @property
    def u_password(self):
        return self._u_password

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

    # 验证密码
    def verify_password(self, password):
        return check_password_hash(self._u_password, password)

    # 权限判定
    def check_permission(self, permission):
        return self.u_permission & permission == permission