from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
from dotenv import load_dotenv 
import os

def classify_waste(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # Replace this with the path to your image
    image = img.convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    #print("Class:", class_name[2:], end="")
    #print("Confidence Score:", confidence_score)

    return class_name, confidence_score


st.set_page_config(layout='wide')

st.title("E-Waste Classifier Sustainability App")

input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button("Classify"):
        
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.info("Your uploaded Image")
            st.image(input_img, use_column_width=True)
        with col2:
            st.info("Your Result")
            image_file = Image.open(input_img)
            label, confidence_score = classify_waste(image_file)
            col4, col5 = st.columns([1,1])
            if label == "0 Battery\n":
                st.success("The image is classified as BATTERY.")                
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\7.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Batteries contain precious metals like lithium, cobalt, nickel, and others. These metals are essential for their ability to store and release energy efficiently. However, extracting and refining these metals can be complex and may have environmental impacts. Recycling batteries helps recover these precious metals for reuse, reducing the need for new mining and preserving natural resources.   CREDIT POINTS:1")
            elif label == "1 Television\n":
                st.success("The image is classified as TELEVISION.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\11.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Television sets contain small amounts of precious metals like gold, silver, and copper. These metals are used in various components such as circuit boards, connectors, and wiring. While the quantity in each TV is relatively small, recycling these metals from old TVs can help recover valuable resources and reduce environmental impact.   CREDIT POINTS:4")
            elif label == "2 Printer\n":
                st.success("The image is classified as PRINTER.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Printers contain various precious metals such as gold, silver, and platinum, which are used in their electronic components and wiring. These metals are present in small quantities but are valuable due to their conductivity and resistance to corrosion. Recycling printers can help recover and reuse these precious metals, reducing environmental impact and conserving resources.   CREDIT POINTS:3")
            elif label == "3 Mobile\n":
                st.success("The image is classified as MOBILE.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Mobile phones contain small amounts of precious metals like gold, silver, and platinum. These metals are used in various components such as circuit boards and connectors. While the quantity of precious metals in each phone is relatively small, recycling these devices can help recover and reuse these valuable resources.   CREDIT POINTS:4")
            elif label == "4 Mouse\n":
                st.success("The image is classified as MOUSE.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\11.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("A computer mouse contains small amounts of precious metals like gold, silver, and copper in its electrical components. These metals are used to conduct electricity and ensure the mouse functions properly. While the quantities are tiny, they contribute to the mouse's performance and durability, making it an essential electronic accessory.   CREDIT POINTS:1")
            elif label == "5 Keyboard\n":
                st.success("The image is classified as KEYBOARD.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\3.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\6.jpg", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Keyboards contain small amounts of precious metals such as gold, silver, and palladium. These metals are used in various components like electrical contacts and circuit boards. While the quantities are relatively small per keyboard, recycling them can help recover these valuable materials for reuse in other electronic devices.   CREDIT POINTS:1")
            elif label == "6 PCB\n":
                st.success("The image is classified as PCB.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Printed Circuit Boards (PCBs) contain small amounts of precious metals like gold, silver, and copper. These metals are used in the conductive pathways on the board. While the quantity of these metals in each PCB is relatively small, when accumulated in large quantities, they can be valuable for recycling purposes.   CREDIT POINTS:5")
            elif label == "7 Microwave\n":
                st.success("The image is classified as MICROWAVE.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Microwaves contain small amounts of precious metals like gold, silver, and copper in various components like circuit boards and wiring. While the quantity of these metals is relatively low, recycling them can help recover valuable resources and reduce environmental impact.   CREDIT POINTS:2")
            elif label == "8 Player\n":
                st.success("The image is classified as PLAYER.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\3.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\6.jpg", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\13.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Precious metals like gold, silver, and platinum are used in small amounts inside a player, mainly for electrical contacts and circuitry. These metals provide excellent conductivity, corrosion resistance, and durability, ensuring the smooth operation of the player's electronic components while minimizing the risk of damage or malfunction over time.  CREDIT POINTS:2")
            elif label == "9 Washing Machine\n":
                st.success("The image is classified as WASHING MACHINE.")
                with col4:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\6.jpg", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\12.png", use_column_width=True)
                with col5:
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\14.png", use_column_width=True)
                    st.image(r"C:\Users\Dell\Desktop\sdg goals\15.png", use_column_width=True)
                with col3:
                    st.info("CREDIT POINTS")
                    st.info("Precious metals like gold, silver, and platinum are used in small amounts inside a player, mainly for electrical contacts and circuitry. These metals provide excellent conductivity, corrosion resistance, and durability, ensuring the smooth operation of the player's electronic components while minimizing the risk of damage or malfunction over time.  CREDIT POINTS:1")
            else:
                st.error("The image is not classified as any relevant class.")
          
                            