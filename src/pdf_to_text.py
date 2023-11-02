import pdf2image
import pytesseract
import csv

text_lists = []
pdf_path = "./legal_will.pdf" # specify the path that contains will files (in pdf)

# Convert the pdf to images
pages = pdf2image.convert_from_path(pdf_path, dpi=300)

# Save the images into png file
n = 0
for page in pages:
    page.save("page"+str(n)+".png", 'png')
    new_text = pytesseract.image_to_string("page"+str(n)+".png") # extract the string from the images
    text_lists.append(new_text)
    n += 1

# Specify the CSV file name (default is use the same name as the pdf name)
csv_file = pdf_path[:-4] + ".csv"

# Write the data to a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["extracted texts"])
    for item in text_lists:
        writer.writerow([item])

print(f"Data has been written to {csv_file}")