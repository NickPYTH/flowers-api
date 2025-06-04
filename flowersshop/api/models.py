from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    opening_hours = models.CharField(max_length=100, verbose_name='Время открытия')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.address)


class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class Employee(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, verbose_name='Торговая точка')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    second_name = models.CharField(max_length=100, verbose_name='Отчество')
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name='Должность')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    tg = models.CharField(max_length=100, verbose_name='Телеграмм')
    mail = models.CharField(max_length=100, verbose_name='Почта')
    hire_date = models.DateField(verbose_name='Дата найма')
    fire_date = models.DateField(verbose_name='Дата увольнения')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = "Работники"

    def __str__(self):
        return '{0} {1} {2} - {3}'.format(self.first_name, self.last_name, self.second_name, self.post.name)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='Доступен')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.category.name)


class Inventory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, verbose_name='Торговая точка')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кол-во товара')

    class Meta:
        verbose_name = 'Наличие товара в магазине'
        verbose_name_plural = "Наличие товара в магазине"

    def __str__(self):
        return '{0} - {1}'.format(self.shop.name, self.product.name)


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    second_name = models.CharField(max_length=100, verbose_name='Отчество')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    tg = models.CharField(max_length=100, verbose_name='Телеграмм')
    note = models.TextField(verbose_name='Примечание')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.phone)


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = "Статусы заказа"

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Вид оплаты'
        verbose_name_plural = "Виды оплаты"

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name='Клиент')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, verbose_name="Торговая точка")
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, verbose_name="Работник")
    order_date = models.DateField(verbose_name='Дата создания')
    delivery_date = models.DateField(verbose_name='Дата доставки')
    delivery_address = models.CharField(max_length=100, verbose_name='Адрес доставки')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус')
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING, verbose_name='Вид оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    note = models.TextField(verbose_name="Примечание")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.shop.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кол-во')
    discount = models.FloatField(verbose_name='Скидка')
    subtotal = models.FloatField(verbose_name='Промежуточная сумма')
    note = models.TextField(verbose_name="Примечание")

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = "Элементы заказов"

    def __str__(self):
        return '{0} {1} {2}'.format(self.order.shop.name, self.product.name, self.subtotal)


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    contact_person = models.CharField(max_length=100, verbose_name='Контактное лицо')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    tg = models.CharField(max_length=100, verbose_name='Телеграмм')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    note = models.TextField(verbose_name='Примечание')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.contact_person, self.phone_number)


class Delivery(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, verbose_name='Поставщик')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, verbose_name="Торговая точка")
    delivery_date = models.DateField(verbose_name='Дата поставки')
    total_cost = models.FloatField(verbose_name='Итоговая сумма')
    note = models.TextField(verbose_name='Примечание')

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = "Поставки"

    def __str__(self):
        return '{0} {1} {2}'.format(self.supplier.name, self.shop.name, self.delivery_date)


class DeliveryItem(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.DO_NOTHING, verbose_name='Поставка')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кол-во')
    unit_price = models.FloatField(verbose_name='Цена единицы')
    subtotal = models.FloatField(verbose_name='Промежуточная сумма')

    class Meta:
        verbose_name = 'Элемент поставки'
        verbose_name_plural = "Элементы поставок"

    def __str__(self):
        return '{0} {1} {2}'.format(self.delivery.delivery_date, self.product.name, self.quantity)


