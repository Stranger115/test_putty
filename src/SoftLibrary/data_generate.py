from faker import Faker
_faker = Faker('zh_CN')


class DataGenerate:

    def enter_message(self, data: dict):
        """获取ssh测试数据"""
        operation = {key: ['', *data[key], 'enter'] for key in data}
        return operation

    def get_url(self):
        name = _faker.domain_name()
        return name
