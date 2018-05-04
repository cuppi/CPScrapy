
from scrapy import Item, Field


class SNGoodsItem(Item):
    # 0
    inventory: str = Field()
    # CPU升级至1.8GHz 性能更强劲 能力胜任大小事 电力满足一天所需
    auxdescription: str = Field()
    # 苹果/Apple MacBook Air 13.3英寸笔记本电脑(I5 8G 128GB MQD32CH/A 银色)
    catentdesc: str = Field()
    # 627848265
    catentryId: str = Field()
    # 46152
    countOfarticle: str = Field()
    # 627848265
    partnumber:str = Field()
    # 6488.0
    price: str = Field()
    # 0
    saleStatus: int = Field()
    #
    contractInfos: str = Field()
    # true
    snFlag: bool = Field()
    # false
    suningSale: bool = Field()
    # 100%
    praiseRate: str = Field()
    # 0000000000
    salesCode: str = Field()
    # 苏宁自营
    salesName: str = Field()
    # 0000000000
    salesCode10: str = Field()
    # 0
    beancurdFlag: str = Field()
    # 1
    goodsType: str = Field()
    # 2
    priceType: str = Field()
    # [{}, {}]
    filters: list = Field()
    # true
    filterAttr: bool = Field()
    # true
    isFav: bool = Field()
    # false
    hwgLable: bool = Field()
    # 0
    baoguangHwg: str = Field()
    # //imgservice3.suning.cn/uimg1/b2c/image/7uLUHa9pIHoXTY004jW97Q==.jpg
    dynamicImg: str = Field()
    extenalFileds: dict = Field()
    '''
    "extenalFileds": {
        "title": "苹果/Apple MacBook Air 13.3英寸笔记本电脑(I5 8G 128GB MQD32CH/A 银色)",
        "mdmGroupId": "R1502001",
        "picVersion": "2105",
        "auxdescription": "CPU升级至1.8GHz 性能更强劲 能力胜任大小事 电力满足一天所需",
        "appAttrTitle": [
            "超长续航",
            "性能更强劲"
        ],
        "attrShow": [
            {
                "attrAppValue": "其他",
                "attrId": "solr_9508_attrId",
                "attrName": "显存容量",
                "attrValue": "其他",  
                "attrValueId": "4374702",
                "sort": "85.0"
            }
        ],
        "goodType": "Z001",
        "commentShow": "4.6万+"
    }
    '''