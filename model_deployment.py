import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
from model import get_cnn_block

def predict_similarity(image1, image2):
    # Preprocess images
    def preprocess(img):
        img = Image.fromarray(img).convert('L')
        img = img.resize((28, 28))
        img_array = np.array(img)
        img_array = img_array.astype('float32') / 255.0
        return img_array.reshape(1, 28, 28)
    
    # Load model
    model = tf.keras.models.load_model('siamese_model.h5')
    
    # Prepare images
    img1_processed = preprocess(image1)
    img2_processed = preprocess(image2)
    
    # Get prediction
    similarity = model.predict([img1_processed, img2_processed])[0][0]
    
    return float(similarity)

# Create Gradio interface
demo = gr.Interface(
    fn=predict_similarity,
    inputs=[
        gr.Image(label="First Image", type="numpy"),
        gr.Image(label="Second Image", type="numpy")
    ],
    outputs=gr.Number(label="Similarity Score (0-1)"),
    title="Siamese Network - Image Similarity",
    description="Upload two images to check their similarity. Score closer to 1 means more similar.",
    examples=[
        ["example1.jpg", "example2.jpg"],
        ["example3.jpg", "example4.jpg"]
    ]
)

if __name__ == "__main__":
    demo.launch()