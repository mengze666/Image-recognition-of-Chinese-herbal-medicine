# models.py ：模型，数据库

from .exts import db, cache


class Medicine(db.Model):
    __tablename__ = 't_medicine'
    # 药材编号
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   comment='药材编号')
    # 药材拼音
    pinyin = db.Column(db.String(30),
                       unique=True,
                       index=True,
                       comment='药材拼音')
    # 药材中文名
    chinese = db.Column(db.String(80),
                        unique=True,
                        index=True,
                        comment='药材中文名')
    # 药材拉丁名
    latin = db.Column(db.Text,
                      comment='药材拉丁名')
    # 药材英文名
    english = db.Column(db.Text,
                        comment='药材英文名')
    # 科
    family = db.Column(db.String(50),
                       comment='科')
    # 产地
    habitat = db.Column(db.Text,
                        comment='产地')
    # 采集时间
    collection_time = db.Column(db.Text,
                                comment='采集时间')
    # 药用部位
    use_part = db.Column(db.String(30),
                         comment='药用部位')
    # 中药材类别（按功效划分）
    efficacy_class = db.Column(db.String(30),
                               comment='中药材类别（按功效划分）')
    # 性
    property = db.Column(db.String(30),
                         comment='性')
    # 味
    flavor = db.Column(db.String(30),
                       comment='味')
    # 归经
    meridian_tropism = db.Column(db.String(50),
                                 comment='归经')
    # 功效
    indications = db.Column(db.Text,
                            comment='功效')
    # 性状
    appearance = db.Column(db.Text,
                           comment='性状')
    # 规格
    specification = db.Column(db.Text,
                              comment='规格')
