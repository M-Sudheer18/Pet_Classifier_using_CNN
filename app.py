import streamlit as st
from huggingface_hub import hf_hub_download

# Page Status
st.set_page_config(
    page_title="AI Pet Classifier",
    page_icon="🐶",
    layout="centered"
)


from PIL import Image
import numpy as np
import tensorflow as tf

# Model Loading 
@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id= "Sudheer17/AI_Pet_Classifier",
        filename='cnn_model.h5'
    )
    return tf.keras.models.load_model(model_path)

model = load_model()



# SideBar with Model and Project Details
with st.sidebar:

    st.title("About")

    st.info(
        """
        ## CNN Image Classifier

        Model : CNN

        Classes:
        - 🐶 Dog
        - 🐱 Cat

        Framework:
        - TensorFlow
        - Streamlit
        """
    )




st.title("🐶🐱 AI Pet Classifier")

st.markdown(
    """
    Upload a **Cat  🐱** or **Dog  🐶** image and let the CNN model
    identify it instantly.
    """
)

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    
    # Input Image
    display_img = Image.open(uploaded_file)

    def preprocess(uploaded_file):

        # Adding RGB COlors if GrayScaled Image
        img = Image.open(uploaded_file).convert('RGB')

        # Resize the image
        img = img.resize((64, 64))

        # Converting img to array
        img_array = np.array(img, dtype=np.float32)

        # Normalize (same as training: rescale=1./255)
        img_array = img_array / 255.0

        # Add Batch Dimensions
        img_array = np.expand_dims(img_array, axis = 0)
    
        return img, img_array  
    
    image, img_array = preprocess(uploaded_file)


    # Displaying the image
    st.image(
        display_img,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Prediction 

    if st.button("🔍 Predict"):
        
        with st.spinner("Analyzing image.."):
            # Getting Prediction
            result = model.predict(img_array, verbose = 0)

            # Probability
            prob = result[0][0]

            # Class Prediction
            if prob >= 0.5:
                prediction = "🐶 Dog"
                confidence = prob * 100
            else:
                prediction = "🐱 Cat"
                confidence = (1 - prob) * 100

            st.markdown("---")
            st.subheader("Prediction Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Prediction", prediction)

            with col2:
                st.metric("Confidence", f"{confidence:.2f}%")

            if confidence < 70:
                st.warning("⚠️ The model has low confidence. Try uploading a clearer image.")



# Footer
st.markdown("---")

st.caption("Made with ❤️ using TensorFlow & Streamlit")
