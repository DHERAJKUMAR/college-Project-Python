import cv2
def add_watermark(image_path,watermark_text, output_path):

image = cv2.imread(image_path)

if image is None:

print(f"Error: Unable to load image at '{image_path}"") 
return

height, width,_= image.shape

font = cv2.FONT_HERSHEY_SIMPLEX

font_scale = 1

color = (255, 255, 255)

thickness = 2

(text_width, text_height), _=cv2.getTextSize(watermark_text, font, font_scale, thickness)

x = width - text_width - 10

y = height - 10

cv2.putText(image, watermark_text, (x, y), font, font_scale, color, thickness)

cv2.imwrite(output_path, image) print(f"Watermarked image saved as '{output_path}"")

image_path = 'pics/madara.jpg' 
watermark_text = 'Copyright 2024' 
output_path = 'madara_watermarked.jpg' add_watermark(image_path, watermark_text, output_path)