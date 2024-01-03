import cv2
from zarnevis import Zarnevis
import numpy as np
import os

# دایرکتوری حاوی فونت‌ها
font_dir = "font"
# لیست حروف و نام متناظر به انگلیسی
txt = [
    'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ه', 'ی']
name = ['aleph', 'beh', 'peh', 'teh', 'theh', 'jim', 'che', 'he jimi', 'khe', 'daal', 'zaal', 're', 'ze', 'zhe', 'sin', 'shin', 'sad', 'zad', 'taa', 'zaa', 'ayn', 'ghayn', 'feh', 'qaf', 'kaf', 'gaf', 'lam', 'mim', 'nun', 'vav', 'he', 'yaa']

# اندازه فونت
font_size = 350

# پیمایش در تمامی فایل‌های فونت
for font_file in os.listdir(font_dir):
    # فیلتر فقط فایل‌های .ttf
    if font_file.endswith('.ttf'):
        fontname, _ = os.path.splitext(font_file)
        output_dir = os.path.join('output', fontname)
        os.makedirs(output_dir, exist_ok=True)  # ساخت پوشه برای هر فونت
        # مسیر کامل فایل فونت
        full_font_path = os.path.join(font_dir, font_file)

        # تولید تصویر برای هر حرف
        for (char, eng_name) in zip(txt, name):
            # ساخت تصویر سفید
            image = np.zeros((512, 512, 3), dtype=np.uint8)
            image.fill(255)  # به رنگ سفید در می‌آید.

            # تنظیمات فونت
            text_x = 20
            text_y = 0

            # ایجاد نمونه‌ای از Zarnevis
            processor = Zarnevis(image=image, text=char, font_file=full_font_path,
                                 font_size=font_size, color=(0, 0, 0),
                                 text_coords=(text_x, text_y))

            # ترسیم حرف روی تصویر
            image = processor.draw_text()

            # ساخت نام فایل و ذخیره تصویر
            output_image_path = f'{output_dir}/{eng_name}_{fontname}.png'
            cv2.imwrite(output_image_path, image)

            # محتوای فایل caption
            caption_content = f"arabic letter {eng_name}, {fontname} typeface"
            # نام فایل caption
            caption_filename = f'{output_dir}/{eng_name}_{fontname}.caption'

            # ذخیره محتوای فایل caption
            with open(caption_filename, 'w', encoding='utf-8') as f:
                f.write(caption_content)
