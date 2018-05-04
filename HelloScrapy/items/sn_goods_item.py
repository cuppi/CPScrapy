
from scrapy import Item, Field


class SNGoodsItem(Item):
    # 0
    inventory: str = Field()
    # CPU升级至1.8GHz 性能更强劲 能力胜任大小事 电力满足一天所需
    aux_description: str = Field()
    # 苹果/Apple MacBook Air 13.3英寸笔记本电脑(I5 8G 128GB MQD32CH/A 银色)
    catent_desc: str = Field()
    # 627848265
    catentry_id: str = Field()
    # 46152
    count_of_article: str = Field()
    # 627848265
    part_number:str = Field()
    # 6488.0
    price: str = Field()
    # 0
    sale_status: int = Field()
    #
    contract_infos: str = Field()
    # true
    sn_flag: bool = Field()
    # false
    suning_sale: bool = Field()
    # 100%
    praise_rate: str = Field()
    # 0000000000
    sales_code: str = Field()
    # 苏宁自营
    sales_name: str = Field()
    # 0000000000
    sales_code10: str = Field()
    # 0
    beancurd_flag: str = Field()
    # 1
    goods_type: str = Field()
    # 2
    price_type: str = Field()
    # [{}, {}]
    filters: list = Field()
    # true
    filter_attr: bool = Field()
    # true
    is_fav: bool = Field()
    # false
    hwg_lable: bool = Field()
    # 0
    baoguang_hwg: str = Field()
    # //imgservice3.suning.cn/uimg1/b2c/image/7uLUHa9pIHoXTY004jW97Q==.jpg
    dynamic_img: str = Field()
    extenal_fileds: dict = Field()
    last_updated = Field()
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

    def __init__(self, args):
        print(args)
        args['inventory'] = args.pop('inventory', '')
        args['aux_description'] = args.pop('auxdescription', '')
        args['catent_desc'] = args.pop('catentdesc', '')
        args['catentry_id'] = args.pop('catentryId', '')
        args['count_of_article'] = args.pop('countOfarticle', '')
        args['part_number'] = args.pop('partnumber', '')
        args['price'] = args.pop('price', '')
        args['sale_status'] = args.pop('saleStatus', 0)
        args['contract_infos'] = args.pop('contractInfos', '')
        args['sn_flag'] = args.pop('snFlag', False)
        args['suning_sale'] = args.pop('suningSale', False)
        args['praise_rate'] = args.pop('praiseRate', '')
        args['sales_code'] = args.pop('salesCode', '')
        args['sales_name'] = args.pop('salesName', '')
        args['sales_code10'] = args.pop('salesCode10', '')
        args['beancurd_flag'] = args.pop('beancurdFlag', '')
        args['goods_type'] = args.pop('goodsType', '')
        args['price_type'] = args.pop('priceType', '')
        args['filters'] = args.pop('filters', [])
        args['filter_attr'] = args.pop('filterAttr', False)
        args['is_fav'] = args.pop('isFav', False)
        args['hwg_lable'] = args.pop('hwgLable', False)
        args['baoguang_hwg'] = args.pop('baoguangHwg', '')
        args['dynamic_img'] = args.pop('dynamicImg', '')
        args['extenal_fileds'] = args.pop('extenalFileds', {})
        
        super(SNGoodsItem, self).__init__(args)

    def serialize_field(self, field, name, value):
        return super(SNGoodsItem, self).serialize_field(field, name, value)
