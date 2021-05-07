from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Image, Product
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    PRODUCT_IMAGES_URLS = []
    product_name = ''
    product_price = 0
    images = Image.query.filter(Image.url.endswith('.jpg')).all()
    for image in images:
        product_id = image.productId
        product = Product.query.filter_by(id=product_id).first()
        if(product):
            product_name = product.name
            product_price = product.price
            img_url = image.url
            if "public" in img_url:
                PRODUCT_IMAGES_URLS.append(
                    'static/img/' + str(product.userId) + '/' + img_url)
            elif current_user.is_authenticated and product.userId == current_user.id:
                PRODUCT_IMAGES_URLS.append(
                    'static/img/' + str(product.userId) + '/' + img_url)

    return render_template('index.html', PRODUCT_IMAGES_URLS=PRODUCT_IMAGES_URLS, PRODUCT_NAME=product_name, PRODUCT_PRICE=product_price)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
