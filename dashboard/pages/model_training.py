import streamlit as st

__all__ = ["model_training"]


def model_training():
    st.write("## Model")

    # Assets' paths
    model_architecture = "../assets/model_architecture.png"
    training_validation_acc = "../assets/training_validation_accuracy.png"
    training_validation_loss = "../assets/training_validation_loss.png"

    st.write("### Model Architecture")
    st.image(model_architecture)
    st.write("")
    st.write("### Data Split")
    st.write("""
             >- `39,416` samples for training (altered fingerprints)
             >- `9,854` samples for validation (altered fingerprints)
             >- `6,000` samples for testing (real fingerprints)
             """)
    st.write("")
    st.write("### Model Training Process")
    st.image(training_validation_acc)
    st.image(training_validation_loss)
