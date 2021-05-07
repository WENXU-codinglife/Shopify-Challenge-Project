import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
#from werkzeug import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Image, Product
from . import db
import imghdr

mana = Blueprint('mana', __name__)


@mana.route('/add')
@login_required
def add():
    return render_template('add.html')


@mana.route('/add', methods=['POST'])
@login_required
def add_post():
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity')
    if(quantity < 1):
        flash('Quantity must be greater than 0!')
        return redirect(url_for('mana.add'))
    price = request.form.get('price')
    if(price <= 0):
        flash('Price must be greater than 0!')
        return redirect(url_for('mana.add'))
    tag = request.form.get('tag')

    # check if the new product name already exists
    item = Product.query.filter_by(
        userId=current_user.id, name=product_name).first()
    if item:
        flash('Product name already exists.')
        return redirect(url_for('mana.add'))

    if(request.files):
        f = request.files.getlist('image')
        i = 1
        latest_product = Product.query.filter(
            Product.id > 0).order_by(Product.id.desc()).first()
        for image in f:
            if(image.filename):
                # Validate file extensions
                image_ext = os.path.splitext(image.filename)[1]
                if image_ext not in ['.jpg'] or image_ext != validate_image(image.stream):
                    flash('Only Accept JPG!')
                    return redirect(url_for('mana.add'))
                # save the uploaded images to the directory
                # the images will be saved with automatically generated names rather than their filenames
                UPLOADS_PATH = os.path.join(mana.root_path, 'static/img/')
                privacy = request.form.get('image_checkbox_'+str(i))
                if(privacy):
                    image.save(os.path.join(UPLOADS_PATH, str(
                        current_user.id)+'/private/'+product_name+'_'+str(i)+'.jpg'))
                    url = 'private/'+product_name+'_'+str(i)+'.jpg'
                else:
                    image.save(os.path.join(UPLOADS_PATH, str(
                        current_user.id)+'/public/'+product_name+'_'+str(i)+'.jpg'))
                    url = 'public/'+product_name+'_'+str(i)+'.jpg'
                    # f.save(secure_filename(f.filename))
                new_img = Image(userId=current_user.id, productId=1, url=url)
                if(latest_product):
                    new_img.productId = latest_product.id + 1
                # add the new images to the database
                db.session.add(new_img)
                db.session.commit()
                i = i + 1
    else:
        flash('Please upload an image!')
        return redirect(url_for('mana.add'))

    # create a new product with the form data.
    new_product = Product(userId=current_user.id, name=product_name,
                          inventory=quantity, price=price, tag=tag, image=i-1)

    # add the new product to the database
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('main.index'))


@mana.route('/delete')
@login_required
def delete():
    PRODUCT_IMAGES_URLS = []
    product_name = ''
    product_price = 0
    images = Image.query.filter_by(userId=current_user.id).all()
    for image in images:
        product = Product.query.filter_by(id=image.productId).first()
        if(product):
            product_name = product.name
            product_price = product.price
            img_url = image.url
            PRODUCT_IMAGES_URLS.append(
                'static/img/' + str(product.userId) + '/' + img_url)
    if not PRODUCT_IMAGES_URLS:
        return redirect(url_for('main.index'))
    return render_template('delete.html', PRODUCT_IMAGES_URLS=PRODUCT_IMAGES_URLS, PRODUCT_NAME=product_name, PRODUCT_PRICE=product_price)


@mana.route('/delete', methods=['POST'])
@login_required
def delete_post():
    PRODUCT_IMAGES_URLS = []
    images = Image.query.filter_by(userId=current_user.id).all()
    for image in images:
        product = Product.query.filter_by(id=image.productId).first()
        if(product):
            img_url = image.url
            PRODUCT_IMAGES_URLS.append(
                'static/img/' + str(product.userId) + '/' + img_url)
    for url in PRODUCT_IMAGES_URLS:
        if(request.form.get(url)):
            path = url.replace("static/img/" + str(current_user.id) + '/', "")
            image_to_be_deleted = Image.query.filter_by(url=path).first()
            DELETION_PATH = os.path.join(mana.root_path, url)
            try:
                os.remove(DELETION_PATH)
            except:
                print('error occurred when deleting the image ' +
                      url + ' from server!')
            product_image_belong_to = Product.query.filter_by(
                id=image_to_be_deleted.productId).first()
            if(product_image_belong_to.image == 1):
                db.session.delete(product_image_belong_to)
            else:
                product_image_belong_to.image = product_image_belong_to.image - 1
            db.session.commit()  # update Product table
            db.session.delete(image_to_be_deleted)
            db.session.commit()  # update Image table

    return redirect(url_for('main.index'))


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')
